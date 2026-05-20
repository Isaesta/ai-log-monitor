import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv


def send_mail(analysis_result, ai_result):
    load_dotenv()

    mail_from = os.getenv("MAIL_FROM")
    mail_to = os.getenv("MAIL_TO")
    mail_password = os.getenv("MAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))

    subject = f"【ai-log-monitor】ログ監視通知: {ai_result['severity']}"

    body = f"""
ログ監視処理が完了しました。

===== 集計結果 =====
総ログ数: {analysis_result['total_count']}
INFO: {analysis_result['levels']['INFO']}
WARNING: {analysis_result['levels']['WARNING']}
ERROR: {analysis_result['levels']['ERROR']}
異常件数: {analysis_result['abnormal']['count']}
異常率: {analysis_result['abnormal']['rate']}%

===== AI判定 =====
重要度: {ai_result['severity']}
概要: {ai_result['summary']}
判断理由: {ai_result['reason']}
推奨対応: {ai_result['recommended_action']}
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


if __name__ == "__main__":
    sample_analysis_result = {
        "total_count": 100,
        "levels": {
            "INFO": 70,
            "WARNING": 20,
            "ERROR": 10
        },
        "abnormal": {
            "count": 30,
            "rate": 30.0
        }
    }

    sample_ai_result = {
        "severity": "Medium",
        "summary": "ERRORとWARNINGが一定数発生しています。",
        "reason": "異常率が30%であり、運用上確認が必要です。",
        "recommended_action": "ERRORログの内容を確認してください。"
    }

    send_mail(sample_analysis_result, sample_ai_result)
