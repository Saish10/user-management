import os

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from jinja2 import Template

from app.config.settings import settings

# Correct the email configuration initialization
conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=True,  # Correctly enable STARTTLS
    MAIL_SSL_TLS=False,  # Disable SSL directly
    USE_CREDENTIALS=True,  # Use credentials as True for Gmail
)


async def send_invitation_email(
    recipients: list,
    template_name: str,
    context: dict,
    attachments: list = None,
):
    """
    Send an email with attachments using a template loaded from the templates folder.

    Args:
        recipients (list): List of recipient email addresses.
        template_name (str): Name of the template file.
        context (dict): Context variables to render the template.
        attachments (list): List of file paths to attach to the email.
    """
    # Construct the full path to the template
    template_path = os.path.join("app", "templates", template_name)

    # Load the template file
    if not os.path.exists(template_path):
        raise FileNotFoundError(
            f"Template '{template_name}' not found in templates folder."
        )

    with open(template_path, "r", encoding="utf-8") as file:
        template = Template(file.read())

    # Render the template with the provided context
    body = template.render(context)

    # Prepare the email message
    message = MessageSchema(
        subject="API Documentation and Firestore Details",
        recipients=recipients,
        body=body,
        subtype=MessageType.html,
        attachments=attachments if attachments else [],  # Attachments, if any
    )

    # Send the email
    fm = FastMail(conf)
    await fm.send_message(message)
