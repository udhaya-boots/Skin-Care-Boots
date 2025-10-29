from utils.database import get_db_connection

class ProductModel:
    def __init__(self):
        pass
    
    def get_all(self):
        """Get all products"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products ORDER BY rating DESC')
        products = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return products
    
    def get_top_products(self, limit=3):
        """Get top products"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM products WHERE is_top_product = 1 ORDER BY rating DESC LIMIT ?',
            (limit,)
        )
        products = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return products
    
    def get_by_id(self, product_id):
        """Get product by ID"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
        product = cursor.fetchone()
        conn.close()
        return dict(product) if product else None
    
    def get_by_concerns(self, concerns, skin_type, limit=10):
        """Get products by concerns"""
        if not concerns:
            concerns = [skin_type]
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        concern_conditions = [f"skin_concerns LIKE '%{concern}%'" for concern in concerns]
        query = f'''
            SELECT * FROM products
            WHERE ({' OR '.join(concern_conditions)})
            ORDER BY is_top_product DESC, rating DESC
            LIMIT ?
        '''
        
        cursor.execute(query, (limit,))
        products = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return products
