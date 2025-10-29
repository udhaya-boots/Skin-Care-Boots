from models.product_model import ProductModel

class ProductRecommenderService:
    def __init__(self):
        self.product_model = ProductModel()
        self.concern_priority = {
            'acne': 3,
            'pore': 2,
            'texture': 2,
            'dry': 1,
            'oily': 1
        }
    
    def get_recommendations(self, concerns, skin_type, limit=10):
        """Get product recommendations based on skin analysis"""
        if not concerns:
            concerns = [skin_type]
        
        # Get products matching concerns
        products = self.product_model.get_by_concerns(concerns, skin_type, limit)
        
        return products
    
    def get_top_products(self, limit=3):
        """Get top recommended products"""
        return self.product_model.get_top_products(limit)
