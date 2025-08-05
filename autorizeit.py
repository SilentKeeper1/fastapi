from fastapi import FastAPI, Header, HTTPException, status
from typing import Optional

app = FastAPI()

SECRET_TOKEN = "Bearer supersecretkey"

@app.get("/simple-data/")
async def get_simple_data(

    authorization: str = Header(..., description="Обов'язковий заголовок 'Authorization' з токеном 'Bearer supersecretkey'"),
    x_custom_info: Optional[str] = Header(None, alias="X-Custom-Info", description="Необов'язковий кастомний заголовок 'X-Custom-Info'")
):
    if authorization != SECRET_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неправильний або відсутній токен авторизації. Використовуйте 'Bearer supersecretkey'."
        )

    response_payload = {
        "message": "Дані успішно отримано!",
        "authorization_status": "OK"
    }

    if x_custom_info:
        response_payload["custom_info"] = x_custom_info

    return response_payload