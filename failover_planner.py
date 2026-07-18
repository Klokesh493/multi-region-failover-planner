import csv
import sys


def choose_region(rows):
    candidates = [row for row in rows if row["health"].lower() == "green" and int(row["free_capacity_pct"]) >= 25 and int(row["replication_lag_sec"]) <= 60]
    if not candidates:
        return None
    return sorted(candidates, key=lambda row: (-int(row["free_capacity_pct"]), int(row["replication_lag_sec"])))[0]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        choice = choose_region(list(csv.DictReader(handle)))
    print(choice["region"] if choice else "no-safe-failover")


if __name__ == "__main__":
    main(sys.argv[1])
