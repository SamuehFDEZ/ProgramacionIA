import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

# Cargar todas las imágenes sin dividir
batch_size = 32
img_height = 128
img_width = 128

full_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    image_size=(img_height, img_width),
    batch_size=batch_size,
    label_mode='binary'
)

# Convertir el Dataset en un array para poder dividirlo
images = []
labels = []

# Cargar imágenes y etiquetas en listas (2 elementos dada la estructura de datos)
for image_batch, label_batch in full_ds:
    images.append(image_batch.numpy())
    labels.append(label_batch.numpy())

images = np.concatenate(images)
labels = np.concatenate(labels)

# Dividir el conjunto de datos en entrenamiento (80%), validación (10%) y test (10%)
X_train, X_temp, y_train, y_temp = train_test_split(images, labels, test_size=0.2, random_state=123)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=123)

# Volver a convertir a datasets de TensorFlow
train_ds = tf.data.Dataset.from_tensor_slices((X_train, y_train)).batch(batch_size)
val_ds = tf.data.Dataset.from_tensor_slices((X_val, y_val)).batch(batch_size)
test_ds = tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(batch_size)