from tasks import process_order, unstable_payment

orders = [
    {"order_id": "DH001", "customer_name": "Nguyen Van A", "amount": 120000},
    {"order_id": "DH002", "customer_name": "Tran Thi B", "amount": 250000},
    {"order_id": "DH003", "customer_name": "Le Van C", "amount": 99000},
    {"order_id": "DH004", "customer_name": "Pham Thi D", "amount": 310000},
    {"order_id": "DH005", "customer_name": "Hoang Van E", "amount": 450000},
]

print("Dang gui cac don hang vao he thong phan tan...\n")

task_ids = []

for order in orders:
    task = process_order.delay(
        order["order_id"],
        order["customer_name"],
        order["amount"]
    )

    task_ids.append(task.id)

    print(f"Da gui don hang: {order['order_id']}")
    print(f"Task ID: {task.id}")
    print("-" * 40)

print("\nGui task thanh toan loi de demo retry...\n")

retry_task = unstable_payment.delay("DH_RETRY_001", 500000)

print(f"Task retry ID: {retry_task.id}")

print("\nDanh sach Task ID can theo doi:")
for task_id in task_ids:
    print(task_id)

print("\nHay dung lenh: python monitor.py <TASK_ID>")
