import streamlit as st
import time


def disable(b):
    st.session_state["disabled"] = b


def launch_app():
    # set page's credentials
    st.title("Super Resolution")
    # set page's description
    st.text("Super-resolution problem solving for the Digital Breakthrough hackathon")

    
    # upload video and get it's object
    uploaded_video = st.file_uploader("Pick a file", type=['mp4', 'wav'])

    # if video uploaded successfully, show it to user
    if uploaded_video != None:
        # show error if no video has been uploaded
        try:
            with st.spinner("Wait..."):
                time.sleep(5)
            st.success("Done!")
            video = open(uploaded_video.name, "rb")
            st.video(video)
        except:
            st.error("No file uploaded :(")


if __name__ == "__main__":
    launch_app()