from fastapi import FastAPI, HTTPException
import requests
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정
origins = ["http://localhost:9000"]  # Quasar dev 서버 주소

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TMDb API 키를 환경 변수에서 가져옴
TMDB_API_KEY = os.getenv('TMDB_API_KEY', '625a3368bc3077f6923a608db044030c')

@app.get("/recommendations/{movie_id}")
def get_recommendations(movie_id: int):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations"
    params = {"api_key": TMDB_API_KEY}
    
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="TMDb API error")
    
    return response.json()

@app.get("/search/")
def search_movie(query: str):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": query}
    
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="TMDb API error")
    
    return response.json()

