"""Routes for sending invitation emails."""

import os
from fastapi import Request
from app.config.settings import BASE_DIR
from app.routers.api_router import router
from app.services.email_service import send_invitation_email
from app.constants import RECIPIENTS, GITHUB_LINK


def generate_docs_links(request: Request) -> dict:
    """
    Generate dynamic documentation links based on the current request's
    base URL.

    Args:
        request (Request): The FastAPI request object.

    Returns:
        dict: A dictionary containing the Swagger and ReDoc links.
    """
    base_url = str(request.base_url).rstrip("/")
    return {
        "documentation_link": f"{base_url}/redoc",
        "swagger_link": f"{base_url}/docs",
    }


@router.post("/send_invite")
async def send_invite(request: Request) -> dict[str, str]:
    """
    Send the invitation email with dynamic API documentation links.

    Args:
        request (Request): The FastAPI request object.

    Returns:
        dict: A success message indicating the email was sent.
    """
    # Generate dynamic documentation links
    docs_links = generate_docs_links(request)

    # Prepare the email context
    template_name = "invitation_email.html"
    context = {
        **docs_links,
        "github_link": GITHUB_LINK,  # Add the GitHub link to the context
    }
    recipients: list[str] = RECIPIENTS
    attachments = [os.path.join(BASE_DIR, "firestore_ss.png")]

    # Send the email
    await send_invitation_email(
        recipients, template_name, context, attachments
    )
    return {"detail": "Invitation email sent successfully"}
