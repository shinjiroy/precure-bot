import openai
import os
import logging

openai.api_key = os.environ['OPENAI_API_KEY']
model_engine = 'gpt-3.5-turbo'

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def _generate_response(messages: list) -> str:
    try:
        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=messages,
        )
        return response.choices[0].message.content
    except openai.error.AuthenticationError as e:
        print('OpenAI authentication error: ', e)
    except openai.error.APIError as e:
        print('OpenAI API error: ', e)

def response(say, messages: list, thread_ts: str, precure_data: dict) -> None:
    res = _generate_response(messages)
    logger.info(res)
    say(
        text=res,
        thread_ts=thread_ts,
        icon_emoji=precure_data['icon_emoji'],
        username=precure_data['name'],
    )
