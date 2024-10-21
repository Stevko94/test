from fastapi import FastAPI
from app.posts.routers.post import router

def create_application() -> FastAPI:
    application = FastAPI(title="posts")
    application.include_router(router)
    return application


app = create_application()
