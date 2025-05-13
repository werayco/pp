import streamlit as st
import requests

url = st.secrets["url"]
st.title("Email Classification App")

subject = st.text_input("Enter Email Subject:")
body = st.text_area("Enter Email Body:")

if st.button("Classify Email"):
    if subject and body:
        payload = {
            "Subject": subject,
            "Ordinary_Body": body,
            "Links":[]
        }
        try:
            response = requests.post(
                url=url,
                json=payload
            )
            if response.status_code == 200:
                result = response.json()
                st.success("Classification Result:")
                st.json(result)
            else:
                st.error(f"Failed with status code: {response.status_code}")
                st.text(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both subject and body.")
