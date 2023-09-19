from tensorflow.keras.applications import VGG16 #importing model 
from google.colab import drive

#create model instance 
base_model = VGG16(weights = 'imagenet')

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
import tensorflow as tf

# Load and preprocess your input image (replace 'image_path' with your image file path)
img_path = '/content/drive/MyDrive/cats/cat2.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = preprocess_input(x)
x = tf.expand_dims(x, axis=0)  # Add batch dimension

# Make predictions
predictions = base_model.predict(x)
decoded_predictions = decode_predictions(predictions, top=5)[0]

# Display the top 5 predicted classes
for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print(f"{i + 1}: {label} ({score:.2f})")
