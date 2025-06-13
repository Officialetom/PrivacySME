import shutil, datetime

def backup_db():
    name = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    shutil.copy("data/database.json", name)
    return f"Backup saved as {name}"