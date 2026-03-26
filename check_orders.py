import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

print("=" * 50)
print("ALL ORDERS IN DATABASE:")
print("=" * 50)

orders = cursor.execute("""
    SELECT order_id, user_id, status, total_amount, order_date 
    FROM orders 
    ORDER BY order_date DESC
""").fetchall()

for order in orders:
    print(f"Order: {order[0]} | User ID: {order[1]} | Status: {order[2]} | Total: ${order[3]}")

print("\n" + "=" * 50)
print("SHIPMENTS:")
print("=" * 50)

shipments = cursor.execute("SELECT order_id, status, current_location FROM shipments").fetchall()
for shipment in shipments:
    print(f"Order: {shipment[0]} | Status: {shipment[1]} | Location: {shipment[2]}")

conn.close()