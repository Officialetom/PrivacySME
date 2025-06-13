from datetime import datetime

def log_event(event):
    with open("activity.log", "a") as f:
        f.write(f"{datetime.now()}: {event}\n")