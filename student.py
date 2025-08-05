from fastapi import  FastAPI, Path, Query
from typing import List, Dict


app = FastAPI()


@app.get("/users/{username}")
def read_username(username: str = Path(..., description="Ім'я користувача для привітання")):
    return {"message": f"Привіт, {username}!"}

@app.get("/groups/{group_id}/students/{student_id}")
def read_student_in_group(
    group_id: int = Path(..., description="ID групи студента"),
    student_id: int = Path(..., description="ID студента в групі")
):
    return {
        "group_id": group_id,
        "student_id": student_id,
        "message": f"Інформація про студента {student_id} у групі {group_id}"
    }
