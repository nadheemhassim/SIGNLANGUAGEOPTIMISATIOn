from flask import Flask, render_template, Response, jsonify, request, send_file
import cv2
import numpy as np
import os
import random
from tensorflow.keras.models import load_model
from flask_cors import CORS



# Initialize Flask app
app = Flask(__name__)
CORS(app)


# Load trained model
model = load_model('/Users/geethakumuduni/Desktop/sign_language_project/models/sign_language_model.h5')

# Webcam
camera = cv2.VideoCapture(0)

IMG_SIZE = 64

# ✅ Now point to 'Test/' folder
DATASET_PATH = '/Users/geethakumuduni/Desktop/sign_language_project/Test'

# Store prediction text
current_prediction = ""

def preprocess(frame):
    img = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def generate_frames():
    global current_prediction

    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            x1, y1, x2, y2 = 100, 100, 300, 300
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            roi = frame[y1:y2, x1:x2]

            if roi.shape[0] > 0 and roi.shape[1] > 0:
                img = preprocess(roi)
                prediction = model.predict(img)
                pred_class = np.argmax(prediction)
                confidence = np.max(prediction)
                letter = chr(65 + pred_class)

                cv2.putText(frame, f'{letter} ({confidence*100:.1f}%)', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

                if confidence >= 0.999:
                    current_prediction = f"Prediction is: {letter}"
                else:
                    current_prediction = ""

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

#this is where prediction for frontend is given
@app.route('/prediction')
def prediction():
    global current_prediction
    return jsonify({'prediction': current_prediction})

# 🔥 Route to get sign images for typed letters
@app.route('/get_images')
def get_images():
    text = request.args.get('text', '').upper()
    images = []

    for char in text:
        char_folder = os.path.join(DATASET_PATH, char)
        if os.path.exists(char_folder):
            images_in_folder = os.listdir(char_folder)
            if images_in_folder:
                image_path = os.path.join(char_folder, random.choice(images_in_folder))
                images.append(f'/letter_image/{char}/{os.path.basename(image_path)}')

    return jsonify({'images': images})

# 🔥 Route to serve actual images
@app.route('/letter_image/<letter>/<filename>')
def letter_image(letter, filename):
    folder = os.path.join(DATASET_PATH, letter)
    return send_file(os.path.join(folder, filename), mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug=True)
