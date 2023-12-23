from fastapi import APIRouter
from pydantic import BaseModel
class Message(BaseModel):
    message: str
router=APIRouter(
    prefix="/user",
    tags=["user"]
)
@router.get('/auth')
def userGoogleAuth():
    return {
        "message":"working"
    }

@router.post('/chat/response')
def getResponse(message:Message):
    print(message)
    return {"message":message.message}
#uvicorn main:app --reload