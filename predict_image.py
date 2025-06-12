import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('models/sign_language_model.h5')

# Path to your test image
image_path = '/Users/geethakumuduni/Desktop/sign_language_project/Test/B/3001.jpg'  # 👈 replace with real image path

# Load and preprocess the image
img = cv2.imread(image_path)

# Check if image loaded
if img is None:
    print(f"❌ Could not load image: {image_path}")
    exit()

# Resize and normalize image
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB (not BGR)
img = cv2.resize(img, (64, 64))             # Resize to 64x64 (same as training)
img = img / 255.0                           # Normalize
img = np.expand_dims(img, axis=0)          # Add batch dimension

# Predict
prediction = model.predict(img)
class_index = np.argmax(prediction)

# Convert index (0–25) to A–Z
predicted_letter = chr(65 + class_index)
print(f"🔤 Predicted letter: {predicted_letter}")
