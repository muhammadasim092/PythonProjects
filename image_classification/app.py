import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model 
import numpy as np
import streamlit as st

model = load_model('D:\Introduction to Programming with Python\PythonProjects\image_classification\image_classifier.keras')

data_cat = ['apple',
 'banana',
 'beetroot',
 'bell pepper',
 'cabbage',
 'capsicum',
 'carrot',
 'cauliflower',
 'chilli pepper',
 'corn',
 'cucumber',
 'eggplant',
 'garlic',
 'ginger',
 'grapes',
 'jalepeno',
 'kiwi',
 'lemon',
 'lettuce',
 'mango',
 'onion',
 'orange',
 'paprika',
 'pear',
 'peas',
 'pineapple',
 'pomegranate',
 'potato',
 'raddish',
 'soy beans',
 'spinach',
 'sweetcorn',
 'sweetpotato',
 'tomato',
 'turnip',
 'watermelon']

img_width = 180
img_height = 180 
st.header('Image Classification Model')

img = st.text_input(
    'Enter Image name',
    r'D:\Introduction to Programming with Python\PythonProjects\image_classification\Apple.jpg'
)



image_load = tf.keras.utils.load_img(img, target_size=(img_width, img_height))
img_arr = tf.keras.utils.array_to_img(image_load)
img_bat = tf.expand_dims(img_arr,0)

predict = model.predict(img_bat)

score = tf.nn.softmax(predict)

st.image(img , width=200)

st.write('Veg/Fruit in image is {} with accuracy of {:.2f}%'.format(data_cat[np.argmax(score)], np.max(score) * 100))
