import streamlit as st
from PIL import Image
from streamlit_extras.colored_header import colored_header

colored_header(
    label="**A few finishing words** ________:",
    color_name="violet-70",
)

text= st.text_area("Something for________",
                   '''_______________________''')

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")


colored_header(
    label=":::::   FINAL RATINGS   ::::: ",
    color_name="orange-70",
)

st.text("")
st.text("")


Ratings= st.slider("**Rate this web application if you'd like. We appreciate feedback !!**",0,10)
st.write("Rating",Ratings)

st.write("_________________________________________________________________________________________________________________")

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

input= st.select_slider("HOW WOULD YOU \" CK \" :crossed_fingers: RATE THIS: ",
                        options=["amm bekarr 🤮","okaii okaii 😐","bdia 😍","areyy bhut bdia 🤯","bss 😏","bsss 💗"])
st.write("Result",input)

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")


col1,mid,col2=st.columns((2,10,2))
with col1:
    st.subheader("©️")
with col2:
    st.caption(" Powered by: KR")

