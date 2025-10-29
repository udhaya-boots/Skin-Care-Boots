from datetime import datetime

def format_datetime(dt):
    """Format datetime to string"""
    if isinstance(dt, str):
        dt = datetime.fromisoformat(dt)
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def calculate_age(birthdate):
    """Calculate age from birthdate"""
    today = datetime.today()
    if isinstance(birthdate, str):
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
