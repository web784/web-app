import streamlit as st

from io import StringIO

import pandas as pd

import numpy as np

import time

import altair as alt

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











with st.spinner("// :blue[5 Sec To Complet...] //"):
    time.sleep(0.1)



st.header("WELCOME TO NGUVU KUU :blue[FAQ]",anchor=False)
st.write("---")
st.subheader("This Page Includes All :blue[Faq] From All Pages But It Have Some More Faq For You",anchor=False)
with st.container():
    l1_column, l2_column = st.columns(2, gap="medium")
    with l1_column:
        st.subheader("",divider=True)
        st.write(":blue[FAQ] It Is Something Like A Public Teacher That Helps You To Understand Something Whithout A Public Teacher Or Some Thing Eles But It Is More Help Full For Fast Understanding It Is Like A Lead That Can Lead Some Bodey To Something Eles .")

    with l2_column:
        st.subheader("")
        st.write(":blue[ABOUT FAQ] This Maide In Oder To Avoid Some Miss Understandi Betwen The User And Website Developer Because Not All Peaple Can Undarstand Every Thing Not But This Can Make All To Understand Some Functionality From This Website And How To Do Something .")


with st.status("loading data...", expanded=True) as status:
    st.write("Found URL.")
    time.sleep(0.1)
    st.write("Searching for data...")
    time.sleep(0.1)
    st.write("loading data...")
    time.sleep(0.1)
    status.update(
        label="loading complete!", state="complete", expanded=False
    )

st.subheader(":raising_hand: :blue[FAQ]",anchor=False, divider="blue")
faq = {
    ":blue[SWALI LA 1 :] Kanisa Lina Patikana Wapi?": ":green[JIBU :] Kanisa Lina Patikana Arusha Tanzania",
    ":blue[QUESTION 1 :] Were The Church Is Located?": ":green[ANSWER :] Church Was Located At Arusha Region In Tanzania",
    ":blue[SWALI LA 2 :] Jinsi Ya kutuma Sadaka Yangu?": ":green[JIBU :] Tuma Sadaka Yako Kwenda Namba Hizi [:red[M-PESA] : :green[0756302908]] & [:orange[HALO-PESA] : :green[0618102908]] Jina David H. Kalalu",
    ":blue[QUESTION 2 :] How Can I Send My Offer?": ":green[ANSWER :] To Send Your Offer Send To This Numbers [:red[M-PESA] : :green[0756302908]] & [:orange[HALO-PESA] : :green[0618102908]] Name David H. Kalalu",
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)


with st.container(border=True):
    c2, c1 = st.columns(2, gap="large")
    with c1:
        st.subheader("🧏🏿‍♀️ :blue[FAQ]",anchor=False, divider="blue")
        faq = {
            ":blue[QUESTION 1 :] Why Do I Have To Do This ?": "ANSWER : Because If You Beleave In Something You Will Practice It Inoder To Find More",
            ":blue[QUESTION 2 :] What About Readings": "ANSWER : Reading Is The Best Way To Make Things Easy Because Many Books Have A Leade For Something Eals",
        }
        for question, answer in faq.items():
            with st.expander(question):
                st.code(answer)

    with c2:
        st.subheader("🙇🏿:blue[Make Things Easy]")
        st.write( """
                How To Make Things Easy To Use There :orange[Three Main Things] To Practice
                
                :blue[**.** 1] Beliving
                 
                :blue[**.** 2] Reading
                 
                :blue[**.** 3] Practising
                """ )

st.write("")
with st.container(border=True):
    c1, c2 = st.columns(2, gap="large",)
    with c1:
        st.subheader("🤷‍♀️ :blue[FAQ]",anchor=False, divider="blue")
        faq = {
            ":blue[SWALI LA 1 :] Kwanini Naitajika Kufanya Ivyo ?": ":green[JIBU :] Kwa Sababu Kama Mtu Anaamini Juu Ya Kitu Fulani Anabudi Kufanya Majribio",
            ":blue[SWALI LA 2 :] Vipi Kuhusu Kusoma ?": ":green[JIBU :] Kusoma Ndio Njia Bora Zaidi Ya Kufanya Vitu Kuwa Rahisi Kwasababu Vitabuu Ni Muongozo Kuhusu Kitu Fulani",
        }
        for question, answer in faq.items():
            with st.expander(question):
                st.write(answer)

    with c2:
        st.subheader("🙇🏿‍♂️:blue[Fanya Mambo Kuwa Rahisi]")
        st.write( """
                Ni Namna Gani Unaweza Kufanya Mambo Kuwa Rahisi Kuna :orange[Mambo Matatu]
                
                :blue[**.** 1] Kuamini
                 
                :blue[**.** 2] Kusoma
                 
                :blue[**.** 3] Majaribio
                """ )