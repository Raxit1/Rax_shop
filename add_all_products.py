import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# ==================== ELECTRONICS PRODUCTS ====================
electronics_products = [
    # Mobile Phone
    ("PROD-ELEC-001", "Mobile Phone", "Electronics", 599.99, 
     "Flagship smartphone with cutting-edge technology", 
     "https://darlingretail.com/cdn/shop/files/iPhone_15_Blue_Pure_Back_iPhone_15_Blue_Pure_Front_2up_Screen__WWEN_800x.jpg?v=1695103868", 
     50, 4.8, "5G Connectivity,12MP Camera,256GB Storage"),
    
    # Laptop
    ("PROD-ELEC-002", "Laptop", "Electronics", 1299.99, 
     "High-performance laptop for professionals", 
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiQrqGNNTR7xwgo2dIb0enMOFgw_5N3X26dA&s", 
     30, 4.9, "Intel i7 Processor,16GB RAM,512GB SSD,Aluminum Body"),
    
    # Camera
    ("PROD-ELEC-003", "Camera", "Electronics", 899.99, 
     "Professional grade digital camera", 
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuNGdjIdNIOvAPNpYRi-VN5Nii-bfpEU3mJA&s", 
     25, 4.7, "24MP Sensor,4K Video,Wi-Fi & Bluetooth"),
    
    # Audio Headphones
    ("PROD-ELEC-004", "Audio Headphones", "Electronics", 349.99, 
     "Premium noise-cancelling wireless headphones", 
     "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=400&fit=crop", 
     60, 4.8, "Active Noise Cancellation,40 Hour Battery"),
    
    # Smart Watch
    ("PROD-ELEC-005", "Smart Watch", "Electronics", 199.99, 
     "Feature-rich smartwatch for daily wear", 
     "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&h=400&fit=crop", 
     80, 4.6, "Heart Rate Monitor,GPS Tracking,5 Day Battery,"),
    
    # Portable Speaker
    ("PROD-ELEC-006", "Portable Speaker", "Electronics", 179.99, 
     "Powerful portable Bluetooth speaker", 
     "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400&h=400&fit=crop", 
     70, 4.7, "24 Hour Battery,Waterproof Design,Bluetooth 5.0"),
    
    # Mechanical Keyboard
    ("PROD-ELEC-007", "Mechanical Keyboard", "Electronics", 149.99, 
     "Premium mechanical keyboard for gaming", 
     "https://m.media-amazon.com/images/I/71ZRus2YNcL._AC_UF894,1000_QL80_.jpg", 
     45, 4.8, "RGB Backlight,Mechanical Switches"),
    
    # Gaming Mouse
    ("PROD-ELEC-008", "Gaming Mouse", "Electronics", 79.99, 
     "High-precision gaming mouse", 
     "https://images.unsplash.com/photo-1527814050087-3793815479db?w=400&h=400&fit=crop", 
     100, 4.5, "16000 DPI Sensor,Customizable Buttons"),
]

# ==================== BOOKS PRODUCTS ====================
books_products = [
    # The Great Novel
    ("PROD-BOOK-001", "The Great Novel", "Books", 24.99, 
     "An epic fiction novel with compelling storytelling", 
     "https://www.crossword.in/cdn/shop/files/81Lfw-skUsL._SL1500.jpg?v=1757741415", 
     100, 4.8, "Hardcover,450 Pages,Award Winner,Bestseller"),
    
    # Python Programming
    ("PROD-BOOK-002", "Python Programming", "Books", 34.99, 
     "Master Python with this comprehensive guide", 
     "https://www.wileyindia.com/pub/media/catalog/product/cache/20f980a1f90e8cec7a3c8f2cf40a32a8/9/7/9789357465304_1.jpg", 
     75, 4.9, "Technical,600 Pages,Code Examples,Beginner Friendly"),
    
    # Science Explained
    ("PROD-BOOK-003", "Science Explained", "Books", 28.99, 
     "Complex science made simple and fun", 
     "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=400&h=400&fit=crop", 
     80, 4.7, "Educational,380 Pages,Illustrations"),
    
    # Business Success
    ("PROD-BOOK-004", "Business Success", "Books", 32.99, 
     "Learn strategies from successful entrepreneurs", 
     "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=400&h=400&fit=crop", 
     60, 4.8, "Business,520 Pages,Case Studies,Practical Tips"),
    
    # Mystery Thriller
    ("PROD-BOOK-005", "Mystery Thriller", "Books", 26.99, 
     "Suspenseful mystery with unexpected twists", 
     "https://m.media-amazon.com/images/I/71D9loFTEGL._AC_UF1000,1000_QL80_.jpg", 
     90, 4.6, "Thriller,400 Pages,Page Turner,Suspenseful,Mystery"),
    
    # World History
    ("PROD-BOOK-006", "World History", "Books", 30.99, 
     "Fascinating tales from human civilization", 
     "https://cdn.exoticindia.com/images/products/thumbnails/t800x600/books-2019-015/nbz456.jpg", 
     70, 4.7, "History,Maps,Timeline,Historical,Detailed"),
    
    # Self Help Guide
    ("PROD-BOOK-007", "Self Help Guide", "Books", 22.99, 
     "Transform your life with proven techniques", 
     "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=400&h=400&fit=crop", 
     120, 4.5, "Self Help,Exercises,Motivational,Practical,"),
    
    # Fantasy Adventure
    ("PROD-BOOK-008", "Fantasy Adventure", "Books", 27.99, 
     "Epic fantasy with magical worlds and adventures", 
     "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=400&h=400&fit=crop", 
     85, 4.8, "Fantasy,Epic Journey,Magic"),
]

