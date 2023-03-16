import streamlit as st
from PIL import Image
from streamlit_extras.colored_header import colored_header
import graphviz

# HEADER
colored_header(
    label=" **A little history lesson**____:",
    description="ABOUT THE FAMILY : ",
    color_name="green-70",
)

st.text("")
st.text("")
st.text("")

# GRAPHVIZ
graph = graphviz.Digraph()
graph.edge("Shri. Baldev Raj ji", 'Mr. Pankaj Kumar')
graph.edge('Mr. Pankaj Kumar', 'Chiranjeev Pankaj Kumar')
st.graphviz_chart(graph,use_container_width=True)

st.write("_________________________________________________________________________________________________________________")

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

options= st.selectbox(":blue[What would you like to see]: Choose any of the options below : ",
                  ("Our owner","Card","QRcode"))
if options == "Our owner":
    image2 = Image.open('OWNER.jpeg')
    st.image(image2, width=400)

    with open("OWNER.jpeg", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="OWNER.jpeg",
            mime="image/jpeg"
          )
if options == "Card":
    image2 = Image.open('card.jpg')
    st.image(image2, width=400)

    with open("card.jpg", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="card.jpg",
            mime="image/jpg"
          )
if options == "QRcode":
    image2 = Image.open('shopqr_code.png')
    st.image(image2, width=400)

    with open("shopqr_code.png", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="shopqr_code.png",
            mime="image/png"
          )
