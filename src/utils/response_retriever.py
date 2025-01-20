import json

def load_responses(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['questions']

def get_response(user_question, responses):
    for item in responses:
        if user_question.lower() in item['question'].lower():
            return item['answer']
    return "Sorry, I don't have an answer for that question."

if __name__ == "__main__":
    responses = load_responses('../data/predefined_responses.json')
    print(get_response("What does the eligibility verification agent (EVA) do?", responses))