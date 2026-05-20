import os
import json
from dotenv import load_dotenv
from google import genai

LOG_FILE = "logs/sample.log"


def extract_json_text(text):
    text = text.strip()

    if text.startswith("```json"):
        text = text.removeprefix("```json").strip()

    if text.startswith("```"):
        text = text.removeprefix("```").strip()

    if text.endswith("```"):
        text = text.removesuffix("```").strip()

    return text


def ai_judge(analysis_result):
    load_dotenv()

    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY が .env に設定されていません。")

    client = genai.Client(api_key=gemini_api_key)

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = f.read()

    prompt = f"""
あなたはシステム運用監視の担当者です。
以下のログ分析結果とログ本文をもとに、異常判定をしてください。

必ず以下のJSON形式だけで回答してください。
Markdownのコードブロックは付けないでください。
説明文も不要です。

{{
  "severity": "High / Medium / Low のいずれか",
  "summary": "100文字以内の要約",
  "reason": "判断理由を150文字以内",
  "recommended_action": "運用者が最初に取るべき対応を1つだけ"
}}

ログ分析結果:
{json.dumps(analysis_result, ensure_ascii=False, indent=2)}

ログ本文:
{logs}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    try:
        json_text = extract_json_text(response.text)
        ai_result = json.loads(json_text)
    except json.JSONDecodeError:
        ai_result = {
            "severity": "Unknown",
            "summary": "AI判定結果のJSON解析に失敗しました。",
            "reason": response.text,
            "recommended_action": "AI応答内容を確認してください。"
        }

    return ai_result


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

    result = ai_judge(sample_analysis_result)
    print(json.dumps(result, ensure_ascii=False, indent=2))