from flask import Flask, request, jsonify
from utils.response_retriever import load_responses, get_response
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq()

app = Flask(__name__)
responses = load_responses('src/data/predefined_responses.json')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question')
    answer = get_response(user_question, responses)
    if not answer:
        answer = get_generic_response(user_question)
    return jsonify({'answer': answer})

def get_generic_response(question):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": question,
        }
    ],
    model="llama-3.3-70b-versatile",
)

    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    app.run(debug=True)

