import streamlit as st
import time
# --- PATH SETTING ---
THIS_DIR = (__file__).parent if "__file__" in locals() else path.cwd()
STYLES_DIR = THIS_DIR / "styles"
ASSETS_DIR = THIS_DIR / "assets"
AUDIOS_DIR = THIS_DIR / "audios"
VIDEOS_DIR = THIS_DIR / "videos"
CSS_FILE = STYLES_DIR / "style.css"

st.set_page_config(
    page_title="Nguvu Kuu Audios",
    page_icon=":material/bar_chart:",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# --- GENERAL SETTING ---
STRIPE_CHECKOUT = "link from anothou website"


def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with st.spinner("Wait for it...", show_time=True):
    time.sleep(5)

# DIAOLOG BOX SETUP STARTS
@ st.dialog("INFO")
def show_contact_form():
    st.status("OPPS!!!! SORY NO AUDIOS UPOADED")
    st.title("WE WILL UPLOAD SOON AS FAST AS WE CAN")


load_css_file(CSS_FILE)

# BUTTOM CONFIG FOR DIALOG SETUP
with st.container():
    st.header("Nguvu Kuu Audios Library",anchor=False)
    st.toast("Sory Audios Will Be Uploaded Soon")
    st.toast("Samahani Audio Zitarushwa Hivi Karibuni")
    st.write("---")
    if st.button("READE THIS INFO"):
        show_contact_form()
    st.title("Tarehe/Date",anchor=False)
    st.write("---")
    st.code("-  -  -  -")

    center_column,rigth_column = st.columns(2, gap="medium")
    with center_column:
            st.write("\n")
            st.subheader("Mahubiri")
            st.write("---")
            #st.audio("./assets/1.mp3")
            st.status("Audio Will Be Uploded Soon")
    with rigth_column:
            st.write("\n")
            st.subheader("Maombi")
            st.write("---")
            #st.audio("./assets/1.mp3")
            st.status("Audio Will Be Uploded Soon")