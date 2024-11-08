 
def log_message(message):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{message}\n")