import time
from celery_app import app


@app.task(bind=True)
def process_order(self, order_id, customer_name, amount):
    self.update_state(
        state="PROGRESS",
        meta={"step": "Kiem tra don hang", "progress": 25}
    )
    time.sleep(2)

    self.update_state(
        state="PROGRESS",
        meta={"step": "Xu ly thanh toan", "progress": 50}
    )
    time.sleep(2)

    self.update_state(
        state="PROGRESS",
        meta={"step": "Dong goi san pham", "progress": 75}
    )
    time.sleep(2)

    self.update_state(
        state="PROGRESS",
        meta={"step": "Hoan thanh don hang", "progress": 100}
    )
    time.sleep(1)

    return {
        "order_id": order_id,
        "customer_name": customer_name,
        "amount": amount,
        "status": "SUCCESS",
        "message": "Don hang da duoc xu ly thanh cong"
    }


@app.task(bind=True, max_retries=3, default_retry_delay=3)
def unstable_payment(self, order_id, amount):
    try:
        if self.request.retries < 2:
            raise Exception("Loi ket noi cong thanh toan")

        return {
            "order_id": order_id,
            "amount": amount,
            "status": "PAYMENT_SUCCESS",
            "retries": self.request.retries,
            "message": "Thanh toan thanh cong sau khi retry"
        }

    except Exception as exc:
        raise self.retry(exc=exc)
