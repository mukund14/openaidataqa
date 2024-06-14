from dataQA.openai_integration import OpenAIIntegration

class QueryProcessor:
    def __init__(self, data, api_key):
        self.data = data
        self.openai_integration = OpenAIIntegration(api_key)

    def ask(self, question):
        context = self.data.to_string()
        return self.openai_integration.ask(question, context)
