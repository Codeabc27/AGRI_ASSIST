# import tensorflow as tf

# from tensorflow.keras.applications import MobileNetV2
# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# from tensorflow.keras import layers, models

# IMG_SIZE = 224
# BATCH_SIZE = 32

# train_dataset = tf.keras.utils.image_dataset_from_directory(
#     r"dataset/CNN_dataset/train",
#     image_size=(IMG_SIZE, IMG_SIZE),
#     batch_size=BATCH_SIZE,
# )

# validation_dataset = tf.keras.utils.image_dataset_from_directory(
#     r"dataset/CNN_dataset/val",
#     image_size=(IMG_SIZE, IMG_SIZE),
#     batch_size=BATCH_SIZE,
# )
# class_names = train_dataset.class_names

# train_dataset = train_dataset.map(lambda x, y: (preprocess_input(x), y))

# validation_dataset = validation_dataset.map(lambda x, y: (preprocess_input(x), y))

# base_model = MobileNetV2(
#     input_shape=(224, 224, 3), include_top=False, weights="imagenet"
# )

# base_model.trainable = False

# model = models.Sequential(
#     [
#         layers.Input(shape=(224, 224, 3)),
#         base_model,
#         layers.GlobalAveragePooling2D(),
#         layers.Dropout(0.3),
#         layers.Dense(len(class_names), activation="softmax"),
#     ]
# )

# model.compile(
#     optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
# )

# history = model.fit(train_dataset, validation_data=validation_dataset, epochs=10)

# model.save("model/mobilenet_tomato_model.h5")

# print("MobileNetV2 Model Saved")
