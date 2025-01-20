# Thoughtful AI Support Agent

## Objective

The Thoughtful AI Support Agent is designed to assist users with basic questions about Thoughtful AI using predefined responses. This project aims to streamline customer support by providing quick and accurate answers to common inquiries.

## Project Structure

```
thoughtful-ai-support-agent
├── src
│   ├── app.py                # Entry point of the application
│   ├── data
│   │   └── predefined_responses.json  # Dataset of predefined questions and answers
│   ├── utils
│   │   └── response_retriever.py     # Function to retrieve responses from the dataset
├── streamlit_app.py          # Streamlit frontend application
├── requirements.txt          # Project dependencies
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone git@github.com:bingai/thoughtful-ai-support-agent.git
   cd thoughtful-ai-support-agent
   ```

2. Create a conda environment and install the required dependencies:
   ```bash
   conda create --name flask_app_env python=3.11
   conda activate flask_app_env
   pip install -r requirements.txt
   ```

## Usage

To run the Flask backend, execute the following command:

```bash
python src/app.py
```

To run the Streamlit frontend, execute the following command:

```bash
streamlit run streamlit_app.py
```

Follow the on-screen instructions to interact with the AI agent. Open your browser and go to `http://localhost:8501` to use the chat interface.

The Thoughtful AI Support Agent utilizes a set of hardcoded responses to answer frequently asked questions about Thoughtful AI's services. It retrieves the most relevant answers from a predefined dataset and presents them in a user-friendly format. The agent also has the capability to provide generic responses for questions outside its predefined dataset.