import schedule
import time

def scheduled_task():
    print("Ejecutando tarea programada")

schedule.every().day.at("00:00").do(scheduled_task)

while True:
    schedule.run_pending()
    time.sleep(60)
