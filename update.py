import os
import json
import random
from datetime import datetime, timezone

# Configuration
LOGS_DIR = "logs"
NOTES_FILE = "data/daily_notes.json"

def get_current_date():
    now = datetime.now(timezone.utc)
    return now.strftime("%Y-%m-%d"), now.strftime("%Y-%m")

def update_log():
    date_str, month_str = get_current_date()
    file_path = os.path.join(LOGS_DIR, f"{month_str}.md")
    
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)
        
    # Load pool of realistic notes
    notes_pool = []
    if os.path.exists(NOTES_FILE):
        try:
            with open(NOTES_FILE, 'r') as f:
                notes_pool = json.load(f)
        except Exception as e:
            print(f"Error loading notes: {e}")

    # Robustness check: Ensure pool is not empty
    if not isinstance(notes_pool, list) or len(notes_pool) == 0:
        notes_pool = [{
            "topic": "Documentation Review", 
            "summary": "Refreshed knowledge on recent library updates and best practices."
        }]
    
    selected_note = random.choice(notes_pool)
    entry = f"- {date_str}: {selected_note['topic']} - {selected_note['summary']}\n"
    
    header = f"# Learning Log: {month_str}\n\n"
    
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(header)
            
    with open(file_path, "a") as f:
        f.write(entry)

if __name__ == "__main__":
    update_log()
