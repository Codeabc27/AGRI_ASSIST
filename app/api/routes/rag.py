from fastapi import APIRouter

from pydantic import BaseModel

from RAG.rag_pipeline import retrieve_answer

router = APIRouter(prefix="/rag", tags=["RAG Assistant"])


class Question(BaseModel):
    question: str


@router.post("/ask")
def ask_question(data: Question):

    answer = retrieve_answer(data.question)

    return {"answer": answer}
