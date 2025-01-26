import streamlit as st

# Create a dictionary of diseases and their corresponding URLs
disease_urls = {
    "Diabetes": "https://diabetes-project2-do5rkns6aljsqwcurxksb5.streamlit.app/",
    "Titanic": "https://titanic-project-ez6yomzl3lcsc8t7ruxkos.streamlit.app/",
}

# Title of the app
st.title("Disease Information Portal")

# Description of the app
st.write("Select a disease to learn more and be redirected to the relevant page.")

# Disease selection dropdown
disease = st.selectbox("Select a disease:", list(disease_urls.keys()))

# Displaying the selected disease URL and adding a button for redirection
if disease:
    st.write(f"You selected: **{disease}**")
    st.write("Click the button below to visit the official webpage:")
    if st.button("Go to webpage"):
        st.write(f"[Click here to visit the {disease} page]({disease_urls[disease]})")
        st.markdown(f'<a href="{disease_urls[disease]}" target="_blank">Click here to visit the {disease} page</a>', unsafe_allow_html=True)
