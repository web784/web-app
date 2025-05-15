import streamlit as st
import time
# --- PATH SETTING ---
THIS_DIR = (__file__).parent if "__file__" in locals() else path.cwd()
STYLES_DIR = THIS_DIR / "styles"
ASSETS_DIR = THIS_DIR / "assets"
AUDIOS_DIR = THIS_DIR / "audios"
VIDEOS_DIR = THIS_DIR / "videos"
CSS_FILE = STYLES_DIR / "style.css"


# --- GENERAL SETTING ---
STRIPE_CHECKOUT = "link from anothou website"


def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Nguvu Kuu Videos",
    page_icon=":material/tv:",
    layout="wide",
    initial_sidebar_state="collapsed"
)
with st.spinner("Wait for it...", show_time=True):
    time.sleep(5)
load_css_file(CSS_FILE)

# DIAOLOG BOX SETUP STARTS
@ st.dialog("INFO")
def show_contact_form():
    st.status("OPPS!!!! SORY NO VIDEO UPOADED")
    st.title("WE WILL UPLOAD SOON AS FAST AS WE CAN")




with st.container():
    st.header("Nguvu Kuu Videos Library")
    st.write("---")
    st.toast("Sory Videos Will Be Uploaded Soon")
    st.toast("Samahani Video Zitarushwa Hivi Karibuni")
    
    if st.button("READE THIS INFO"):
                show_contact_form()
    left_column,rigth_column = st.columns(2, gap="small")
    with left_column:
            st.header("DATE/TAREHE")
            st.write("---")
    with st.container():
        st.code("-  -  -  -")
        left_column,rigth_column = st.columns(2, gap="large")
        with left_column:
                st.subheader("Mahubiri")
                st.write("---")
                st.status("sory we will upload videos soon")
        with rigth_column:
                st.subheader("Mahubiri")
                st.write("---")
                st.status("sory we will upload videos soon")