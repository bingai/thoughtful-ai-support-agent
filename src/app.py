from flask import Flask, request, jsonify
from utils.response_retriever import load_responses, get_response

app = Flask(__name__)
responses = load_responses('src/data/predefined_responses.json')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question')
    answer = get_response(user_question, responses)
    return jsonify({'answer': answer})

if __name__ == "__main__":
    app.run(debug=True)