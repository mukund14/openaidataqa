from dataQA.data_loader import DataLoader
from dataQA.query_processor import QueryProcessor

class DataQA:
    def __init__(self, file_path, api_key):
        self.loader = DataLoader(file_path)
        self.data = self.loader.load_data()
        self.query_processor = QueryProcessor(self.data, api_key)

    def ask(self, question):
        return self.query_processor.ask(question)

# Example usage
if __name__ == "__main__":
    file_path = 'path_to_your_dataset.csv'  # replace with your file path
    api_key = 'your_openai_api_key'  # replace with your OpenAI API key
    data_qa = DataQA(file_path, api_key)
    while True:
        question = input("Ask a question about the data (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        answer = data_qa.ask(question)
        print("Answer:", answer)
