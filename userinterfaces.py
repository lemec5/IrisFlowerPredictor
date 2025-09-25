import streamlit as st
import joblib 
import numpy as np
model = joblib.load('flowerClassifier.pkl')

st.title('My app')

st.write('Enter flower measurement to predict the iris species')

sepal_length = st.number_input('enter sepal length')
sepal_width = st.number_input('enter sepal width')
petal_length = st.number_input('enter petal length')
petal_width = st.number_input('enter petal width')
petal_widths = st.number_input('enter petal widths')

if st.button('Predict'):
    newData = [[sepal_length, sepal_width, petal_length, petal_width, petal_widths]]
    prediction = model.predict(newData) 

    if prediction == 0:
        st.success('The predicted class is Setosa')

    elif prediction == 1:
        st.success('The predicted class is Versicolor')

    else:
        st.success('The predicted class is virginica')


