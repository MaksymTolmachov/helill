import email_sender_homework


def main():
    list_of_recipients = [
        "aaaa@ukr.net",

    ]

    # email_sender_homework.send_email(
    #     list_of_recipients, mail_subject="Head", mail_body="Body"
    # )

    email_sender_homework.create_welcome_letter({"user": "Alex"})


if __name__ == '__main__':
    main()
