import os
import logging
import json
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler
from bot.events.mention import main as mention

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = App(
    token=os.environ['SLACK_BOT_TOKEN'],
    signing_secret=os.environ['SLACK_SIGNING_SECRET'],
    process_before_response=True,
)
handler = SlackRequestHandler(app)

@app.event('url_verification')
def url_verification(event, say):
    return {
        'statusCode': 200,
        'body': json.dumps({'challenge': event['challenge']})
    }

@app.event('message')
def message(event, say):
    # 何もしない
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'message event'})
    }

# メンションがあった時の応答
@app.event('app_mention')
def app_mention(event, say):
    mention(event, say, app.client)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'app_mention event'})
    }

def lambda_handler(event, context):

    logger.info(event)
    headers = event['headers']
    if ('x-slack-retry-num' in headers):
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'ignore retry'})
        }

    response = handler.handle(event, context)
    return response
