import logging
import re
import yaml
import os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

data = {}
with open(os.path.dirname(os.path.abspath(__file__)) + '/data.yml', 'r') as f:
    yaml_data = yaml.safe_load(f)
    for row in yaml_data:
        data[row['name']] = row
if data == {}:
    raise Exception('データファイルがありません。')

def is_calling(str):
    # プリキュアを呼んでるメッセージかどうか
    return re.search(r'([ァ-ヶー])*をよんで', str)

def call_message(name):
    # プリキュアを呼ぶためのmessageを取得
    return {
        'role': 'system',
        'content': data[name]['call'],
    }
