from datetime import datetime

def log_attack(message, attack_type):
    with open("waf_logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] {attack_type}: {message}\n")
