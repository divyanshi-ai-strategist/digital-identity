import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()
st.set_page_config(page_title="My Digital Identity", layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go To", ["About me", "My Projects"])
BACKEND_URL = os.getenv("BACKEND_API_URL", "http://127.0.0.1:8000")
if page == 'About me':
    st.title("👨‍💻 My LinkedIn Profile")
    try:
        response = requests.get(f"{BACKEND_URL}/profile").json()
        col1, col2 = st.columns([1, 2])
        with col1:
            if "picture" in response:
                st.image(response["picture"], width=250)
        with col2:
            st.header(f"{response.get('given_name')} {response.get('family_name')}")
            st.subheader("Senior Technical Lead") # You can hardcode this or fetch via extra scopes
            st.write(f"📧 Email: {response.get('email')}")
            st.info("This data is synced live from LinkedIn.")
    except:
        st.error(f"{BACKEND_URL}")
        #st.error(response.json()['detail'])

elif page == "My Projects":
    st.title("🚀 GitHub Portfolio")
    try:
        repos = requests.get(f"{BACKEND_URL}/projects").json()
        
        # Displaying repos in a grid
        for i in range(0, len(repos), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(repos):
                    repo = repos[i+j]
                    with cols[j].container(border=True):
                        st.markdown(f"### {repo['name']}")
                        st.write(repo['description'])
                        st.caption(f"Main Tech: {repo['tech']} | ⭐ {repo['stars']}")
                        st.link_button("Source Code", repo['url'])
    except:
        st.error("Here")
        #st.error(response.json()['detail'])

