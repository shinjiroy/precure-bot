import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']
model_engine = "gpt-3.5-turbo"

def generate_response(messages: list) -> str:
    try:
        response = openai.Completion.create(
            engine=model_engine,
            messages=messages,
        )
        return response.choices[0].text
    except openai.error.AuthenticationError as e:
        print("OpenAI authentication error: ", e)
    except openai.error.APIError as e:
        print("OpenAI API error: ", e)

# https://slack.dev/bolt-python/api-docs/slack_bolt/context/say/say.html#slack_bolt.context.say.say.Say
def start_thread(say, precure_name: str, ts: str) -> None:
    res = generate_response([{
            'role': 'assistant',
            'content': f'{precure_name}の口調で話して',
        }])
    say(
        text=res,
        thread_ts=ts,
    )

def response(say, message: str, thread_ts: str) -> None:
    say(
        text=message,
        thread_ts=thread_ts,
    )
