import json
from collections import Counter


def analyze_logs(log_file="logs/sample.log"):
    level_counts = Counter()
    total_count = 0

    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            total_count += 1

            parts = line.strip().split("|")

            if len(parts) >= 2:
                level = parts[1].strip()
                level_counts[level] += 1

    info_count = level_counts["INFO"]
    warning_count = level_counts["WARNING"]
    error_count = level_counts["ERROR"]

    abnormal_count = warning_count + error_count
    abnormal_rate = abnormal_count / total_count * 100 if total_count > 0 else 0

    result = {
        "total_count": total_count,
        "levels": {
            "INFO": info_count,
            "WARNING": warning_count,
            "ERROR": error_count,
        },
        "abnormal": {
            "count": abnormal_count,
            "rate": round(abnormal_rate, 1),
        },
    }

    return result


if __name__ == "__main__":
    result = analyze_logs()
    print(json.dumps(result, ensure_ascii=False, indent=2))
