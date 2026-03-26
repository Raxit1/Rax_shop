import sqlite3
import os

def reset_database():
    # Delete existing database
    if os.path.exists("users.db"):
        os.remove("users.db")
        print("✓ Old database deleted")
    
    # Create new database with all tables
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Users table with admin column
    cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        MobileNo TEXT,
        password TEXT,
        is_admin INTEGER DEFAULT 0
    )
    """)
    
    # Orders table
    cursor.execute("""
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        order_id TEXT UNIQUE,
        full_name TEXT,
        email TEXT,
        phone TEXT,
        address TEXT,
        city TEXT,
        postal_code TEXT,
        payment_method TEXT,
        notes TEXT,
        total_amount REAL,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT DEFAULT 'Processing',
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)
    
    # Order items table
    cursor.execute("""
    CREATE TABLE order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT,
        product_name TEXT,
        product_category TEXT,
        quantity INTEGER,
        price REAL,
        subtotal REAL,
        FOREIGN KEY(order_id) REFERENCES orders(order_id)
    )
    """)
    
    # Shipments table
    cursor.execute("""
    CREATE TABLE shipments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT UNIQUE,
        tracking_number TEXT,
        shipped_date TIMESTAMP,
        estimated_delivery DATE,
        current_location TEXT,
        status TEXT DEFAULT 'Order Placed',
        notes TEXT,
        FOREIGN KEY(order_id) REFERENCES orders(order_id)
    )
    """)
    
    # Products table
    cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id TEXT UNIQUE,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT,
        image_url TEXT,
        stock INTEGER DEFAULT 0,
        rating REAL DEFAULT 0,
        features TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Order status history table
    cursor.execute("""
    CREATE TABLE order_status_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT,
        status TEXT,
        updated_by TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        notes TEXT,
        FOREIGN KEY(order_id) REFERENCES orders(order_id)
    )
    """)
    
    conn.commit()
    conn.close()
    
    print("✓ New database created with all tables")
    print("\nNow run setup_admin.py to create admin user")

if __name__ == "__main__":
    reset_database()