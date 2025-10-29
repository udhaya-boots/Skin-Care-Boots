import cv2
import numpy as np
from services.image_processor import ImageProcessorService

class SkinAnalyzerService:
    def __init__(self):
        self.image_processor = ImageProcessorService()
    
    def analyze(self, image_data):
        """Perform comprehensive skin analysis"""
        try:
            # Process image
            image = self.image_processor.decode_base64_image(image_data)
            enhanced_image = self.image_processor.preprocess_image(image)
            
            # Detect face region
            face_region, landmarks = self.image_processor.detect_face_region(enhanced_image)
            
            if face_region is None:
                return {'success': False, 'error': 'No face detected in image'}
            
            # Perform analyses
            pore_analysis = self._analyze_pores(face_region)
            acne_analysis = self._analyze_acne(face_region)
            texture_analysis = self._analyze_texture(face_region)
            skin_type = self._analyze_skin_type(face_region)
            
            # Calculate overall score
            overall_score = 100 - (
                pore_analysis['score'] * 0.3 +
                acne_analysis['score'] * 0.4 +
                texture_analysis['score'] * 0.3
            )
            
            # Determine concerns
            concerns = []
            if pore_analysis['score'] > 30:
                concerns.append('pore')
            if acne_analysis['score'] > 20:
                concerns.append('acne')
            if texture_analysis['score'] > 35:
                concerns.append('texture')
            
            return {
                'success': True,
                'data': {
                    'overall_score': round(max(0, overall_score), 2),
                    'pore_analysis': pore_analysis,
                    'acne_analysis': acne_analysis,
                    'texture_analysis': texture_analysis,
                    'skin_type': skin_type,
                    'concerns': concerns,
                    'recommendation': self._generate_recommendation(overall_score, concerns)
                }
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _analyze_pores(self, image):
        """Analyze pore visibility using texture analysis"""
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        
        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        
        # Detect edges (pores appear as small dark spots)
        edges = cv2.Canny(blurred, 30, 100)
        
        # Count edge pixels as pore indicators
        pore_density = np.sum(edges > 0) / edges.size
        
        # Normalize to 0-100 scale
        pore_score = min(100, pore_density * 500)
        
        return {
            'score': round(pore_score, 2),
            'severity': self._get_severity(pore_score),
            'description': f'Pore visibility detected at {pore_score:.1f}%'
        }
    
    def _analyze_acne(self, image):
        """Detect acne and blemishes using color and texture analysis"""
        # Convert to HSV for better color detection
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        
        # Define range for redness (acne indicator)
        lower_red1 = np.array([0, 50, 50])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 50, 50])
        upper_red2 = np.array([180, 255, 255])
        
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        red_mask = mask1 + mask2
        
        # Find contours (potential acne spots)
        contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Filter contours by size
        acne_spots = [c for c in contours if 10 < cv2.contourArea(c) < 500]
        
        acne_count = len(acne_spots)
        acne_score = min(100, acne_count * 3)
        
        return {
            'score': round(acne_score, 2),
            'count': acne_count,
            'severity': self._get_severity(acne_score),
            'description': f'{acne_count} potential acne spots detected'
        }
    
    def _analyze_texture(self, image):
        """Analyze skin texture smoothness"""
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        
        # Calculate standard deviation of Laplacian (texture roughness)
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        texture_variance = laplacian.var()
        
        # Normalize to 0-100 scale
        texture_score = min(100, texture_variance / 10)
        
        return {
            'score': round(texture_score, 2),
            'severity': self._get_severity(texture_score),
            'description': f'Texture roughness at {texture_score:.1f}%'
        }
    
    def _analyze_skin_type(self, image):
        """Determine skin type based on color and texture"""
        # Analyze brightness
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        brightness = np.mean(gray)
        
        # Analyze color distribution
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        saturation = np.mean(hsv[:, :, 1])
        
        if saturation > 100:
            skin_type = "oily"
        elif saturation < 50:
            skin_type = "dry"
        else:
            skin_type = "normal"
        
        return skin_type
    
    def _get_severity(self, score):
        """Convert score to severity level"""
        if score < 20:
            return 'minimal'
        elif score < 40:
            return 'mild'
        elif score < 60:
            return 'moderate'
        else:
            return 'severe'
    
    def _generate_recommendation(self, score, concerns):
        """Generate personalized recommendation"""
        if score > 80:
            return "Luar biasa! Kulit Anda dalam kondisi sangat baik."
        elif score > 60:
            return "Kulit Anda cukup baik, pertahankan dengan perawatan rutin."
        elif score > 40:
            return "Hasil menunjukkan kulit anda membutuhkan perawatan perbaikan kulit"
        else:
            return "Kulit memerlukan perhatian khusus. Konsultasi dengan ahli kulit disarankan."
