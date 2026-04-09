import redis
import json
import time

r = redis.Redis(host='redis', port=6379, db=0)
p = r.pubsub()
p.subscribe('orders')

print("[Notification Service] Listening to 'orders' channel...", flush=True)

for message in p.listen():
    if message['type'] == 'message':
        try:
            order = json.loads(message['data'])
            print(f"[Notification Service] Notification sent for Order {order['order_id']} to {order['customer']}", flush=True)
        except Exception as e:
            print(f"Error parsing message: {e}")
            