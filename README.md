# Golf Assistant

## Overview
Golf Assistant is a chatbot designed to help golf enthusiasts improve their game by providing tailored advice and insights. Utilizing a Retrieval-Augmented Generation (RAG) architecture, the chatbot leverages a curated list of comprehensive golf manuals to deliver precise and contextually relevant guidance.

## Features
- **Knowledge Base**: Incorporates well-respected golf manuals including:
  - Bob's Living Golf Book
  - First Swing Golfer's Guide
  - Golf Hacks
  - The Ultimate Golfers Guide

- **Intelligent Response Generation**: Powered by OpenAI's API, the chatbot employs both Large Language Models (LLM) and Model Embedding techniques to generate knowledgeable and accurate responses.

- **Vector Database**: Utilizes QDrant for efficient storage and retrieval of embeddings, enhancing the chatbot's ability to fetch relevant information quickly.

- **User Interface**: Built with Streamlit, offering a clean and interactive user experience.

- **Orchestration**: Managed via Langchain, ensuring smooth operation and scalability of the application.

## Installation

To set up the Golf Assistant on your local machine, follow these steps:
```bash
# Clone the repository
git clone https://github.com/dsuarezsouto/golf-assistant.git

# Navigate to the project directory
cd golf-assistant

# Create python environemtn and install dependencies
pipenv install --python 3.11
pipenv shell
```

Create `src/config.py` script:

```python
import os
OPENAI_API_KEY='Your OpenAI key'

def set_environment():
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
```

```bash
# Run the application
streamlit run src/app.py
```

## Usage
After installation, you can interact with the Golf Assistant through the Streamlit UI. Simply input your golf-related queries, and the assistant will retrieve information and suggestions based on the extensive knowledge embedded from the golf manuals.

## Future Improvements
- **Integration of User Performance Data**: Plans to incorporate JSONs containing individual playing metrics (e.g., strikes per hole, yards per club) to personalize advice further, transforming the assistant into a virtual golf caddie.

- **Exploration of LLM Agent**: Investigating the potential evolution into a more autonomous LLM Agent to enhance decision-making capabilities on the course.
