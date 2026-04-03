log_file = "logs.txt"

ip_count = {}

with open(log_file, "r") as file:
    for line in file:
        if "failed" in line:
            ip = line.split(" ")[0]

            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1

print("---- Suspicious Activity ----")

for ip, count in ip_count.items():
    if count > 3:
        print(f"Suspicious IP: {ip} | Attempts: {count}")
