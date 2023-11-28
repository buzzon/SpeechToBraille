from typing import Union

from fastapi import FastAPI, Request, Body
from pydantic import BaseModel

from main import convertTextToBraille

app = FastAPI()


class Data(BaseModel):
    text: str

@app.post("/textToBraille")
def main(data: Data):
    try:
        text = data.text
        braille = convertTextToBraille(text)
        return {"text": text, "braille": braille}
    except:
        return "Something went wrong, check if you have field 'text' in your request"


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}