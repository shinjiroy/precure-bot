import os
import logging
import json
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from bot.events.mention import main as mention

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = App(
    token=os.environ['SLACK_BOT_TOKEN'],
    process_before_response=True,
)
handler = SlackRequestHandler(app)

@app.event('url_verification')
def url_verification(event, say):
    logger.info('test2')
    return {
        'statusCode': 200,
        'body': json.dumps({'challenge': event['challenge']})
    }

# メンションがあった時の応答
@app.event('app_mention')
def app_mention(event, say):
    mention(event, say)

def lambda_handler(event, context):

    response = {
        'statusCode': 200,
        'body': 'test',
    }
    logger.info(event)
    logger.info(context)
    # response = handler.handle(event, context)
    return response
