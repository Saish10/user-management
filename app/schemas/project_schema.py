"""Module for project schemas."""

from typing import List
from pydantic import BaseModel


class TeamMember(BaseModel):
    """Team member schema."""

    id: int
    name: str
    role: str


class ProjectDetails(BaseModel):
    """Project details schema."""

    start_date: str
    end_date: str
    team_members: List[TeamMember] = []


class Project(BaseModel):
    """Project schema."""

    project_id: int
    name: str
    details: ProjectDetails
