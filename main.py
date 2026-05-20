from generate_logs import generate_logs
from analyze_logs import analyze_logs
from ai_judge_gemini import ai_judge
from send_mail import send_mail


def main():
    generate_logs()
    analysis_result = analyze_logs()
    ai_result = ai_judge(analysis_result)
    send_mail(analysis_result, ai_result)
    print("全処理が完了しました")


if __name__ == "__main__":
    main()
