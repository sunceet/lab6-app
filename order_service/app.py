import redis
import json
import time
import random

r = redis.Redis(host='redis', port=6379, db=0)

def create_order(order_id, customer):
    order = {
        "order_id": order_id,
        "customer": customer,
        "status": "created"
    }
    r.publish('orders', json.dumps(order))
    print(f"[Order Service] Order {order_id} published for {customer}", flush=True)

if __name__ == "__main__":
    order_counter = 1
    customers = ["Alice", "Bob", "Charlie", "Diana"]
    while True:
        customer = random.choice(customers)
        create_order(order_counter, customer)
        order_counter += 1
        time.sleep(7)