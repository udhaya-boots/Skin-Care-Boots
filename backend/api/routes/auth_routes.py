from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from api.validators.request_validators import validate_signup, validate_signin

bp = Blueprint('auth', __name__)
auth_service = AuthService()

@bp.route('/signup', methods=['POST'])
def signup():
    """User registration endpoint"""
    try:
        data = request.get_json()
        
        # Validate request
        is_valid, error = validate_signup(data)
        if not is_valid:
            return jsonify({'error': error}), 400
        
        # Register user
        result = auth_service.register_user(
            email=data.get('email'),
            password=data.get('password'),
            name=data.get('name', '')
        )
        
        if result.get('success'):
            return jsonify(result), 201
        else:
            return jsonify(result), 409
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/signin', methods=['POST'])
def signin():
    """User login endpoint"""
    try:
        data = request.get_json()
        
        # Validate request
        is_valid, error = validate_signin(data)
        if not is_valid:
            return jsonify({'error': error}), 400
        
        # Authenticate user
        result = auth_service.authenticate_user(
            email=data.get('email'),
            password=data.get('password')
        )
        
        if result.get('success'):
            return jsonify(result), 200
        else:
            return jsonify(result), 401
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/google', methods=['POST'])
def google_signin():
    """Google OAuth signin endpoint"""
    try:
        data = request.get_json()
        
        if not data.get('email'):
            return jsonify({'error': 'Email required'}), 400
        
        result = auth_service.google_signin(
            email=data.get('email'),
            name=data.get('name', '')
        )
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/verify', methods=['GET'])
def verify_token():
    """Verify JWT token"""
    try:
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        
        if not token:
            return jsonify({'error': 'Token required'}), 401
        
        user_id = auth_service.verify_token(token)
        
        if user_id:
            return jsonify({'success': True, 'user_id': user_id}), 200
        else:
            return jsonify({'error': 'Invalid token'}), 401
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500
