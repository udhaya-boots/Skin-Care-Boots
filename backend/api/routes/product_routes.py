from flask import Blueprint, request, jsonify
from models.product_model import ProductModel

bp = Blueprint('products', __name__)
product_model = ProductModel()

@bp.route('/all', methods=['GET'])
def get_all_products():
    """Get all products"""
    try:
        products = product_model.get_all()
        return jsonify({
            'success': True,
            'products': products
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/top', methods=['GET'])
def get_top_products():
    """Get top products"""
    try:
        limit = request.args.get('limit', 3, type=int)
        products = product_model.get_top_products(limit)
        return jsonify({
            'success': True,
            'products': products
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get single product details"""
    try:
        product = product_model.get_by_id(product_id)
        
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        
        return jsonify({
            'success': True,
            'product': product
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/recommend', methods=['POST'])
def recommend_products():
    """Get product recommendations based on concerns"""
    try:
        data = request.get_json()
        concerns = data.get('concerns', [])
        skin_type = data.get('skin_type', 'normal')
        limit = data.get('limit', 10)
        
        products = product_model.get_by_concerns(concerns, skin_type, limit)
        
        return jsonify({
            'success': True,
            'products': products
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/search', methods=['GET'])
def search_products():
    """Search products by name or category"""
    try:
        query = request.args.get('q', '')
        category = request.args.get('category', '')
        
        products = product_model.search(query, category)
        
        return jsonify({
            'success': True,
            'products': products
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
