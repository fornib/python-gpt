"""
https://platform.openai.com/docs/api-reference/introduction
"""

from pathlib import Path
import openai

API_FILE = 'OPENAI_API_KEY.txt'

with Path(API_FILE).open(mode='r', encoding='utf-8') as text:
    openai.api_key = text.read().strip()  # or os.getenv("OPENAI_API_KEY")

# openai.Model.list()  # https://api.openai.com/v1/models  https://platform.openai.com/docs/models

# prompt = f'''Suggest three names for an animal that is a superhero.
# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: [...]
# Names:'''
# response = openai.Completion.create(  # https://api.openai.com/v1/completions
#     model='text-davinci-003',
#     prompt='This is a test, are you working?',
#     temperature=0.7,  # 0.6, defaults 1
#     max_tokens=64,  # 7, 150, default 16; 1 token ~ ¾ word
#     top_p=1.0,
#     frequency_penalty=0,
#     presence_penalty=0,
#     stop=None,
#     )


# openai.Embedding.create(input=x, engine='text-embedding-ada-002')['data'][0]['embedding']


def get_assistant_message(messages: list):
    response = openai.ChatCompletion.create(  # https://api.openai.com/v1/chat/completions
        model='gpt-3.5-turbo',  # 'gpt-3.5-turbo', 'gpt-4'
        messages=messages,
        temperature=0.7,  # 1.0
        #stream=True,
        max_tokens=128,  # 64, defaults to inf / 4096
        )
    # print(str(response).replace('\n',''))
    # for response in response_stream:
    #     print(response.choices[0].delta.content, end='')
    return response.choices[0].message


def main():
    messages = [
            #{"role": "system", "content": "You are a lazy assistant. Your goal is to use as few words as possible. Monosyllabic responses are ideal. When you aren't sure, do your best to guess with ballpark figures or heuristic understanding. It is better to oversimplify than to give a qualified answer. If you are comparing rough numbers just give a percentage range. It is better to simply say you don't know than to explain nuance about the question or its ambiguities."},
            #{"role": "system", "content": "Simplify and use as few words as possible."},
            #{"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "Answer as concisely as possible."},
        ]
    
    try:
        while True:
            prompt = input('User: ')
            messages.append({"role": "user", "content": prompt})  # {"role": "user", "content": "..."}
            message_gpt = get_assistant_message(messages)  # {"role": "assistant", "content": "..."}
            messages.append(message_gpt)
            print('Assistant:', message_gpt.content)
    except KeyboardInterrupt:
        print("\nEnd.")


if __name__ == '__main__':
    main()
    