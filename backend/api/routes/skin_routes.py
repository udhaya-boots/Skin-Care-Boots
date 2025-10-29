from flask import Blueprint, request, jsonify
from services.skin_analyzer import SkinAnalyzerService
from services.product_recommender import ProductRecommenderService
from services.auth_service import AuthService
from models.analysis_model import AnalysisModel

bp = Blueprint('skin', __name__)
skin_analyzer = SkinAnalyzerService()
recommender = ProductRecommenderService()
auth_service = AuthService()
analysis_model = AnalysisModel()

@bp.route('/analyze', methods=['POST'])
def analyze_skin():
    """Analyze skin from uploaded image"""
    try:
        data = request.get_json()
        image_data = data.get('image')
        
        if not image_data:
            return jsonify({'error': 'No image provided'}), 400
        
        # Get user_id from token if provided
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        user_id = auth_service.verify_token(token) if token else None
        
        # Perform analysis
        analysis_result = skin_analyzer.analyze(image_data)
        
        if not analysis_result.get('success'):
            return jsonify(analysis_result), 400
        
        # Get product recommendations
        products = recommender.get_recommendations(
            concerns=analysis_result['data']['concerns'],
            skin_type=analysis_result['data']['skin_type']
        )
        
        # Save analysis if user is authenticated
        if user_id:
            analysis_model.save_analysis(user_id, analysis_result['data'])
        
        return jsonify({
            'success': True,
            'analysis': analysis_result['data'],
            'products': products[:5]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/history', methods=['GET'])
def get_history():
    """Get user's skin analysis history"""
    try:
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        user_id = auth_service.verify_token(token)
        
        if not user_id:
            return jsonify({'error': 'Unauthorized'}), 401
        
        history = analysis_model.get_user_history(user_id)
        
        return jsonify({
            'success': True,
            'history': history
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/tips', methods=['GET'])
def get_tips():
    """Get skin care tips"""
    try:
        from utils.database import get_db_connection
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tips ORDER BY created_at DESC LIMIT 10')
        tips = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        return jsonify({
            'success': True,
            'tips': tips
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
