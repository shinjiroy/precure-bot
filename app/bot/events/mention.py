import logging
import bot.core as core
import re
from slack_sdk.web import WebClient

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def strip_angle_bracket_tags(str):
    # strから<>で囲まれた箇所(メンション)を削除する
    return re.sub(r'<[^>]*>', '', str)

def is_calling(str):
    # プリキュアを呼んでるメッセージかどうか
    return re.search(r'([ァ-ヶー])*をよんで', str)

# メンションされたときの処理
def main(event, say, client: WebClient):

    text = strip_angle_bracket_tags(event['text'])
    if ('thread_ts' in event):
        # スレッドの場合には、スレッドのメッセージを取得して対話モードになるように組み立てる
        replies = client.conversations_replies(
            channel=event['channel'],
            ts=event['ts'],
            inclusive=True
        ).validate()

        messages = []
        for reply in replies.get('messages'):
            match = is_calling(reply['text'])
            if match:
                # プリキュア呼び出し時
                messages.append({
                    'role': 'system',
                    'content': f'{match.group()}の口調で話して',
                })
            elif reply.get('bot_id'):
                # botの入力の場合
                messages.append({
                    'role': 'assistant',
                    'content': reply['text']
                })
            else:
                # ユーザーの入力の場合
                # bot以外の入力は全てuserとする
                messages.append({
                    'role': 'user',
                    'content': strip_angle_bracket_tags(reply['text'])
                })
        core.response(say, messages, event['ts'])
    else:
        # スレッドでない場合にはプリキュアを呼んでいる場合のみ考慮する
        # メンションされたテキストからプリキュアの名前を抽出する
        match = is_calling(text)
        if match:
            messages = [{
                'role': 'system',
                'content': f'{match.group()}の口調で話して',
            }]
            # 会話スタート
            core.response(say, messages, event['ts'])
