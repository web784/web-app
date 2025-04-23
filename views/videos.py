import streamlit as st





st.write("##")
st.write("##")
st.write("##")
with st.container():
    row1_column,row2_column,row3_column = st.columns(3, gap="large", vertical_alignment="center")
    with row1_column:
        st.write("")
    with row2_column:
        st.title("NO VIDEOS UPLOADED")
        st.toast("Sory Videos Will Be Uploaded Soon")
        st.toast("Samahani Video Zitarushwa Hivi Karibuni")

























# # st.set_page_config(page_title="Videos", layout="wide",)


# # with st.container():
# #     left_column,rigth_column = st.columns(2, gap="small")
# #     with left_column:
# #         st.title("NGUVU KUU ZA MUNGU  VIDEOS")
# #         st.header("DATE/TAREHE")
# #         st.write("---")
# # with st.container():
# #     st.code("6/4/2026")
# #     left_column,rigth_column = st.columns(2, gap="large")
# #     with left_column:
# #         st.subheader("mahubiri")
# #         st.write("---")
# #         st.video("./videos/7.webm")
# #     with rigth_column:
# #         st.subheader("Ushuhuda")
# #         st.write("---")
# #         st.video("./videos/6.webm")
# # with st.container():
# #     st.code("-------------")
# #     left_column,rigth_column = st.columns(2, gap="large")
# #     with left_column:
# #         st.subheader("Ushuhuda")
# #         st.write("---")
# #         st.video("./videos/4.webm")
# #     with rigth_column:
# #         st.subheader("Mahubiri")
# #         st.write("---")
# #         st.video("./videos/5.webm","lol")