import logging
import bot.core as core
import re
from slack_sdk.web import WebClient
import bot.precure.service as precure

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def strip_angle_bracket_tags(str):
    # strから<>で囲まれた箇所(メンション)を削除する
    return re.sub(r'<[^>]*>', '', str)

# メンションされたときの処理
def main(event, say, client: WebClient):

    text = strip_angle_bracket_tags(event['text'])
    if ('thread_ts' in event):
        # スレッドの場合には、スレッドのメッセージを取得して対話モードになるように組み立てる
        replies = client.conversations_replies(
            channel=event['channel'],
            ts=event['thread_ts'],
            inclusive=True
        ).validate()

        messages = []
        precure_data = {}
        for reply in replies.get('messages'):
            precure_name = precure.get_calling_name(reply['text'])
            if precure_name:
                # プリキュアを呼び出した時の入力の場合
                messages.append(precure.get_call_message(precure_name))
                precure_data = precure.get_data(precure_name)
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
        core.response(say, messages, event['ts'], precure_data)
    else:
        # スレッドでない場合にはプリキュアを呼んでいる場合のみ考慮する
        # メンションされたテキストからプリキュアの名前を抽出する
        precure_name = precure.get_calling_name(text)
        if precure_name:
            messages = [precure.get_call_message(precure_name)]
            # 会話スタート
            core.response(say, messages, event['ts'], precure.get_data(precure_name))
        else:
            say(
                text=f'すきなキャラクターのおなまえを「○○をよんで」とボットにおねがいしてね！',
            )
