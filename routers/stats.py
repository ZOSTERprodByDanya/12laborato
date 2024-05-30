from fastapi import APIRouter, Request
from typing import Dict

router = APIRouter()

request_count: Dict[str, int] = {
    "GET /version": 0,
    "GET /posts": 0,
    "POST /posts": 0,
    "PUT /posts/{post_id}": 0,
    "DELETE /posts/{post_id}": 0,
}

@router.get("/")
async def get_stats():
    return request_count

@router.middleware("http")
async def count_requests(request: Request, call_next):
    endpoint = f"{request.method} {request.url.path}"
    if endpoint in request_count:
        request_count[endpoint] += 1
    response = await call_next(request)
    return response
