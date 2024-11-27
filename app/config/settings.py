"""Configuration settings for the application."""

import os
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
