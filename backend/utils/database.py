import sqlite3
from config import Config
import os

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(Config.DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Initialize database with schema and sample data"""
    os.makedirs(os.path.dirname(Config.DATABASE_PATH), exist_ok=True)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            brand TEXT NOT NULL,
            description TEXT,
            image_url TEXT,
            category TEXT,
            skin_concerns TEXT,
            price REAL,
            rating REAL DEFAULT 0,
            is_top_product BOOLEAN DEFAULT 0
        )
    ''')
    
    # Skin analysis history
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS skin_analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            image_path TEXT,
            pore_score REAL,
            acne_score REAL,
            texture_score REAL,
            overall_score REAL,
            skin_type TEXT,
            concerns TEXT,
            analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Tips table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            tip_type TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert sample products
    sample_products = [
        ('Serum by scarlet', 'Scarlet', 'Contains natural ingredients good for oily skin', 
         '/images/serum1.png', 'serum', 'pore,acne', 299000, 4.5, 1),
        ('Hydrating Facial Toner', 'SkinLab', 'Contains natural ingredients good for dry skin',
         '/images/toner1.png', 'toner', 'dry,texture', 199000, 4.3, 1),
        ('Acne Clear Solution', 'DermaCare', 'Special formula to treat acne and acne scars',
         '/images/acne1.png', 'treatment', 'acne,inflammation', 349000, 4.7, 1),
        ('Pore Minimizer Essence', 'PureGlow', 'Reduces the appearance of pores and controls oil',
         '/images/essence1.png', 'essence', 'pore,oily', 279000, 4.4, 0),
        ('Gentle Face Cleanser', 'SkinLab', 'Gentle facial cleanser for all skin types',
         '/images/cleanser1.png', 'cleanser', 'normal,dry', 159000, 4.6, 1),
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO products (name, brand, description, image_url, category, skin_concerns, price, rating, is_top_product)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', sample_products)
    
    # Insert sample tips
    sample_tips = [
        ('How to choose a good toner', 'Contains natural ingredients good for oily skin', 'good'),
        ('How to choose a good serum', 'Contains natural ingredients good for oily skin', 'good'),
        ('Importance of sunscreen', 'Use sunscreen daily to protect skin from UV rays', 'good'),
        ('Correct skincare routine', 'Cleansing, toner, serum, moisturizer, sunscreen', 'good'),
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO tips (title, description, tip_type)
        VALUES (?, ?, ?)
    ''', sample_tips)
    
    conn.commit()
    conn.close()
    print("✓ Database initialized successfully")
