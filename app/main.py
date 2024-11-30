"""Main module for the application."""

from fastapi import FastAPI
from app.routers import user_routes, invite_routes


app = FastAPI(
    title="User Management API", docs_url="/docs", redoc_url="/redoc"
)

app.include_router(user_routes.router, prefix="/api")
app.include_router(invite_routes.router, prefix="/api")


