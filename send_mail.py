import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

mail_from = os.getenv("MAIL_FROM")
mail_to = os.getenv("MAIL_TO")
mail_password = os.getenv("MAIL_PASSWORD")
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT", "587"))

subject = "【ai-log-monitor】ログ監視通知"
body = """
ログ監視処理が完了しました。

詳細は分析結果を確認してください。
"""

msg = MIMEText(body, "plain", "utf-8")
msg["Subject"] = subject
msg["From"] = mail_from
msg["To"] = mail_to

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(mail_from, mail_password)
    server.send_message(msg)

print("メール送信完了")
