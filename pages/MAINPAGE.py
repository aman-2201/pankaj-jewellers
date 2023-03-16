import streamlit as st
from PIL import Image
from streamlit_extras.colored_header import colored_header

#TITLE AND IMAGE
st.title(" :gem: :green[PANKAJ] JEWELLERS _and_ :blue[SON] :gem: ")
st.text("")
image = Image.open("pankajjewellers.jpg")
st.image(image,caption = " \"The talk of the townn\" ")

st.text("")
st.text("")

# BUTTON
if st.button("!! CLICK ME !!C'mon try it once :smirk:"):
    st.header(" :orange[ WELCOMEE TO YOUR SAFE SPACE!!!] :heart_eyes:")
    st.balloons()
else:
    print("How come you did'nt click me? :angry:")

st.text("")
st.text("")
st.text("")
st.text("")

# RADIO
reply = st.radio(
    "WOULD YOU LIKE TO BE SURPRISED FURTHERR?",
    ("maybe","yes","no"))
st.text("")
st.text("")
st.text("")

if reply == "maybe":
    st.subheader("Convert it to a YES 🥰")
if reply == 'yes':
    colored_header(
    label="**A few words describing the** ________:",
    description="jo bhi likhna ho yha like-",
    color_name="violet-70",)

    st.text("")
    st.text("")

    col1, col2 = st.columns(2)
    col1.metric(":violet[SUCCESS RATE]", "1000 %", "100 %")
    col2.metric(":violet[GUARANTEE]", "101 %", "100 %")
if reply == "no":
    st.subheader("Well your loss!! :unamused:")


st.text("")



st.text(" ")
st.text(" ")
st.text(" ")
st.text("")
st.text("")

# DOWNLOAD IMAGE
with open("pankajjewellers.jpg", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="pankajjewellers.jpg",
            mime="image/jpg"
          )

 


