import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email_report(
    sender_email,
    app_password,
    receiver_email,
    subject,
    body,
    attachment_path,
    host="smtp.gmail.com",
    port=587
):
    print("Creating the email message...")
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with open(attachment_path, "rb") as file:
        part = MIMEApplication(file.read(), Name="weekly_customer_spend.pdf")
        part["Content-Disposition"] = 'attachment; filename="weekly_customer_spend.pdf"'
        msg.attach(part)

    if port == 465:
        with smtplib.SMTP_SSL(host, port) as server:
            print("Logging into the email server...")
            server.login(sender_email, app_password)
            print("Sending the email...")
            server.send_message(msg)
    else:
        with smtplib.SMTP(host, port) as server:
            print("Starting connection...")
            server.starttls()
            print("Logging into the email server...")
            server.login(sender_email, app_password)
            print("Sending the email...")
            server.send_message(msg)

    print("📧 Email sent successfully.")
