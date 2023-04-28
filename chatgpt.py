import openai


class ChatGPT:
    """ChatGPT"""

    def __init__(self, api_key, model='gpt-3.5-turbo', max_tokens=1000, temperature=0.5):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def get_response_from_chat(self, text):
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": text
                }
            ],
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        return response['choices'][0]['message']['content']
