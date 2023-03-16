import streamlit as st
from PIL import Image
from streamlit_extras.colored_header import colored_header


# HEADER
colored_header(
    label=" :green[**Pankaj jewellers** deals in all kinds of ornaments] ________",
    description="DISPLAYING SOME :- ",
    color_name="red-70",
)

# TABS
tab1, tab2, tab3 = st.tabs(["Bhagwan ji", "Gold", "Silver"])
with tab1:
   st.header(":red[LAKSHMI GANESH JI]")
   st.text("")
   st.text("")
   image1 = Image.open('lakshmi ganesh.jpg')
   st.image(image1,caption="Lakshmi Ganesh", width=400)

with tab2:
   st.header(":violet[GOLD ITEMS]")
   st.text("")
   st.text("")
   image2 = Image.open('shopsona.jpg')
   st.image(image2, width=400)
   with st.expander("SEE OPTIONS :"):
    st.write("Sells several gold items according to your preference, you just state it !!")
    st.image("neck.jfif",caption=" Beautiful neckpiece", width= 300)

with tab3:
   st.header(":violet[SILVER ITEMS]")
   st.text("")
   st.text("")
   image3 = Image.open('silver.jpg')
   st.image(image3, width=400)
   with st.expander("SEE OPTIONS: "):
    st.write("Sells several silver items according to your preference, you just state it !!")
    st.image("silverkada.jpg",caption="Silver bangle ",width= 300)

    st.text("")
    st.text("")
    st.text("")
    st.text("")

   colored_header(
    label=" :green[**Pankaj jewellers** official card -]",
    color_name="red-70",
    )
   st.text("")
   st.text("")
   st.text("")

   image= Image.open("card.jpg")
   st.image(image,caption=" Shop contact card")
   st.subheader("To download the card: ")
   with open("card.jpg", "rb") as file:
     btn = st.download_button(
            label="Download image",
            data=file,
            file_name="card.jpg",
            mime="image/jpg"
          )





