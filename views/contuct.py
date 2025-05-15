import streamlit as st

import time

import numpy as np

# def Loading_contuct_page():
#     progress_bar = st.progress(0)
#     status_text = st.empty()

#     for i in range(0, 101):
#         progress_bar.progress(i)
#         time.sleep(0.01)

#     progress_bar = (
#         st.code(f"loading {i}% complet // YOUR WELCOME ANY TIME //") 
#     )
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
    page_title="Nguvu Kuu Contuct",
    page_icon=":material/chat:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_css_file(CSS_FILE)

@ st.dialog("INFO")
def show_contuct_form():
      st.html("""
          <!DOCTYPE html>
          <html lang="en">
          <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">


          <!-------------- STYLE FOR CONTUCT FORM ---------------->


          <style>
          .contect-container {
               height: 65vh;
               display: flex;
               align-items: center;
               justify-content: space-evenly;
               justify-content: space-evenly;
               justify-content: space-betwen;
          }

          .contect-left-titel h2 {
               font-weight: 600;
               color: #a363aa;
               font-size: 40px;
               margin-bottom: 5px;
          }
          .contect-inputs {
               width: 300px;
               border: none;
               outline: none;
               padding: 15px;
               font-weight: 300;
               color: white;
               border-radius: 50px;
               justify-content: space-evenly;
               background-color: transparent;
               border: 2px solid #ff994f;
          }

          .contect-left textarea {
               height: 160px;
               padding: 30px;
               border-radius: 20px;
               border: 2px solid #ff994f;
          }
          .contect-inputs::placeholder {
               color: #a9a9a9;
               font-family: Arial, Helvetica, sans-serif;
          }

          .j {
               display: flex;
               align-items: center;
               padding: 15px 30px;
               font-size: 16px;
               color: #fff;
               gap: 10px;
               border: none;
               border-radius: 50px;
               background: linear-gradient(270deg, #ff994f, #fa6d86);
               cursor: pointer;
          }

          .j {
               text-decoration: none;
          }
          </style>

          <!-----------  CONTUCT FORM  -------------->

          </head>

          <body>


          <div class="contect-container" id="contuct">
          <form form action="https://api.web3forms.com/submit" method="POST" class="contect-left">
          <div class="contect-left-titel">
          <h2>SEND YOUR MESSAGE</h2>
          </div>
          <input type="hidden" name="access_key" value="2d3176aa-a029-4004-aaa2-ba6770d84d40">
          <input type="text" name="name" placeholder="your name" class="contect-inputs" required>
          <input type="text" name="email" placeholder="your email" class="contect-inputs" required>
          <textarea name="message" placeholder="your message" class="contect-inputs required"></textarea>
          <button type="submit" class="j">submit</button>
          </form>


          </body>

          </html>
          """)




st.title("SEND YOUR MESSAGE HERE",anchor=False)
st.write("---")
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(0.1)
my_bar.empty()
# response message
with st.container():
     l_column,r_column = st.columns(2, gap="medium")
     with l_column:
          st.subheader("Kuhusu Contact Us",anchor=False)
          st.write(""" Section Hii Imewekwa Kwa Jili Yako Wewe Mtumiaji Wa Tuvuti Hii Matumizi Ya Section Hii Ni Kwa Jili Ya **Kutupa Mrejesho** Sisi Ili Tufanye Maboresho Au Kukupa Msaada Wewe Mtumiaji Wa Tovuti Yetu""")
     

     with r_column:
          st.subheader("About contuct us",anchor=False)
          st.write(""" This Section Has Been Created For You To **Send Feedback** To Us In Oder To Make Chages And Helping You For More Information About Our Website Enjoy Using This Website Thanks""")

if st.button("SEND HERE"):
     show_contuct_form()
st.write("---")
st.subheader("""**:raising_hand_man: CONTUCT US FAQ**""",anchor=False)
with st.container():
     l1_column, l2_column = st.columns(2,gap="medium")
     with l1_column:
          faq = {
          "SWALI LA 1 : Kwanini Tovuti Hii Inalodi Taratibu ? ": "JIBU : Hakikisha Mtandao Wako Uko Fasta Zaidi 🔌",
          "QUESTION 1 : Why Web Page Is Loding Sloowly ? ": "ANSWER : Make Sure You Have High Speed Intarnet 🔌",
          "SWALI LA 2 : Ntapataje Mrejesho Wenu ? ": "JIBU : Utapata Mrejesho Wetu Kupitia Barua Pepe Yako",
          "QUESTION 2 : How Can I Get Feedbak ? ": "ANSWER : You Will See Our Feedback To Your Email Or Gmail",
          }
          for question, answer in faq.items():
               with st.expander(question):
                    st.code(answer)
     with l2_column:
          st.subheader("ABOUT FAQ",anchor=False)
          st.write("This Section Is For Making Sure You Understand Some Fuctions Of This Website So Don't Wory Stay Come More Functionality Are Coming Soon")
          st.subheader("KUHUSU FAQ",anchor=False)
          st.write("Sectioni Hii Ni Kwa Ajili Ya Kuhakikisha Wewe Mtumiaji Wa Tovuti Kufahamu Bahazi Ya Ufanyaji Kazi Wa Tovuti Hii")
with st.container():
     r1_column, r2_column, = st.columns(2, gap= "medium")
     with r1_column:
          st.status("// Furahia Tovuti Hii Bila Malipo Yoyote //")
     with r2_column:
          st.status("// Enjoy Using This Website Without Any Payments //")


st.toast("We Will Responde Through Your Email/Gmail")
st.toast("Utajibiwa Kupitia Email/Gmail Yako")

