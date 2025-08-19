from fastapi import FastAPI

app = FastAPI(title="Bank-jwt")

@app.get('/')
def home():
    return {'message':'Hello Bank'}