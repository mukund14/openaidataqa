import openai

class OpenAIIntegration:
    def __init__(self, api_key):
        openai.api_key = api_key

    def ask(self, question, context):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Context: {context}\n\nQuestion: {question}\n\nAnswer:",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        answer = response.choices[0].text.strip()
        return answer
