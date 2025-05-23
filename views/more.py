import time

import numpy as np

import streamlit as st

# --- PATH SETTING ---
THIS_DIR = (__file__).parent if "__file__" in locals() else path.cwd()
STYLES_DIR = THIS_DIR / "styles"
ASSETS_DIR = THIS_DIR / "assets"
AUDIOS_DIR = THIS_DIR / "audios"
VIDEOS_DIR = THIS_DIR / "videos"
CSS_FILE = STYLES_DIR / "style.css"



st.set_page_config(
    page_title="Nguvu Kuu About",
    page_icon=":material/info:",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# --- GENERAL SETTING ---
STRIPE_CHECKOUT = "link from anothou website"



def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.02)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(0)
my_bar.empty()
load_css_file(CSS_FILE)

st.title("ABOUT NGUVU KUU ONLINE",anchor=False)



st.write("---")
st.subheader("KUHUSU",anchor=False)


with st.container():
        st.write("KUHUSU KANISA LA NGUVU KUU TUNA PATIKANA ARUSHA SANAWARI YA JUU TANZANIA")
        with st.container():
                col1_column,col2_column, = st.columns(2, gap="small")
                with col1_column:
                        st.write("""
                        Tovuti Hii Ya Kanisa La Nguvu Kuu Imetengenezwa Na Kanisa Kwaajili Yakuifikisha Kazi Ya Mungu Kimataifa.
                        ajenda yetu dunia nzima imjue mungu
                        tutuma Sadaka Yako.
                                """
                )
                with col2_column:
                        st.write("""
                        SIMU NAMBA, 0756302908 , 0618102908
                        Mungu Atakuzidishia Zaidi Na Zaidi.
                        Okoka Leo Nafamilia Yako Muingie Mbinguni Njoo Wewe Familia Ndugu Jamaa Na Marafiki
                        Muokoke Leo Mungu Wetu Ni Wa Rehema Ukiamini Utaokolewa Njoo Leo Utengeneze Kesho Njema
                        Amen.

                                """
                )
with st.container():
        st.write("TUNA WEZA KUFANYA LOLOTE KATIKA YEYE ATUTIAE NGUVU.")
        st.write("""
                Uponyaji, Kufunguliwa, Kuokoka, Ni Nguvu Kuu Za Mungu Njoo
                Na Bwana Awejuu Yako Ukiamini Utapokea Bali Akunamatokeo 
                Yoyote Pasipokuamini.
                """
        )




st.write("---")
st.subheader("ABOUT",anchor=False)
st.write("""
        We Are The CHILDRENS Of GOD We Have Create This Web For All People From This World In Order Them To Knwo God And Then To Be The One Who Will Go In Heaven
        If You Have Been Savied By God Through This Web site

        Don't Forget To Send Your Offer _ _ _

        Send It Through This Numbers

        PHONE NO 0756302908 , 0618102908

        We Can Do All This Through Him Gives Us Strength
        PHILP 4:13 
                """
        )

st.write("##")
st.code("[ DEVELOPDE By @Webacco With code better ] Contuct us At Webacco177@gmail.com")
st.write("""Webacco From Arusha Tanzania

 We Are Website Developer, Ai Chatbot, Mobile Applications, Online Marketing, Grafics Desine, Post maker & etc.
 
 For Works Like This Don't Forget To Contuct Us To This Gmail Account Webacco177@gmail.com"""
         )

