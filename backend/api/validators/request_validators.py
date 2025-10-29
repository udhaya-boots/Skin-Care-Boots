import re

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_password(password):
    """Validate password strength"""
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    return True, None


def validate_signup(data):
    """Validate signup request data"""
    email = data.get('email')
    password = data.get('password')
    
    if not email:
        return False, "Email is required"
    
    if not validate_email(email):
        return False, "Invalid email format"
    
    if not password:
        return False, "Password is required"
    
    is_valid, error = validate_password(password)
    if not is_valid:
        return False, error
    
    return True, None


def validate_signin(data):
    """Validate signin request data"""
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return False, "Email and password are required"
    
    return True, None


def validate_image_data(image_data):
    """Validate base64 image data"""
    if not image_data:
        return False, "Image data is required"
    
    if not isinstance(image_data, str):
        return False, "Image data must be a base64 string"
    
    return True, None
