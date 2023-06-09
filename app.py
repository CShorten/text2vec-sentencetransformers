from fastapi import FastAPI, Response, status
from vectorizer import Vectorizer, VectorInput
from meta import Meta
import os
from sentence_transformers import SentenceTransformer

app = FastAPI()

model = SentenceTransformer.load("./models")

meta_info = Meta()


@app.get("/.well-known/live", response_class=Response)
@app.get("/.well-known/ready", response_class=Response)
def live_and_ready(response: Response):
    response.status_code = status.HTTP_204_NO_CONTENT


@app.get("/meta")
def meta():
    return meta_info.get()


@app.post("/vectors")
async def read_item(item: VectorInput, response: Response):
    try:
        vector = await model.vectorize(item.text)
        return {"text": item.text, "vector": vector.tolist(), "dim": len(vector)}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}