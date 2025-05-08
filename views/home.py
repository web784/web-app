# --- PAGE RUNNER PACK --- 
import streamlit as st

def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



# --- PATH SETTING ---
THIS_DIR = (__file__).parent if "__file__" in locals() else path.cwd()
STYLES_DIR = THIS_DIR / "styles"
ASSETS_DIR = THIS_DIR / "assets"
AUDIOS_DIR = THIS_DIR / "audios"
VIDEOS_DIR = THIS_DIR / "videos"
CSS_FILE = STYLES_DIR / "style.css"


# --- GENERAL SETTING ---
STRIPE_CHECKOUT = "link from anothou website"




# --- WEB PAGE SETUP ---
st.set_page_config(
    page_title="Nguvu Kuu Online",
    page_icon=":telephone_receiver:",
    layout="wide",
    initial_sidebar_state="collapsed"
)
load_css_file(CSS_FILE)

@ st.dialog("IMAGE")
def show_contact_form():
    st.image("./assets/logo2.png", use_container_width=True)




# --- WEB PAGE STARDED ---
with st.container():
    st.image("./assets/logo.png", use_container_width=True)
    left_column,rigth_column = st.columns(2, gap="large", vertical_alignment="center")
    with left_column:
        st.subheader("WELCOME TO NGUVU KUU ONLINE",anchor=False )
        st.write("---")
        st.write("WE HAVE GIVEN A CUP OF MERCY")
        st.write("For There Is One God And One Mediator Between God And Men, The Man Christ Jesus 1TIM 2:5")
        if st.button("DISPLAY IMAGE"):
            show_contact_form()
    with rigth_column:
        st.subheader("")
        st.write("---")
        st.write("TUMEPEWA KIKOMBE CHA REHEMA")
        st.write("Kwa Sababu Mungu Ni Mmoja, Na Mpatanishi Kati Ya Mungu Na Mwanadamu Ni Mmoja, Mwanadamu Kristo Yesu")
        if st.button("ONYESHA PICHA"):
            show_contact_form()
with st.container():
    st.write("---")
    st.write("\n")

    # Documantion: https://localhost/ !!! CHANGE THE EMAIL ADRESS !!!


with st.container():
    left_column,rigth_column,center_column = st.columns(3, gap="small")
    with left_column:
            st.write("Tuna Weza Kufanya Lolote Katika Yeye Atutiae Nguvu")
            st.write("\n")
            st.image("./assets/hug.jpg", width=300)
    with rigth_column:
            st.write("We Can Do All This Through Him Gives Us Strength")
            st.write("\n")
            st.image("./assets/huf.jpg", width=300)
    with center_column:
            st.write("MAOMBI YA REHEMA")
            st.write("---")
            st.write(
                """
            omba maombi ya mtoza ushuru
            lakini yule mtoza ushuru alisimama mbali,wala hakuthubutu hata kuinua macho yake mbinguni ,bali alijipiga-piga kifua akisema,
            ee mungu uniwie rathi mimi mwenye dhambi"""
            )


with st.container():
    st.write("##")
    st.title("SERVICE TIME/RATIBA ZA IBADA",anchor=False)
    left_column,center_column,rigth_column = st.columns(3)
    with left_column:
            st.subheader("WENESDAY",anchor=False)
            st.write("\n")
            st.code("""
                Starts At 16:00pm
                Praising And Worshiping
                    """
            )

    with center_column:
            st.subheader("FRIDAY",anchor=False)
            st.write("\n")
            st.code("""
                Starts At 14:00pm
                Praising And Worshiping
                    """
            )
    with rigth_column:
            st.subheader("SUNDAY",anchor=False)
            st.write("\n")
            st.code("""
                Starts At 9:30:am
                There Will Be Sunday School, Praising And Worshiping
                    """
            )


with st.container():
    st.write("##")
    left_column,center_column,rigth_column = st.columns(3)
    with left_column:
            st.subheader("JUMA TANO",anchor=False)
            st.write("\n")
            st.code("""
                Ibada Inaanza Saa 10:00pm
                Ibada Itakuwa Maubiri , Maombi Na Maombezi
                    """
            )

    with center_column:
            st.subheader("IJUMAA",anchor=False)
            st.write("\n")
            st.code("""
                Ibada Inaanza Saa 10:00pm Na kwa Wanakwaya Ni Saa 8:00pm
                Ibada Itakuwa Na Maubiri , Maombi Na Maombezi
                    """
            )
    with rigth_column:
            st.subheader("JUMAPILI",anchor=False)
            st.write("\n")
            st.code("""
                Ibada Inaanza Saa 3:30:am Mpaka Saa 8:00pm
                Kutakuwa Na Ibada Ya Sunday school Ibada Kuu, Maombi Na Maombezi
                    """
            )


with st.container():
    st.write("##")
    center_column,left_column,rigth_column = st.columns(3, gap="small")
    with left_column:
            st.write("Njoo Ufunguliwe Kwa Mwanadamu Haiwezekani Lakini Kwa Mungu Inawezekana")
            st.write("\n")
            st.image("./assets/hug.jpg", width=300)# ,st.write("l")
    with rigth_column:
            st.write("Tunawakaribisha Watu Wote, Makabila Yote, Na Dini Zote Katika Kanisa La Nguvu Kuu")
            st.write("\n")
            st.image("./assets/huf.jpg", width=300)# local
    with center_column:
            st.write("NGUVU KUU ZA MUNGU")
            st.write("---")
            st.write(
                """
            Tuna Wakaribisha Watu Wote
            Katika Kanisa Letu
            Njoo Umjue Bwana Yesu Na Uokoke
            Uzaliwe Upya Ndani Ya Yesu Mnazareti Yaani Kubatizwa
            """
            )

            
with st.container():
    st.write("##")
    center_column,left_column = st.columns(2, gap="small")
    with center_column:
        st.subheader(":telephone_receiver: KWA MAWASILIANO ZAIDI",anchor=False)
        st.write("""
            Kanisa Lina Patikana Arusha Sanawari Ya Juu Kata Ya Oltroto

            Pia tuna patikana kwa simu namba 

            0756302908

            0618102908
            """
    )
        st.write("---")
    with left_column:
        st.subheader(":telephone_receiver: FOR MORE INFORMATION",anchor=False)
        st.write("""
            Church Was Located At Sanawari Arusha

            For Phone Call Use Phone Numbers 

            0756302908

            0618102908
            """
    )
        st.write("---")


with st.container():
    st.write("##")
    col1_column,col2_column, = st.columns(2, gap="small")
    with col1_column:
        st.subheader(":man_kneeling: Weka Maisha Yako Kwa Mungu",anchor=False)
        st.write("---")
        st.image("./assets/huf.jpg", width=500)
        
    with col2_column:
        st.subheader(":woman_kneeling: Bring Your Life To Jesus",anchor=False)
        st.write("---")
        st.write("""
            **Beneficts Of Bringing Your Life To Jesus**

            .End Of Deases

            .Happyness Life

            .Endless Peace

            """
    )
        st.text("")
        st.write("""
            **Faida Za Kuweka Maisha Yako Kwa Mungu**

            .Mwisho Wa Magonjwa

            .Furaha Maishani

            .Amani Ya Milele

            """
    )







# --- FAQ ---

st.write("")
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
































with st.container():
    st.text("")
    st.write("##")
    st.status("Videos And Audios Will Be Uploaded Soon Sory ")
    st.status("video na audio zitarushwa hivi karibuni samahani")