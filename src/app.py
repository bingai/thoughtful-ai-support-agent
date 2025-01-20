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
    """
    Handles POST requests to the '/ask' endpoint. Retrieves a predefined answer
    to the user's question if available, otherwise generates a generic response.

    The function expects a JSON payload with a 'question' key. It returns a JSON
    object with the corresponding 'answer'.

    Returns:
        Response: A JSON response containing the answer to the user's question.
    """

    user_question = request.json.get('question')
    answer = get_response(user_question, responses)
    if not answer:
        answer = get_generic_response(user_question)
    return jsonify({'answer': answer})

def get_generic_response(question):
    """
    Retrieves a generic response to the user's question if the answer is not in the
    predefined responses dataset. The function uses the Groq API to generate a
    completion for the given question.

    Args:
        question (str): The user's question.

    Returns:
        str: A generic response to the user's question.
    """
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

