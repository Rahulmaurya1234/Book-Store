from datetime import datetime

with open("cron.log", "a") as file:
    file.write(f"Cron executed at {datetime.now()}\n")