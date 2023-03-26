import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re

app = FastAPI()
openai.api_key = "------------------Get this api key from OpenAI--------------"

class EvaluationInput(BaseModel):
    question: str
    answer: str

class EvaluationOutput(BaseModel):
    exam_score: str
    details: dict

async def chat_with_gpt_35_turbo(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

@app.post("/evaluate_answer", response_model=EvaluationOutput)
async def evaluate_answer(evaluation_input: EvaluationInput):
    # Construct the prompt
    prompt = (
        f"Please evaluate this answer on a scale of 0 to 100 based on these criteria: accuracy, completeness, relevance, clarity, and depth:"
        f"\nQuestion: \"{evaluation_input.question}\""
        f"\nAnswer: \"{evaluation_input.answer}\""
        f"\n\nTotal Score (0-100): "
    )

    result = await chat_with_gpt_35_turbo(prompt)

    if not result:
        raise HTTPException(status_code=500, detail="Could not generate a valid response")

    # Extract the exam score
    score_pattern = r"(\d+)\s*[\r\n]+"
    score_match = re.search(score_pattern, result)

    if not score_match:
        raise HTTPException(status_code=500, detail="Could not extract the exam score")

    exam_score = score_match.group(1)

    # Remove the score from the response to get the evaluation details
    evaluation_details = re.sub(score_pattern, "", result).strip()

    return {"exam_score": exam_score, "details": {"question": evaluation_input.question, "answer": evaluation_input.answer, "evaluation": evaluation_details}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
