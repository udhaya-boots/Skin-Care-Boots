import bcrypt
import jwt
from datetime import datetime, timedelta
from config import Config
from models.user_model import UserModel

class AuthService:
    def __init__(self):
        self.user_model = UserModel()
    
    def register_user(self, email, password, name=''):
        """Register new user"""
        try:
            # Check if user exists
            existing_user = self.user_model.get_by_email(email)
            if existing_user:
                return {'success': False, 'error': 'Email already exists'}
            
            # Hash password
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            # Create user
            user_id = self.user_model.create(email, password_hash, name)
            
            # Generate token
            token = self._generate_token(user_id, email)
            
            return {
                'success': True,
                'token': token,
                'user': {'id': user_id, 'email': email, 'name': name}
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def authenticate_user(self, email, password):
        """Authenticate user"""
        try:
            user = self.user_model.get_by_email(email)
            
            if not user:
                return {'success': False, 'error': 'Invalid credentials'}
            
            # Verify password
            if not bcrypt.checkpw(password.encode('utf-8'), user['password']):
                return {'success': False, 'error': 'Invalid credentials'}
            
            # Generate token
            token = self._generate_token(user['id'], user['email'])
            
            return {
                'success': True,
                'token': token,
                'user': {'id': user['id'], 'email': user['email'], 'name': user['name']}
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def google_signin(self, email, name=''):
        """Google OAuth signin"""
        try:
            user = self.user_model.get_by_email(email)
            
            if not user:
                # Create new user
                user_id = self.user_model.create(email, '', name)
            else:
                user_id = user['id']
            
            # Generate token
            token = self._generate_token(user_id, email)
            
            return {
                'success': True,
                'token': token,
                'user': {'id': user_id, 'email': email, 'name': name}
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def verify_token(self, token):
        """Verify JWT token"""
        try:
            payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=['HS256'])
            return payload['user_id']
        except:
            return None
    
    def _generate_token(self, user_id, email):
        """Generate JWT token"""
        payload = {
            'user_id': user_id,
            'email': email,
            'exp': datetime.utcnow() + Config.JWT_ACCESS_TOKEN_EXPIRES
        }
        return jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm='HS256')
