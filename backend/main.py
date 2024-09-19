import redis
import json
from fastapi import FastAPI, HTTPException
import requests
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Redis 클라이언트 설정
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

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

# 캐싱된 데이터 조회 함수
def get_cached_data(key):
    data = redis_client.get(key)
    if data:
        return json.loads(data)
    return None

# 캐싱된 데이터 저장 함수
def cache_data(key, data, expire_time=3600):
    redis_client.set(key, json.dumps(data), ex=expire_time)

# 영화 검색 엔드포인트
@app.get("/search/")
def search_movies(query: str, language: str = "ko"):
    cache_key = f"search:{query}"
    
    # 캐싱된 데이터가 있으면 반환
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": query, "language": language}
    
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="TMDb API error")
    
    data = response.json()
    
    # 응답 데이터 캐싱
    cache_data(cache_key, data, expire_time=3600)  # 캐시 만료 시간 1시간으로 설정

    return data

# 영화 추천 엔드포인트
@app.get("/recommendations/{movie_id}")
def get_recommendations(movie_id: int, language: str = "ko"):
    cache_key = f"recommendations:{movie_id}"
    
    # 캐싱된 데이터가 있으면 반환
    cached_data = get_cached_data(cache_key)
    if cached_data:
        return cached_data
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations"
    params = {"api_key": TMDB_API_KEY, "language": language}
    
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="TMDb API error")
    
    data = response.json()
    
    # 응답 데이터 캐싱
    cache_data(cache_key, data, expire_time=3600)  # 캐시 만료 시간 1시간으로 설정
    
    return data

