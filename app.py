import streamlit as st 
import numpy as np 
import pytesseract #python wrapper for the ocr software 
from PIL import Image 
st.title('OPTICAL CHARACTER RECOGNITION')
st.text('Upload the Image')

uploaded_file = st.sidebar.file_uploader('Choose an image :', type = ["jpg","png","jpeg"])   #create a file uploader in the sidebar 
if uploaded_file is not None:     #follow the below steps only if there is some file uploaded in the uploader
  img = Image.open(uploaded_file) #read the uploaded image, open it 
  st.image(img, caption = 'Uploaded Image',use_column_width=True) #display the image on the webapp screen #,use_column_width=True means keep original image size 
  st.write("")  #print blank space

  if st.button('PREDICT'):
    st.write("Extracted text : ")
    output = pytesseract.image_to_string(img) # pytesseract converts image to text and then prints the output 
    st.write(output)
