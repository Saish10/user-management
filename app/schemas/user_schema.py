"""Module for user schemas."""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, The FastAPI User Management API"

from pydantic import BaseModel
from app.schemas.project_schema import Project


class User(BaseModel):
    """User schema"""
    id: int
    name: str
    email: str
    phone: str
    projects: Project
