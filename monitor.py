import sys
import time
from celery.result import AsyncResult
from celery_app import app

if len(sys.argv) < 2:
    print("Cach dung: python monitor.py <TASK_ID>")
    sys.exit()

task_id = sys.argv[1]

while True:
    result = AsyncResult(task_id, app=app)

    print(f"Task ID: {task_id}")
    print(f"Trang thai: {result.state}")

    if result.info:
        print(f"Thong tin: {result.info}")

    print("-" * 40)

    if result.ready():
        print("Ket qua cuoi cung:")
        print(result.get(propagate=False))
        break

    time.sleep(2)
