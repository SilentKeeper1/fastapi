from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Movie API")


class Movie(BaseModel):
    id: int
    title: str
    genre: str
    year: int
    rating: float

movies_db = [
    Movie(id=1, title="The Shawshank Redemption", genre="Drama", year=1994, rating=9.3),
    Movie(id=2, title="Pulp Fiction", genre="Crime", year=1994, rating=8.9),
    Movie(id=3, title="The Dark Knight", genre="Action", year=2008, rating=9.0),
]

@app.get("/movies", response_model=List[Movie])
def get_movies():
    return movies_db


@app.post("/movies", response_model=Movie)
def add_movie(movie: Movie):
    movies_db.append(movie)
    return movie


@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int):
    for movie in movies_db:
        if movie.id == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, updated_movie: Movie):
    for index, movie in enumerate(movies_db):
        if movie.id == movie_id:
            movies_db[index] = updated_movie
            return updated_movie
    raise HTTPException(status_code=404, detail="Movie not found")

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    global movies_db
    movies_db = [movie for movie in movies_db if movie.id != movie_id]
    return {"message": "Movie deleted successfully"}