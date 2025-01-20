import json

def load_responses(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def get_response(question, responses):
    normalized_question = question.lower().strip()
    
    for item in responses.get('questions', []):
        if item['question'].lower().strip() == normalized_question:
            return item['answer']
    return None