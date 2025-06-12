from tensorflow.keras.models import load_model
from load_data import load_data

# Load test data
_, test_data = load_data()

# Load model
model = load_model('/Users/geethakumuduni/Desktop/sign_language_project/models/sign_language_model.h5')

# Evaluate check accuracy
loss, accuracy = model.evaluate(test_data)
print(f"✅ Test Accuracy: {accuracy:.2%}")
