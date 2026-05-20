import random
from datetime import datetime, timedelta

levels = ["INFO", "WARNING", "ERROR"]

messages = {
    "INFO": [
        "Login Success",
        "File Uploaded",
        "Scheduled Backup Completed",
        "User Access Granted"
    ],
    "WARNING": [
        "CPU Usage High",
        "Disk Space Low",
        "Memory Usage Warning"
    ],
    "ERROR": [
        "Failed Login",
        "Database Connection Failed",
        "Server Timeout",
        "Unauthorized Access Attempt"
    ]
}

start_time = datetime.now()

with open("logs/sample.log", "w", encoding="utf-8") as f:

    for i in range(100):

        log_time = start_time + timedelta(
            seconds = i * random.randint(5, 30)
        )

        level = random.choices(
            levels,
            weights = [70, 20, 10]
        )[0]

        message = random.choice(messages[level])

        user_id = f"user{random.randint(100,999)}"

        log = f"{log_time} | {level} | {message} | {user_id}"

        f.write(log + "\n")

print("ログ生成完了")
