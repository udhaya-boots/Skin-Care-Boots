import cv2
import numpy as np
from PIL import Image
import base64
import io
import mediapipe as mp

class ImageProcessorService:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            min_detection_confidence=0.5
        )
    
    def decode_base64_image(self, base64_string):
        """Decode base64 image string to numpy array"""
        try:
            if ',' in base64_string:
                base64_string = base64_string.split(',')[1]
            
            image_bytes = base64.b64decode(base64_string)
            image = Image.open(io.BytesIO(image_bytes))
            return np.array(image)
        except Exception as e:
            raise ValueError(f"Failed to decode image: {str(e)}")
    
    def preprocess_image(self, image):
        """Enhance image quality for analysis"""
        # Convert to RGB if needed
        if len(image.shape) == 2:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        elif image.shape[2] == 4:
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        
        # Resize to standard size
        image = cv2.resize(image, (640, 480))
        
        # Enhance contrast
        lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        l = clahe.apply(l)
        enhanced = cv2.merge([l, a, b])
        enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2RGB)
        
        return enhanced
    
    def detect_face_region(self, image):
        """Detect face and extract region of interest"""
        results = self.face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        if not results.multi_face_landmarks:
            return None, None
        
        landmarks = results.multi_face_landmarks[0]
        h, w = image.shape[:2]
        
        # Extract face bounding box
        x_coords = [landmark.x * w for landmark in landmarks.landmark]
        y_coords = [landmark.y * h for landmark in landmarks.landmark]
        
        x_min, x_max = int(min(x_coords)), int(max(x_coords))
        y_min, y_max = int(min(y_coords)), int(max(y_coords))
        
        face_region = image[y_min:y_max, x_min:x_max]
        
        return face_region, landmarks
