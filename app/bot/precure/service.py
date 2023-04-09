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

def get_calling_name(str):
    # プリキュアを呼んでるメッセージかどうか
    match = re.search(r'([ァ-ヶー]+)をよんで', str)
    if match:
        return match.group(1)
    return None

def get_data(name):
    return data[name]

def get_call_message(name):
    # プリキュアを呼ぶためのmessageを取得
    return {
        'role': 'system',
        'content': data[name]['call'],
    }
