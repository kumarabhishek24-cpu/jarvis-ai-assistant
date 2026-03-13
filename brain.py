import requests

def ask_ai(question):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": question,
        "stream": False
    }

    response = requests.post(url, json=data)

    result = response.json()

    return result["response"]