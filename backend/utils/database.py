import sqlite3
import os
from contextlib import contextmanager
from config import Config

DATABASE_PATH = Config.DATABASE_PATH

def init_database():
    """Initialize the database with required tables"""
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        
        # Create products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                brand TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT,
                ingredients TEXT,
                skin_types TEXT,
                rating REAL DEFAULT 4.0,
                image_url TEXT,
                url TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create skin_analysis table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS skin_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                skin_type TEXT,
                overall_score REAL,
                oily_score REAL,
                dry_score REAL,
                acne_score REAL,
                wrinkle_score REAL,
                dark_spot_score REAL,
                sensitivity_score REAL,
                pore_score REAL,
                recommendations TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        print("Database initialized successfully")

@contextmanager
def get_db_connection():
    """Get database connection context manager"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Enable dict-like access
    try:
        yield conn
    finally:
        conn.close()
