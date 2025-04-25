import streamlit as st




# use local css

# def local_css(file_name):
#       with open(file_name) as f:
#       st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#local_css("pip/pip.css")



# ---- page setup ---- 
about_page = st.Page(
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
    icon=":material/camera:",
)
audios_page = st.Page(
    page="views/audio.py",
    title="Audio Library",
    icon=":material/bar_chart:",
)
salse_page = st.Page(
    page="views/more.py",
    title="About",
    icon=":material/info:",
)
# --- navigation ---


pg = st.navigation(
    {
        "Home Page": [about_page],
        "Other": [videos_page, audios_page],
        "Feedback":[chat_page],
        "Info":[salse_page],
    }
    
)


# ---- run navigation -----


 
pg.run()
st.logo("./assets/logo1.png")
st.Icon = "name"
st.sidebar.title("YOUR WELCOME ANY TIME ")
name = st.code("NGUVU KUU ONLINE FOR YOU")
#(_provided_cursor=LockedCursor(_index=2, _parent_path=(2, 0, 0), _props={'delta_type': 'imgs', 'add_rows_metadata': None}), _parent=DeltaGenerator(_provided_cursor=RunningCursor(_parent_path=(2, 0, 0), _index=4), _parent=DeltaGenerator(_provided_cursor=RunningCursor(_parent_path=(2, 0)))))


