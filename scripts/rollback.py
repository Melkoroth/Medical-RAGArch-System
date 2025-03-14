import os
import shutil

BACKUP_PATH = "./data/prompts_backup/"
PROMPT_PATH = "./data/prompts/"

def backup_prompts():
    os.makedirs(BACKUP_PATH, exist_ok=True)
    if os.path.exists(PROMPT_PATH):
        for file in os.listdir(PROMPT_PATH):
            shutil.copy(os.path.join(PROMPT_PATH, file), os.path.join(BACKUP_PATH, file))

def rollback_prompts():
    if os.path.exists(BACKUP_PATH):
        for file in os.listdir(BACKUP_PATH):
            shutil.copy(os.path.join(BACKUP_PATH, file), os.path.join(PROMPT_PATH, file))
        print("Rollback completado: restaurado el estado anterior de los prompts.")
    else:
        print("No hay versiones anteriores disponibles para rollback.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "backup":
        backup_prompts()
    elif len(sys.argv) > 1 and sys.argv[1] == "rollback":
        rollback_prompts()