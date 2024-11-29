"""Configuration settings for the application."""


import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


class Settings:
    """Configuration settings for the application."""

    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD")
    MAIL_FROM: str = os.getenv("MAIL_FROM")
    MAIL_PORT: int = int(os.getenv("MAIL_PORT"))
    MAIL_SERVER: str = os.getenv("MAIL_SERVER")


settings = Settings()


BASE_DIR = Path(__file__).resolve().parent.parent.parent
