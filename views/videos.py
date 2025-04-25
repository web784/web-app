import streamlit as st

st.set_page_config(page_title="Videos", layout="wide",)

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
    # if st.button("Watch videos"):
        # with st.container():
        #     left_column,rigth_column = st.columns(2, gap="small")
        #     with left_column:
        #         st.header("DATE/TAREHE")
        #         st.write("---")
        # with st.container():
        #     st.code("6/4/2026")
        #     left_column,rigth_column = st.columns(2, gap="large")
        #     with left_column:
        #         st.subheader("mahubiri")
        #         st.write("---")
        #     with rigth_column:
        #         st.subheader("Ushuhuda")
        #         st.write("---")
        # with st.container():
        #     st.code("-------------")
        #     left_column,rigth_column = st.columns(2, gap="large")
        #     with left_column:
        #         st.subheader("Ushuhuda")
        #         st.write("---")
        #     with rigth_column:
        #         st.subheader("Mahubiri")
        #         st.write("---")