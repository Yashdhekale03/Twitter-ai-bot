from fastapi import FastAPI, HTTPException
from twitter_client import post_tweet

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from the Twitter AI Bot!"}

@app.post("/tweet")
def tweet(message: str):
    result = post_tweet(message)
    if result["status"] == "success":
        return result
    else:
        raise HTTPException(status_code=500, detail=result["message"])
