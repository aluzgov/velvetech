from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from filter_bad_words.config import FRONTEND_PORT


def create_app():
    app = FastAPI()

    origins = [
        "http://localhost",
        f"http://localhost:{FRONTEND_PORT}",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
