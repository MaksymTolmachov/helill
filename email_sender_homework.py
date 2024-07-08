import config_homework
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import smtplib
import os
import jinja2
from email import encoders

def send_email(
        recipients: list[str],
        *,
        mail_body: str,
        mail_subject: str,
        attachment: str = None,
):
    TOKEN = config_homework.TOKEN_UKR_NET_HW
    USER = config_homework.MAIL_USER_HW
    SMTP_SERVER = config_homework.SMTP_SERVER_HW

    msg = MIMEMultipart("alternative")
    msg["Subject"] = mail_subject
    msg["From"] = f"<Email was sent from {USER}>"
    msg["Reply-To"] = USER
    msg["Return-Path"] = USER
    msg["X-Mailer"] = "decorator"

    text_to_send = MIMEText(mail_body, "html")
    msg.attach(text_to_send)

    if attachment:
        is_file_exists = os.path.exists(attachment)
        if is_file_exists:
            basename = os.path.basename(attachment)
            filesize = os.path.getsize(attachment)
            file = MIMEBase('aplication', f'octet-stream; name={basename}')
            file.set_payload(open(attachment, 'br').read())
            file.add_header("Content-Discription", f"attachment; filename{attachment}, size={filesize} ")
            encoders.encode_base64(file)
            msg.attach(file)


    mail = smtplib.SMTP_SSL(SMTP_SERVER)
    mail.login(USER, TOKEN)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()


def create_welcome_letter(params: dict) -> str:
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template_file = "letter_template_hw.html"
    template = template_env.get_template(template_file)
    out_put = template.render(params)
    return out_put





