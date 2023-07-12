from datetime import datetime

LOG_FILE_NAME = "file_organizer.log"

def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}\n"
    with open(LOG_FILE_NAME, "a") as log_file:
        log_file.write(log_message)