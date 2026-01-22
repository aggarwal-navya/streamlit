import streamlit as st

st.title(" kindly add city and age")
age=st.slider("select your age",1,100)
city= st.selectbox("select your city",["delhi","mumbai","meerut","banglore"])
if st.button("submit"):
    st.write(f"your age is {age} and you live in {city}")