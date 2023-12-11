from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test():
    text = "раз два три четыре стоп"
    response = client.post("/textToBraille/", json={"text": text})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['text'] == text
    assert json_data['braille'] == "⠗⠁⠵ ⠙⠺⠁ ⠞⠗⠊ ⠟⠑⠞⠮⠗⠑ ⠎⠞⠕⠏"