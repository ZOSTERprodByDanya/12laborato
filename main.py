from fastapi import FastAPI
from routers import version, posts, stats

app = FastAPI()

app.include_router(version.router, prefix="/version")
app.include_router(posts.router, prefix="/posts")
app.include_router(stats.router, prefix="/stats")

@app.on_event("startup")
async def startup_event():
    print("App has started")
