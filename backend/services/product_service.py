from db.database import get_db
from models.product import Product

class ProductService:
    def __init__(self):
        pass
    
    def get_products_by_skin_type(self, skin_type):
        """Get products suitable for a specific skin type"""
        db = next(get_db())
        try:
            products = db.query(Product).all()
            matching_products = []
            
            for product in products:
                # Convert skin_types string to list if needed
                if isinstance(product.skin_types, str):
                    skin_types_list = product.skin_types.split(',')
                else:
                    skin_types_list = product.skin_types or []
                
                # Check if the product is suitable for the skin type
                if skin_type in skin_types_list or 'normal' in skin_types_list:
                    matching_products.append({
                        'id': product.id,
                        'name': product.name,
                        'brand': product.brand,
                        'category': product.category,
                        'price': product.price,
                        'description': product.description,
                        'ingredients': product.ingredients.split(',') if product.ingredients else [],
                        'skin_types': skin_types_list,
                        'rating': product.rating,
                        'image_url': product.image_url,
                        'url': getattr(product, 'url', None)
                    })
            
            return matching_products
        finally:
            db.close()
    
    def get_all_products(self):
        """Get all products"""
        db = next(get_db())
        try:
            products = db.query(Product).all()
            return [{
                'id': product.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'price': product.price,
                'description': product.description,
                'ingredients': product.ingredients.split(',') if product.ingredients else [],
                'skin_types': product.skin_types.split(',') if product.skin_types else [],
                'rating': product.rating,
                'image_url': product.image_url,
                'url': getattr(product, 'url', None)
            } for product in products]
        finally:
            db.close()
    
    def get_top_rated_products(self, limit=10):
        """Get top rated products"""
        db = next(get_db())
        try:
            products = db.query(Product).order_by(Product.rating.desc()).limit(limit).all()
            return [{
                'id': product.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'price': product.price,
                'description': product.description,
                'ingredients': product.ingredients.split(',') if product.ingredients else [],
                'skin_types': product.skin_types.split(',') if product.skin_types else [],
                'rating': product.rating,
                'image_url': product.image_url,
                'url': getattr(product, 'url', None)
            } for product in products]
        finally:
            db.close()