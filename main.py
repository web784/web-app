import streamlit as st


# ---- page setup ---- 
home_page = st.Page(
    page="views/home.py",
    title="HOME",
    icon=":material/home:",
    default=True,
)
chat_page = st.Page(
    page="views/contuct.py",
    title="Contuct Us",
    icon=":material/chat:",
)
videos_page = st.Page(
    page="views/videos.py",
    title="Video Library",
    icon=":material/tv:",
)
audios_page = st.Page(
    page="views/audio.py",
    title="Audio Library",
    icon=":material/bar_chart:",
)
about_page = st.Page(
    page="views/more.py",
    title="About",
    icon=":material/info:",
)
faq_page = st.Page(
    page="views/faq.py",
    title="FAQ",
    icon=":material/thumb_up:",
)
test_page = st.Page(
    page="views/test.py",
    title="test",
    icon=":material/add:",
)
# --- navigation ---


pg = st.navigation(
    {
        'home': [home_page],
        "librarys": [videos_page, audios_page],
        "more": [faq_page, chat_page, about_page,test_page],
    }  
)


# ---- run navigation -----


 
pg.run()



st.logo("./assets/logo1.png")
st.write("##")
st.sidebar.text = "name"
st.sidebar.subheader("YOUR WELCOME ANY TIME ")
name = st.status("NGUVU KUU RUNNING ONLINE FOR YOU")
