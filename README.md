### README.md

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
├── requirements.txt          # Project dependencies
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd thoughtful-ai-support-agent
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the customer support AI agent, execute the following command:

```
python src/app.py
```

Follow the on-screen instructions to interact with the AI agent.

## Overview

The Thoughtful AI Support Agent utilizes a set of hardcoded responses to answer frequently asked questions about Thoughtful AI's services. It retrieves the most relevant answers from a predefined dataset and presents them in a user-friendly format. The agent also has the capability to provide generic responses for questions outside its predefined dataset.