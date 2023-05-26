from pydantic import BaseModel

class VectorInput(BaseModel):
    text: str

class Vectorizer:
    model: str

    def __init__(self, model: str):
        self.model = model

    async def vectorize(self, text: str):
        vector = self.model.encode(text)
        return vector
