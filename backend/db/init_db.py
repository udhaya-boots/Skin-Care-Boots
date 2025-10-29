# Sample data for products
sample_products = [
    {
        'name': 'Product 1',
        'brand': 'Brand A',
        'category': 'category_1',
        'price': 19.99,
        'description': 'Description for product 1',
        'ingredients': ['Ingredient 1', 'Ingredient 2'],
        'skin_types': ['normal', 'dry'],
        'rating': 4.5,
        'image_url': '/images/product1.jpg',
        'url': 'https://www.example.com/product1'
    },
    {
        'name': 'Product 2',
        'brand': 'Brand B',
        'category': 'category_2',
        'price': 29.99,
        'description': 'Description for product 2',
        'ingredients': ['Ingredient 3', 'Ingredient 4'],
        'skin_types': ['oily', 'combination'],
        'rating': 4.0,
        'image_url': '/images/product2.jpg',
        'url': 'https://www.example.com/product2'
    }
]

# Boots products from CSV
boots_products = [
    {
        'name': 'No7 The Ultimate Skincare Collection Gift Set',
        'brand': 'No7',
        'category': 'skincare_set',
        'price': 39.00,
        'description': 'Star Gift - Only £39 using code ULTIMATESAVE on No7 The Ultimate Skincare Collection Gift Set - online only',
        'ingredients': ['Hyaluronic Acid', 'Peptides', 'Antioxidants'],
        'skin_types': ['normal', 'dry', 'mature'],
        'rating': 4.5,
        'image_url': '/images/no7_ultimate_set.jpg',
        'url': 'https://www.boots.com/no7-the-ultimate-skincare-collection-gift-set-10364646'
    },
    {
        'name': 'The Ordinary Niacinamide 10% + Zinc 1% Oil Control Serum',
        'brand': 'The Ordinary',
        'category': 'serum',
        'price': 6.90,
        'description': 'Oil control serum with niacinamide and zinc for blemish-prone skin',
        'ingredients': ['Niacinamide', 'Zinc', 'Hyaluronic Acid'],
        'skin_types': ['oily', 'combination', 'acne'],
        'rating': 4.6,
        'image_url': '/images/ordinary_niacinamide.jpg',
        'url': 'https://www.boots.com/the-ordinary-niacinamide-10-zinc-1-10267783'
    },
    {
        'name': 'The Ordinary Glycolic Acid 7% Exfoliating Toner',
        'brand': 'The Ordinary',
        'category': 'toner',
        'price': 8.90,
        'description': 'Exfoliating toner with glycolic acid for improved skin texture',
        'ingredients': ['Glycolic Acid', 'Aloe Vera', 'Ginseng'],
        'skin_types': ['normal', 'combination', 'dull'],
        'rating': 4.4,
        'image_url': '/images/ordinary_glycolic.jpg',
        'url': 'https://www.boots.com/the-ordinary-glycolic-acid-7-exfoliating-solution-100ml-10335078'
    },
    {
        'name': 'CeraVe Get Your Glow On Gift Set',
        'brand': 'CeraVe',
        'category': 'skincare_set',
        'price': 29.50,
        'description': 'Worth £59, only £29.50 - Complete skincare routine for healthy glow',
        'ingredients': ['Ceramides', 'Hyaluronic Acid', 'Vitamin B3'],
        'skin_types': ['dry', 'normal', 'sensitive'],
        'rating': 4.7,
        'image_url': '/images/cerave_glow_set.jpg',
        'url': 'https://www.boots.com/cerave-get-your-glow-on-gift-set-10374474'
    },
    {
        'name': 'Boots Ingredients Hyaluronic Acid Moisturiser',
        'brand': 'Boots',
        'category': 'moisturizer',
        'price': 3.60,
        'description': 'Hydrating moisturizer with hyaluronic acid for all skin types',
        'ingredients': ['Hyaluronic Acid', 'Glycerin', 'Vitamin E'],
        'skin_types': ['dry', 'normal', 'sensitive'],
        'rating': 4.2,
        'image_url': '/images/boots_hyaluronic.jpg',
        'url': 'https://www.boots.com/boots-ingredients-hyaluronic-acid-moisturiser-30ml-10276161'
    },
    {
        'name': 'Super Facialist Vitamin C+ Brighten Gentle Daily Micro Polish Wash',
        'brand': 'Super Facialist',
        'category': 'cleanser',
        'price': 6.67,
        'description': 'Gentle daily cleanser with vitamin C for brighter skin',
        'ingredients': ['Vitamin C', 'Micro Beads', 'Citrus Extract'],
        'skin_types': ['normal', 'dull', 'combination'],
        'rating': 4.3,
        'image_url': '/images/superfacialist_vitc.jpg',
        'url': 'https://www.boots.com/superfacialist-vitamin-c-gentle-daily-micro-polish-wash-125ml-10160292'
    },
    {
        'name': 'DIOR Capture Anti-Aging Gift Set',
        'brand': 'DIOR',
        'category': 'skincare_set',
        'price': 109.00,
        'description': 'Limited edition anti-aging skincare collection',
        'ingredients': ['Retinol', 'Peptides', 'Antioxidants'],
        'skin_types': ['normal', 'dry', 'mature'],
        'rating': 4.8,
        'image_url': '/images/dior_capture.jpg',
        'url': 'https://www.boots.com/dior-capture-anti-aging-gift-set-limited-edition--10368981'
    },
    {
        'name': 'Clinique Beauty Icons Star Gift',
        'brand': 'Clinique',
        'category': 'skincare_set',
        'price': 44.50,
        'description': 'Star Gift - Better than 1/2 price, Worth £121, Only £44.50',
        'ingredients': ['Salicylic Acid', 'Hyaluronic Acid', 'Ceramides'],
        'skin_types': ['oily', 'combination', 'normal'],
        'rating': 4.5,
        'image_url': '/images/clinique_icons.jpg',
        'url': 'https://www.boots.com/clinique-beauty-icons-star-gift-10369863'
    }
]

# Add boots products to sample products
all_products = sample_products + boots_products

# ...existing code...

for product_data in all_products:
    # Code to add each product to the database
    pass