from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_data(train_dir='train/', image_size=(64, 64), batch_size=32):
    # Include validation split
    datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2,  # 20% will be used as validation
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
    )

    train_data = datagen.flow_from_directory(
        train_dir,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=True,
        subset='training'
    )

    val_data = datagen.flow_from_directory(
        train_dir,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=True,
        subset='validation'
    )

    return train_data, val_data
