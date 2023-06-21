import random
import requests
import pytexit
import re


API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
HEADERS = {"Authorization": "Bearer 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"}
FORMULAS = []
with open("formulas.csv", "r") as f:
    for row in list(f)[1:]:
        FORMULAS.append(row.strip().replace('"', ""))


def is_latex(string):
    string = re.sub(r"\\\w+", "", str(string))
    try:
        pytexit.py2tex(string)
        return True
    except:
        return False


def query(payload):
    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={
            "inputs": f"{payload}",
            "parameters": {
                "top_p": random.uniform(0.8, 1.0),
            },
        },
    )
    return response.json()[0]["generated_text"]


def get_latex():
    res = rf"""Generate new completely unique and random but correct LaTeX formula shorter than 50 symbols
        1: ${random.choice(FORMULAS)}$
        2: ${random.choice(FORMULAS)}$
        3: ${random.choice(FORMULAS)}$   
        4: $"""
    while res.count("$") < 8:
        res = query(res)
    res = res.split("$")[7]
    while not is_latex(res):
        res = res[:-1]
    return res


for i in range(100):
    print(get_latex())
