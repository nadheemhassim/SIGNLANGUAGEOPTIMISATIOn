import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('/Users/geethakumuduni/Desktop/sign_language_project/models/sign_language_model.h5')

# Open webcam
cap = cv2.VideoCapture(0)

# Set the input size of your model
IMG_SIZE = 64

#building of webcam
def preprocess(frame):
    # Resize and normalize
    img = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error grabbing frame")
        break

    # Draw a box where the user should place hand
    x1, y1, x2, y2 = 100, 100, 300, 300
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
    roi = frame[y1:y2, x1:x2]

    # Only predict when box is filled
    if roi.shape[0] > 0 and roi.shape[1] > 0:
        img = preprocess(roi)
        pred = model.predict(img)
        class_index = np.argmax(pred)
        confidence = np.max(pred)
        letter = chr(65 + class_index)  # Convert 0–25 to A–Z

        # Show prediction
        cv2.putText(frame, f'{letter} ({confidence*100:.1f}%)', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Sign Language Recognition", frame)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
