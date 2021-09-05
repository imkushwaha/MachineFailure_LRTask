import streamlit as st
import pickle
import numpy as np

# import the model
model = pickle.load(open('LR.pickle','rb'))

st.title("Air Temperature")
#image = Image.open('image.jpg')
#st.image(image,  width = 700)
html_temp = """
<div style="background-color:DarkSlateGray;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit Air Temperature Prediction ML App </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)

# Process_temperature
Process_temperature = st.number_input('Process_temperature')

# Rotational_speed
Rotational_speed = st.number_input('Rotational_speed')

# Machine_failure
Machine_failure = st.selectbox('Machine Failure',['No','Yes'])

# Failure Due To Heat
HDF = st.selectbox('Machine Failure Due To Heat',['No','Yes'])

# Type of machine
Type = st.selectbox('Type of Machine',['High', 'Medium','Low'])

if st.button('Predict Air Temperature'):
    # query
    
    Type_L = None
    Type_M = None
    
    if Machine_failure == 'Yes':
        Machine_failure = 1
    else:
        Machine_failure = 0

    if HDF == 'Yes':
        HDF = 1
    else:
        HDF = 0

    if Type == 'High':
        Type_L = 0
        Type_M = 0
        
    elif Type == "Medium":
        Type_L = 0
        Type_M = 1
        
    else:
        Type_L = 1
        Type_M = 0
        
    
    query = [[Process_temperature,Rotational_speed,Machine_failure,HDF,Type_L,Type_M]]
    
    st.success("The predicted air temperature is " + str((model.predict(query))))
    
    
    if st.button("About Author"):
        st.text("Name : Upendra Kumar")
        st.text("Email : upendra.kumar48762@gmail.com") 
        st.text("Oragnization : Data Science Intern at ineuron.ai")
     