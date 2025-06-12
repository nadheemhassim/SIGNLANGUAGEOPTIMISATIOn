from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from load_data import load_data

# Load training and validation data (now split from 'train/' folder)
train_data, val_data = load_data()

# Build the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),  # Helps prevent overfitting
    Dense(26, activation='softmax')  # 26 output neurons for A-Z
])

# Compile the model
model.compile(
    optimizer=Adam(),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
history = model.fit(
    train_data,
    epochs=25,  # Feel free to increase if training looks good
    validation_data=val_data
)

# Save the trained model
model.save('models/sign_language_model.h5')
print("✅ Model has been trained and saved at 'models/sign_language_model.h5'")
