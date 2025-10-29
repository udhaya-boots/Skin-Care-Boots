from utils.database import get_db_connection

class AnalysisModel:
    def __init__(self):
        pass
    
    def save_analysis(self, user_id, analysis_data):
        """Save analysis to database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO skin_analysis 
            (user_id, pore_score, acne_score, texture_score, overall_score, skin_type, concerns)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            user_id,
            analysis_data['pore_analysis']['score'],
            analysis_data['acne_analysis']['score'],
            analysis_data['texture_analysis']['score'],
            analysis_data['overall_score'],
            analysis_data['skin_type'],
            ','.join(analysis_data['concerns'])
        ))
        
        conn.commit()
        analysis_id = cursor.lastrowid
        conn.close()
        return analysis_id
    
    def get_user_history(self, user_id, limit=10):
        """Get user's analysis history"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM skin_analysis
            WHERE user_id = ?
            ORDER BY analyzed_at DESC
            LIMIT ?
        ''', (user_id, limit))
        
        history = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return history
