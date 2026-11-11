import streamlit as st


st.header("Taswira AI")
st.write("Fetal AI ultrasound image analysis and prediction tool to support resource-limited midwives")
st.subheader("Review an ultrasound frame")
uploaded_file = st.file_uploader("Upload an ultrasound image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Ultrasound Image", width=600)
    st.write("Image uploaded. Model prediction is not connected yet.")
    # Here you would add your image analysis code
    st.write("Analysis complete. Results will be displayed here.")