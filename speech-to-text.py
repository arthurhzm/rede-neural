import librosa
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

audio_path = "C:\\Users\\arthu\\Downloads\\Megadeth - Holy Wars...The Punishment Due.mp3"
y, sr = librosa.load(audio_path)
num_classes = 10

mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
print(mfccs.shape)  # (13, 17112)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(None, 13)),
    tf.keras.layers.LSTM(128, return_sequences=True),
    tf.keras.layers.LSTM(128),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Suponha que `X` são os MFCCs e `y` são as labels
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
y_train = to_categorical(y_train, num_classes=num_classes)
y_val = to_categorical(y_val, num_classes=num_classes)

model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=20)