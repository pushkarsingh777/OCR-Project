import streamlit as st
from ocr import extract_text

# Title of the web app
st.title("OCR Application with GOT")

# Upload image file
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Process the uploaded image
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    extracted_text = extract_text("temp_image.jpg")
    
    # Display the extracted text
    st.subheader("Extracted Text:")
    st.write(extracted_text)

    # Keyword search
    keyword = st.text_input("Enter a keyword to search:")
    
    if keyword:
        if keyword.lower() in extracted_text.lower():
            st.success(f"Keyword '{keyword}' found in the text!")
        else:
            st.error(f"Keyword '{keyword}' not found.")
