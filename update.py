from datetime import datetime

with open("log.txt", "a") as f:
    f.write(f"Update at {datetime.now()}\n")
