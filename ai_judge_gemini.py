import os
from dotenv import load_dotenv
from google import genai

LOG_FILE = "logs/sample.log"

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY が .env に設定されていません。")

client = genai.Client(api_key=gemini_api_key)

with open(LOG_FILE, "r", encoding="utf-8") as f:
    logs = f.read()

prompt = f"""
あなたはシステム運用監視の担当者です。
以下のログを分析し、異常の有無を日本語で判定してください。

出力形式：
1. 総合判定
2. 気になる点
3. 想定される原因
4. 推奨対応

ログ：
{logs}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print("===== Gemini AI判定結果 =====")
print(response.text)