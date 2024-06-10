import streamlit as st
import pandas as pd
st.title('obesity pred')
ID = st.number_input("Enter your ID")
Age = st.number_input("Enter your Age")
Gender = st.number_input("Enter Gender")
Height = st.number_input("Enter your Height")
Weight = st.number_input("Enter your Weight")
BMI = st.number_input("Enter your BMI")

test = pd.DataFrame({'ID':ID,
                     'Age':Age,
                     'Gender':Gender,
                     'Height':Height,
                     'Weight':Weight,
                     'BMI':BMI},index=[0])

if st.button("submit"):
 import pickle
 model = pickle.load(open("obesity1.pkl",'rb'))
 st.write(model.predict(test))
