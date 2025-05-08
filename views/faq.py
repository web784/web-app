import streamlit as st



def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

THIS_DIR = (__file__).parent if "__file__" in locals() else path.cwd()
STYLES_DIR = THIS_DIR / "styles"
ASSETS_DIR = THIS_DIR / "assets"
AUDIOS_DIR = THIS_DIR / "audios"
VIDEOS_DIR = THIS_DIR / "videos"
CSS_FILE = STYLES_DIR / "style.css"


st.set_page_config(
    page_title="🤷‍♀️ FAQ",
    page_icon=":material/info:",
    layout="wide",
    initial_sidebar_state="collapsed"
)
load_css_file(CSS_FILE)















st.header("WELCOME TO NGUVU KUU FAQ")
st.write("---")
st.subheader(":raising_hand: FAQ",anchor=False)
faq = {
    "SWALI LA 1 : Kanisa Lina Patikana Wapi?": "JIBU : Kanisa Lina Patikana Arusha Tanzania",
    "QUESTION 1 : Were The Church Is Located?": "ANSWER : Church Was Located At Arusha Region In Tanzania",
    "SWALI LA 2 : Jinsi Ya kutuma Sadaka Yangu?": "JIBU : Tuma Sadaka Yako Kwenda Namba Hizi [M-PESA : 0756302908] & [HALO-PESA : 0618102908] Jina David H. Kalalu",
    "QUESTION 2 : How Can I Send My Offer?": "ANSWER : To Send Your Offer Send To This Numbers [M-PESA : 0756302908] & [HALO-PESA : 0618102908] Name David H. Kalalu",
}
for question, answer in faq.items():
    with st.expander(question):
        st.code(answer)