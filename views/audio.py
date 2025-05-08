import streamlit as st

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


# DIAOLOG BOX SETUP STARTS
@ st.dialog("INFO")
def show_contact_form():
    st.status("OPPS!!!! SORY NO AUDIOS UPOADED")
    st.title("WE WILL UPLOAD SOON AS FAST AS WE CAN")


load_css_file(CSS_FILE)

# BUTTOM CONFIG FOR DIALOG SETUP
with st.container():
    st.header("Nguvu Kuu Audios Library")
    st.toast("Sory Audios Will Be Uploaded Soon")
    st.toast("Samahani Audio Zitarushwa Hivi Karibuni")
    st.write("---")
    if st.button("READE THIS INFO"):
        show_contact_form()
    # if st.button("Litsen Audios"):
    #     with st.container():
    #         st.title("Tarehe/Date")
    #         st.subheader("---------")
    #         left_column,center_column,rigth_column = st.columns(3)
    #         with left_column:
    #             st.write("\n")
    #             st.write("Ushuhuda Wa Jumapili")
    #             st.write("---")
    #             #st.audio("./assets/1.mp3")
    #             st.write("Audio Will Be Uploded Soon")
    #             st.write("Audio Zita Rushwa Ivi Karibuni")
    #         with center_column:
    #             st.write("\n")
    #             st.write("Mahubiri Ya Jumapili")
    #             st.write("---")
    #             #st.audio("./assets/1.mp3")
    #             st.write("Audio Will Be Uploded Soon")
    #             st.write("Audio Zita Rushwa Ivi Karibuni")
    #         with rigth_column:
    #             st.write("\n")
    #             st.write("Maombi Ya Jumapili")
    #             st.write("---")
    #             #st.audio("./assets/1.mp3")
    #             st.write("Audio Will Be Uploded Soon")
    #             st.write("Audio Zita Rushwa Ivi Karibuni")
    #     with st.container():
    #         st.title("Tarehe/Date")
    #         st.subheader("---------")
    #         left_column,center_column,rigth_column = st.columns(3)
    #         with left_column:
    #             st.write("\n")
    #             st.write("Ushuhuda Wa Jumapili")
    #             st.write("---")
    #             #st.audio("./assets/1.mp3")
    #             st.write("Audio Will Be Uploded Soon")
    #             st.write("Audio Zita Rushwa Ivi Karibuni")
    #         with center_column:
    #             st.write("\n")
    #             st.write("Mahubiri Ya Jumapili")
    #             st.write("---")
    #             #st.audio("./assets/1.mp3")
    #             st.write("Audio Will Be Uploded Soon")
    #             st.write("Audio Zita Rushwa Ivi Karibuni")
    #         with rigth_column:
    #             st.write("\n")
    #             st.write("Maombi Ya Jumapili")
    #             st.write("---")
    #             #st.audio("./assets/1.mp3")
    #             st.write("Audio Will Be Uploded Soon")
    #             st.write("Audio Zita Rushwa Ivi Karibuni")
    #     with st.container():
    #         st.title("Tarehe/Date")
    #         st.subheader("---------")
    #         left_column,center_column,rigth_column = st.columns(3)
    #         with left_column:
    #             st.write("\n")
    #             st.write("Ushuhuda Wa Jumapili")
    #             st.write("---")
    #             #st.audio("./assets/1.mp3")
    #             st.write("Audio Will Be Uploded Soon")
    #             st.write("Audio Zita Rushwa Ivi Karibuni")
    #         with center_column:
    #             st.write("\n")
    #             st.write("Mahubiri Ya Jumapili")
    #             st.write("---")
    #             #st.audio("./assets/1.mp3")
    #             st.write("Audio Will Be Uploded Soon")
    #             st.write("Audio Zita Rushwa Ivi Karibuni")
    #         with rigth_column:
    #             st.write("\n")
    #             st.write("Maombi Ya Jumapili")
    #             st.write("---")
    #             #st.audio("./assets/1.mp3")
    #             st.write("Audio Will Be Uploded Soon")
    #             st.write("Audio Zita Rushwa Ivi Karibuni")