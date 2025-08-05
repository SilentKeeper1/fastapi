from fastapi import FastAPI, Path, Query, Header, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from typing import Optional

app = FastAPI()


@app.get("/users/{id}")   # /users/55
def path(id: int = Path(...)):
    return {"id": id}

@app.get("/users/{id}")   # /users/55
def path(id: int = Path(0)):
    return {"id": id}

@app.get("/users/{id}")   # /users/55
def path(id: Optional[int] = Path(None)):
    return {"id": id}


@app.get("/users") # /users/?id=55
def query(id: int = Query(...)):
    return {"id": id}

@app.get("/users") # /users/?id=55
def query(id: int = Query(0, title="Ми отримуємо id", description="Це id користувача")):
    return {"id": id}


@app.get("/items/")
def list_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/items/")
def list_items(skip: int = Query(0, ge=0), limit: int = Query(10, gt=0, le=10)):  # ge >= 0, gt > 0, le <= 10, lt < 10
    return {"skip": skip, "limit": limit}


@app.get("/items/search")
def list_items(item_name: str = Query(None, max_length=50)):
    return ...



@app.get("/items/")
async def read_items(
    user_agent: str = Header(None),
    x_token: str = Header(...)
):
    if x_token != "secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


    return {"User-Agent": user_agent, "X-Token": x_token}


#  curl -H "Accept: application/json" http://127.0.0.1:8000/info/
@app.get("/info/")
async def get_info(accept: str = Header(default="application/json")):
    data = {"message": "This is a JSON response"}


    if "application/json" in accept:
        return JSONResponse(content=data)


    elif "text/html" in accept:
        html_content = "<html><body><h1>This is an HTML response</h1></body></html>"
        return HTMLResponse(content=html_content)


    else:
        raise HTTPException(status_code=406, detail="Not Acceptable")
