import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "pratik138.rejoice@gmail.com"  # Enter your address
receiver_email = "leyijiy250@songsign.com"  # Enter receiver address
password = "pratik@0011"
otp = 343434
message = f"""
Subject: Hi there

login otp is : {otp}."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)