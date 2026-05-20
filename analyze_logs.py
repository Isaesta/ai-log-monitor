from collections import Counter

log_file = "logs/sample.log"

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
abnormal_rate = abnormal_count / total_count * 100

print("===== ログ分析結果 =====")
print(f"総ログ数  : {total_count}")
print(f"INFO     : {info_count}")
print(f"WARNING  : {warning_count}")
print(f"ERROR    : {error_count}")
print(f"異常件数  : {abnormal_count}")
print(f"異常率    : {abnormal_rate:.1f}%")
