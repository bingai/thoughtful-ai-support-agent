import json

def load_responses(filepath):
    """
    Loads predefined responses from a JSON file.

    Args:
        filepath (str): Path to the JSON file containing the responses.

    Returns:
        dict: A dictionary containing the predefined responses, where each key is a question and the value is the answer.
    """
    with open(filepath, 'r') as file:
        return json.load(file)

def get_response(question, responses):
    """
    Retrieves the predefined answer for a given question from the provided responses.

    Args:
        question (str): The question for which an answer is to be retrieved.
        responses (dict): A dictionary containing predefined questions and answers.

    Returns:
        str or None: The answer corresponding to the question if found in the responses; 
                     otherwise, None.
    """

    normalized_question = question.lower().strip()
    
    for item in responses.get('questions', []):
        if item['question'].lower().strip() == normalized_question:
            return item['answer']
    return None