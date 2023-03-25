import logging
import bot.core as core
import re

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def strip_angle_bracket_tags(str):
    # strから<>で囲まれた箇所(メンション)を削除する
    return re.sub(r'<[^>]*>', '', str)

# メンションされたときの処理
def main(event, say):

    text = strip_angle_bracket_tags(event['text'])
    if ('thread_ts' in event):
        # スレッドの場合には、スレッドのメッセージを取得して対話モードになるように組み立てる
        core.response
    else:
        # スレッドでない場合にはプリキュアを呼んでいる場合のみ考慮する
        # メンションされたテキストからプリキュアの名前を抽出する
        match = re.search(r'([ァ-ヶー])*をよんで', text)
        if match:
            # 会話スタート
            core.start_thread(say, match.group(), event['ts'])

