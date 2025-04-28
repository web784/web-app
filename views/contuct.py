import streamlit as st



st.set_page_config(page_title="Nguvu Kuu Message", layout="wide")


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




st.title("SEND YOUR MESSAGE HERE")
st.write("---")

# response message

st.toast("We Will Responde Through Your Email/Gmail")
st.toast("Utajibiwa Kupitia Email/Gmail Yako")
with st.container():
     if st.button("SEND HERE"):
          show_contuct_form()





st.status("Enjoy Using Our Website Secuerly")
st.status("Furahia Tovutihii")