# ==================== GROCERY PRODUCTS ====================
grocery_products = [
    # Fresh Potatoes
    ("PROD-GROC-001", "Fresh Potatoes (1kg)", "Grocery", 3.99, 
     "Fresh farm potatoes, perfect for cooking", 
     "https://cdn.pixabay.com/photo/2016/08/11/08/04/potato-1585060_1280.jpg", 
     500, 4.7, "Fresh Harvest,Rich in Potassium,Farm Fresh"),
    
    # Fresh Apples
    ("PROD-GROC-002", "Fresh Apples (1kg)", "Grocery", 4.99, 
     "Fresh, crisp apples for healthy eating", 
     "https://images.unsplash.com/photo-1560806887-1195db42f038?w=400&h=400&fit=crop", 
     300, 4.8, "Organic,Fresh Picked,Rich in Fiber,Long Shelf Life"),
    
    # Organic Carrots
    ("PROD-GROC-003", "Organic Carrots (500g)", "Grocery", 2.99, 
     "Crunchy organic carrots for cooking", 
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSS5kX_8qkufRzo8BVE2nXq4tBLmRFT7wCBQ&s", 
     400, 4.6, "100% Organic,Fresh Quality,No Chemicals"),
    
    # Fresh Broccoli
    ("PROD-GROC-004", "Fresh Broccoli (1 head)", "Grocery", 3.49, 
     "Green fresh broccoli for healthy meals", 
     "https://images.unsplash.com/photo-1588291212639-dd28a54e6e15?w=400&h=400&fit=crop", 
     350, 4.7, "Nutrient Dense,Fresh Picked,Long Lasting"),
    
    # Fresh Tomatoes
    ("PROD-GROC-005", "Fresh Tomatoes (1kg)", "Grocery", 3.99, 
     "Garden fresh organic tomatoes", 
     "https://media.istockphoto.com/id/831570242/photo/three-juicy-red-tomatoes-isolated-on-white-background.jpg?s=612x612&w=0&k=20&c=bBrjZsWY4eg90OpA2S6cO3psGR1TFx8f4L0HAmIQqm4=", 
     400, 4.8, "100% Organic,Farm Fresh,Rich Red Color,Great Flavor"),
    
    # Fresh Bananas
    ("PROD-GROC-006", "Fresh Bananas (1 bunch)", "Grocery", 2.49, 
     "Yellow ripe fresh bananas", 
     "https://5.imimg.com/data5/SELLER/Default/2022/12/EK/NP/CN/49293026/fresh-banana-fruit.webp", 
     600, 4.9, "Rich in Potassium,Sweet Taste,High Energy,Best Bunch"),
    
    # Fresh Onions
    ("PROD-GROC-007", "Fresh Onions (1kg)", "Grocery", 2.99, 
     "Fresh red onions for daily cooking", 
     "https://m.media-amazon.com/images/I/51DJ-9xkuQL.jpg", 
     500, 4.5, "Fresh Harvest,Strong Flavor,Farm Fresh"),
    
    # Fresh Spinach
    ("PROD-GROC-008", "Fresh Spinach (250g)", "Grocery", 3.29, 
     "Nutritious fresh spinach leaves", 
     "https://m.media-amazon.com/images/I/71tdN2taTCL.jpg", 
     300, 4.7, "High Iron,Antioxidants,Dark Green Color,Perfect for Cooking"),
]

