# GPT-3 Evaluator API

An API to evaluate answers using OpenAI's GPT-3.5 Turbo model, implemented with FastAPI.

This API allows you to submit a question and answer pair, and it will return an evaluation score and detailed feedback based on criteria such as accuracy, completeness, relevance, clarity, and depth.

## Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn
- OpenAI Python library
- Requests (for testing)

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/gpt-3-evaluator-api.git
cd gpt-3-evaluator-api


2. Install the required libraries:
pip install fastapi uvicorn openai requests


3. Set your OpenAI API key as an environment variable:
export OPENAI_API_KEY="your_openai_api_key"


## Running the API

Run the API locally using Uvicorn:
uvicorn main:app --host 0.0.0.0 --port 8000


The API will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

- POST `/evaluate_answer`: Submit a question and answer pair, and receive an evaluation score and detailed feedback.

## Testing

Use the provided `test_api.py` script to test the API with various question and answer pairs:

python test_api.py


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


Remember to replace yourusername with your GitHub username in the README.md file. You can create a new repository with the suggested name and description, then add the code and README.md to the repository. Don't forget to include a LICENSE file as well, such as the MIT License.


