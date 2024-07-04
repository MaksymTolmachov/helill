import smtplib
import jinja2
import config
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
def send_email(
    recipients: list[str],
    # /,
    *,
    email_body: str,
    email_subject: str,
    attachment: str = None,
):
    TOKEN = config.TOKEN_UKR_NET
    USER = config.USER
    SMTP_SERVER = config.SMTP_SERVER

    msg = MIMEMultipart("alternative")
    msg["Subject"]  = email_subject
    msg["from"]  = f"<Email was sent from {USER}>"
    msg["To"] = ",".join(recipients)
    msg["Reply-To"]  = USER
    msg["Returm-Path"] = USER
    msg["X-Mailer"] = "decorator"

    text_to_send  = MIMEText(email_body, "html")
    msg.attach(text_to_send)

    mail = smtplib.SMTP_SSL(SMTP_SERVER)
    mail.login(USER, TOKEN)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()


def create_welcome_letter(params: dict) -> str:
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template_file = "letter_template.html"
    template = template_env.get_template(template_file)
    output = template.render(params)
    return