# ==================== FASHION PRODUCTS ====================
fashion_products = [
    # Men's Formal Shirt
    ("PROD-FASH-001", "Men's Formal Shirt", "Fashion", 49.99, 
     "Premium formal shirt for professionals", 
     "https://thefoomer.in/cdn/shop/products/jpeg-optimizer_PATP5156.jpg?v=1680162712", 
     200, 4.7, "100% Cotton,Easy Care,Multiple Sizes,Machine Washable"),
    
    # Women's Dress
    ("PROD-FASH-002", "Women's Dress", "Fashion", 79.99, 
     "Elegant women's dress for any occasion", 
     "https://www.bullionknot.com/cdn/shop/files/Lipika-02.jpg?v=1753954225&width=1200", 
     150, 4.8, "Comfortable Fit,Beautiful Design,Multiple Colors,Hand Washable"),
    
    # Denim Jeans
    ("PROD-FASH-003", "Denim Jeans", "Fashion", 69.99, 
     "Classic denim jeans for everyday wear", 
     "https://cantabilshop.com/cdn/shop/products/MDNM00403_LTHILLIUM_1.jpg?v=1757052556", 
     300, 4.6, "Premium Denim,Comfortable,All Sizes,Deep Blue Color"),
    
    # Casual T-Shirt
    ("PROD-FASH-004", "Casual T-Shirt", "Fashion", 24.99, 
     "Comfortable casual t-shirt for daily wear", 
     "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=400&fit=crop", 
     400, 4.5, "Soft Fabric,Breathable,Multiple Colors"),
    
    # Hoodie Sweatshirt
    ("PROD-FASH-005", "Hoodie Sweatshirt", "Fashion", 54.99, 
     "Warm and cozy hoodie for cold weather", 
     "https://media.istockphoto.com/id/1142211733/photo/front-of-sweatshirt-with-hood-isolated-on-white-background.jpg?s=612x612&w=0&k=20&c=inMPwtP-ebqhXD9_A3bHETPkyC37x0rFNSLYgf6rLMM=", 
     180, 4.8, "Plush Fabric,Drawstring Hood,Kangaroo Pocket,Various Colors"),
    
    # Women's Shoes
    ("PROD-FASH-006", "Women's Shoes", "Fashion", 89.99, 
     "Stylish women's shoes for any occasion", 
     "https://m.media-amazon.com/images/I/71pl8w5xXJL._AC_UY1000_.jpg", 
     120, 4.7, "Premium Quality,Comfortable,Non-Slip Sole,Elegant Design,"),
    
    # Handbag
    ("PROD-FASH-007", "Handbag", "Fashion", 129.99, 
     "Premium handbag with elegant design", 
     "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=400&h=400&fit=crop", 
     80, 4.9, "Genuine Material,Spacious,Strong Handles"),
    
    # Winter Scarf
    ("PROD-FASH-008", "Winter Scarf", "Fashion", 34.99, 
     "Warm and stylish winter scarf", 
     "https://m.media-amazon.com/images/I/61u4jOe1DFL._AC_UF1000,1000_QL80_.jpg", 
     250, 4.4, "Soft Wool,Warm Material,Fashion Forward,All Ages,"),
]

# Combine all products
all_products = electronics_products + books_products + grocery_products + fashion_products

print("=" * 60)
print("ADDING ALL PRODUCTS TO DATABASE")
print("=" * 60)

added_count = 0
existing_count = 0

for product in all_products:
    existing = cursor.execute("SELECT product_id FROM products WHERE product_id = ?", (product[0],)).fetchone()
    if not existing:
        cursor.execute("""
            INSERT INTO products (product_id, name, category, price, description, image_url, stock, rating, features)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, product)
        print(f"✅ Added: {product[1]} ({product[2]})")
        added_count += 1
    else:
        print(f"⚠️ Already exists: {product[1]}")
        existing_count += 1

conn.commit()
conn.close()

print("\n" + "=" * 60)
print(f"SUMMARY:")
print(f"✅ New products added: {added_count}")
print(f"⚠️ Existing products skipped: {existing_count}")
print(f"📊 Total products: {added_count + existing_count}")
print("=" * 60)

# Show summary by category
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

print("\n📊 PRODUCT SUMMARY BY CATEGORY:")
print("-" * 40)

categories = ['Electronics', 'Books', 'Grocery', 'Fashion']
for category in categories:
    count = cursor.execute("SELECT COUNT(*) FROM products WHERE category = ?", (category,)).fetchone()[0]
    print(f"  {category}: {count} products")

conn.close()

print("\n🎉 All products added successfully!")