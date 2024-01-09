from fastapi import FastAPI 
from pydantic import BaseModel
from .utils import get_qa_chain

ENDPOINT_URL = "http://admin:admin@opensearch-node:9200"
LLM_CONFIG = {
    'max_new_tokens': 256, 
    'temperature': 0.01, 
    'context_length': 8000
}

app = FastAPI()
qa_chain = get_qa_chain(ENDPOINT_URL, LLM_CONFIG)


class Question(BaseModel):
    text: str = ""

@app.post("/qa_chain")
async def t5(input: Question):
    response = qa_chain({'query': input.text})
    return f'\nAnswer: {response["result"]}'
