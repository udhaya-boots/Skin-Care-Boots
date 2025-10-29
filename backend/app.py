from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import random

def create_app():
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Create necessary directories
    upload_folder = os.path.join(os.path.dirname(__file__), 'uploads')
    os.makedirs(upload_folder, exist_ok=True)
    
    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health_check():
        return jsonify({
            'status': 'healthy',
            'message': 'Skin Care Analyzer API is running',
            'version': '1.0.0'
        })
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Endpoint not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': 'Bad request'}), 400
    
    # Authentication endpoints
    @app.route('/api/auth/signup', methods=['POST'])
    def signup():
        try:
            data = request.json
            email = data.get('email')
            password = data.get('password')
            name = data.get('name', '')
            
            if not email or not password:
                return jsonify({'error': 'Email and password are required'}), 400
            
            # Simple user storage (in production, use a proper database)
            # For now, we'll just return success
            return jsonify({
                'success': True,
                'message': 'User registered successfully',
                'user': {
                    'email': email,
                    'name': name
                }
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @app.route('/api/auth/signin', methods=['POST'])
    def signin():
        try:
            data = request.json
            email = data.get('email')
            password = data.get('password')
            
            if not email or not password:
                return jsonify({'error': 'Email and password are required'}), 400
            
            # Simple authentication (in production, verify against database)
            # For now, we'll accept any non-empty credentials
            if email and password:
                return jsonify({
                    'success': True,
                    'message': 'Login successful',
                    'user': {
                        'email': email,
                        'name': email.split('@')[0]  # Use email prefix as name
                    },
                    'token': 'mock_jwt_token_' + email  # Mock JWT token
                })
            else:
                return jsonify({'error': 'Invalid credentials'}), 401
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    # Add product recommendations endpoint
    @app.route('/api/product-recommendations', methods=['POST'])
    def get_product_recommendations():
        try:
            data = request.json
            scores = data.get('scores', {})
            
            # Generate recommendations based on skin analysis scores
            if scores.get('oily_score', 0) > 0.6 or scores.get('acne_score', 0) > 0.5:
                recommendations = [
                    {
                        'name': 'The Ordinary Niacinamide 10% + Zinc 1%',
                        'brand': 'The Ordinary',
                        'price': '£6.90',
                        'description': 'Oil control serum for blemish-prone skin',
                        'reason': 'Perfect for controlling oily skin and reducing blemishes',
                        'url': 'https://www.boots.com/the-ordinary-niacinamide-10-zinc-1-10267783',
                        'rating': 4.6
                    },
                    {
                        'name': 'Clinique Beauty Icons Star Gift',
                        'brand': 'Clinique',
                        'price': '£44.50',
                        'description': 'Complete skincare routine for oily skin',
                        'reason': 'Comprehensive solution for oily/combination skin',
                        'url': 'https://www.boots.com/clinique-beauty-icons-star-gift-10369863',
                        'rating': 4.5
                    }
                ]
            elif scores.get('dry_score', 0) > 0.6:
                recommendations = [
                    {
                        'name': 'CeraVe Get Your Glow On Gift Set',
                        'brand': 'CeraVe',
                        'price': '£29.50',
                        'description': 'Complete skincare routine for healthy glow',
                        'reason': 'Provides deep hydration for dry skin',
                        'url': 'https://www.boots.com/cerave-get-your-glow-on-gift-set-10374474',
                        'rating': 4.7
                    },
                    {
                        'name': 'Boots Ingredients Hyaluronic Acid Moisturiser',
                        'brand': 'Boots',
                        'price': '£3.60',
                        'description': 'Hydrating moisturizer for all skin types',
                        'reason': 'Affordable daily hydration solution',
                        'url': 'https://www.boots.com/boots-ingredients-hyaluronic-acid-moisturiser-30ml-10276161',
                        'rating': 4.2
                    }
                ]
            elif scores.get('wrinkle_score', 0) > 0.5:
                recommendations = [
                    {
                        'name': 'DIOR Capture Anti-Aging Gift Set',
                        'brand': 'DIOR',
                        'price': '£109.00',
                        'description': 'Limited edition anti-aging skincare collection',
                        'reason': 'Premium anti-aging formula for mature skin',
                        'url': 'https://www.boots.com/dior-capture-anti-aging-gift-set-limited-edition--10368981',
                        'rating': 4.8
                    },
                    {
                        'name': 'No7 The Ultimate Skincare Collection Gift Set',
                        'brand': 'No7',
                        'price': '£39.00',
                        'description': 'Complete anti-aging skincare routine',
                        'reason': 'Proven anti-aging ingredients at great value',
                        'url': 'https://www.boots.com/no7-the-ultimate-skincare-collection-gift-set-10364646',
                        'rating': 4.5
                    }
                ]
            else:
                recommendations = [
                    {
                        'name': 'The Ordinary Glycolic Acid 7% Exfoliating Toner',
                        'brand': 'The Ordinary',
                        'price': '£8.90',
                        'description': 'Exfoliating toner for improved skin texture',
                        'reason': 'Great for maintaining healthy skin texture',
                        'url': 'https://www.boots.com/the-ordinary-glycolic-acid-7-exfoliating-solution-100ml-10335078',
                        'rating': 4.4
                    },
                    {
                        'name': 'Super Facialist Vitamin C+ Brighten Gentle Daily Micro Polish Wash',
                        'brand': 'Super Facialist',
                        'price': '£6.67',
                        'description': 'Gentle daily cleanser with vitamin C',
                        'reason': 'Perfect for daily skincare routine',
                        'url': 'https://www.boots.com/superfacialist-vitamin-c-gentle-daily-micro-polish-wash-125ml-10160292',
                        'rating': 4.3
                    }
                ]
            
            return jsonify({
                'success': True,
                'recommendations': recommendations[:2]  # Return top 2
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500

    # Update analyze endpoint to include product recommendations
    @app.route('/api/analyze', methods=['POST'])
    def analyze_skin():
        try:
            if 'image' not in request.files:
                return jsonify({'error': 'No image uploaded'}), 400
            
            file = request.files['image']
            if file.filename == '':
                return jsonify({'error': 'No image selected'}), 400
            
            # Mock skin analysis (replace with actual analysis logic)
            result = {
                'skin_type': random.choice(['oily', 'dry', 'normal', 'combination']),
                'overall_score': random.randint(60, 95),
                'scores': {
                    'oily_score': random.uniform(0.1, 0.9),
                    'dry_score': random.uniform(0.1, 0.9),
                    'acne_score': random.uniform(0.1, 0.8),
                    'wrinkle_score': random.uniform(0.1, 0.7),
                    'dark_spot_score': random.uniform(0.1, 0.6),
                    'sensitivity_score': random.uniform(0.1, 0.5)
                },
                'recommendations': [
                    'Use gentle cleanser twice daily',
                    'Apply moisturizer after cleansing',
                    'Use sunscreen during the day'
                ]
            }
            
            # Add product recommendations to the result
            scores = result.get('scores', {})
            
            if scores.get('oily_score', 0) > 0.6 or scores.get('acne_score', 0) > 0.5:
                recommendations = [
                    {
                        'name': 'The Ordinary Niacinamide 10% + Zinc 1%',
                        'brand': 'The Ordinary',
                        'price': '£6.90',
                        'description': 'Oil control serum for blemish-prone skin',
                        'reason': 'Perfect for controlling oily skin and reducing blemishes',
                        'url': 'https://www.boots.com/the-ordinary-niacinamide-10-zinc-1-10267783',
                        'rating': 4.6
                    },
                    {
                        'name': 'Clinique Beauty Icons Star Gift',
                        'brand': 'Clinique',
                        'price': '£44.50',
                        'description': 'Complete skincare routine for oily skin',
                        'reason': 'Comprehensive solution for oily/combination skin',
                        'url': 'https://www.boots.com/clinique-beauty-icons-star-gift-10369863',
                        'rating': 4.5
                    }
                ]
            elif scores.get('dry_score', 0) > 0.6:
                recommendations = [
                    {
                        'name': 'CeraVe Get Your Glow On Gift Set',
                        'brand': 'CeraVe',
                        'price': '£29.50',
                        'description': 'Complete skincare routine for healthy glow',
                        'reason': 'Provides deep hydration for dry skin',
                        'url': 'https://www.boots.com/cerave-get-your-glow-on-gift-set-10374474',
                        'rating': 4.7
                    },
                    {
                        'name': 'Boots Ingredients Hyaluronic Acid Moisturiser',
                        'brand': 'Boots',
                        'price': '£3.60',
                        'description': 'Hydrating moisturizer for all skin types',
                        'reason': 'Affordable daily hydration solution',
                        'url': 'https://www.boots.com/boots-ingredients-hyaluronic-acid-moisturiser-30ml-10276161',
                        'rating': 4.2
                    }
                ]
            elif scores.get('wrinkle_score', 0) > 0.5:
                recommendations = [
                    {
                        'name': 'DIOR Capture Anti-Aging Gift Set',
                        'brand': 'DIOR',
                        'price': '£109.00',
                        'description': 'Limited edition anti-aging skincare collection',
                        'reason': 'Premium anti-aging formula for mature skin',
                        'url': 'https://www.boots.com/dior-capture-anti-aging-gift-set-limited-edition--10368981',
                        'rating': 4.8
                    },
                    {
                        'name': 'No7 The Ultimate Skincare Collection Gift Set',
                        'brand': 'No7',
                        'price': '£39.00',
                        'description': 'Complete anti-aging skincare routine',
                        'reason': 'Proven anti-aging ingredients at great value',
                        'url': 'https://www.boots.com/no7-the-ultimate-skincare-collection-gift-set-10364646',
                        'rating': 4.5
                    }
                ]
            else:
                recommendations = [
                    {
                        'name': 'The Ordinary Glycolic Acid 7% Exfoliating Toner',
                        'brand': 'The Ordinary',
                        'price': '£8.90',
                        'description': 'Exfoliating toner for improved skin texture',
                        'reason': 'Great for maintaining healthy skin texture',
                        'url': 'https://www.boots.com/the-ordinary-glycolic-acid-7-exfoliating-solution-100ml-10335078',
                        'rating': 4.4
                    },
                    {
                        'name': 'Super Facialist Vitamin C+ Brighten Gentle Daily Micro Polish Wash',
                        'brand': 'Super Facialist',
                        'price': '£6.67',
                        'description': 'Gentle daily cleanser with vitamin C',
                        'reason': 'Perfect for daily skincare routine',
                        'url': 'https://www.boots.com/superfacialist-vitamin-c-gentle-daily-micro-polish-wash-125ml-10160292',
                        'rating': 4.3
                    }
                ]
            
            result['product_recommendations'] = recommendations[:2]
            
            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)