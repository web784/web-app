# ---------- PAGE RUNNER PACK --------         
import streamlit as st
# WEB PAGE SETUP
st.set_page_config(page_title="Nguvu Kuu Online", layout="wide",)


# WEB PAGE STARDED


with st.container():
    st.title("NGUVU KUU ZA MUNGU")
    left_column,rigth_column = st.columns(2, gap="large")
    with left_column:
        st.write("#")
        st.subheader("WELCOME TO NGUVU KUU ONLINE" )
        st.write("---")
        st.write("WE HAVE GIVEN A CUP OF MERCY")
        st.write("Kwa Sababu Mungu Ni Mmoja, Na Mpatanishi Kati Ya Mungu Na Mwanadamu Ni Mmoja, Mwanadamu Kristo Yesu")
        st.write("For There Is One God And One Mediator Between God And Men, The Man Christ Jesus")
        with rigth_column:
            st.image("./assets/logo2.png", width=300)


with st.container():
    st.write("---")
    st.write("\n")

    # Documantion: https://localhost/ !!! CHANGE THE EMAIL ADRESS !!!


with st.container():
    left_column,rigth_column,center_column = st.columns(3, gap="small")
    with left_column:
            st.write("Tuna Weza Kufanya Lolote Katika Yeye Atutiae Nguvu")
            st.write("\n")
            st.image("./assets/hug.jpg", width=300)# ,st.write("l")
    with rigth_column:
            st.write("We Can Do All This Through Him Gives Us Strength")
            st.write("\n")
            st.image("./assets/huf.jpg", width=300)# local
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
    st.title("SERVICE TIME/RATIBA ZA IBADA")
    left_column,center_column,rigth_column = st.columns(3)
    with left_column:
            st.subheader("WENESDAY")
            st.write("\n")
            st.code("""
                Starts At 16:00pm
                Praising And Worshiping
                    """
            )

    with center_column:
            st.subheader("FRIDAY")
            st.write("\n")
            st.code("""
                Starts At 14:00pm
                Praising And Worshiping
                    """
            )
    with rigth_column:
            st.subheader("SUNDAY")
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
            st.subheader("JUMA TANO")
            st.write("\n")
            st.code("""
                Ibada Inaanza Saa 10:00pm
                Ibada Itakuwa Maubiri , Maombi Na Maombezi
                    """
            )

    with center_column:
            st.subheader("IJUMAA")
            st.write("\n")
            st.code("""
                Ibada Inaanza Saa 10:00pm Na kwa Wanakwaya Ni Saa 8:00pm
                Ibada Itakuwa Na Maubiri , Maombi Na Maombezi
                    """
            )
    with rigth_column:
            st.subheader("JUMAPILI")
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
        st.subheader("KWA MAWASILIANO ZAIDI")
        st.write("""
            Kanisa Lina Patikana Arusha Sanawari Ya Juu Kata Ya Oltroto

            Pia tuna patikana kwa simu namba 

            0756302908

            0618102908
            """
    )
    with left_column:
        st.subheader("FOR MORE INFORMATION")
        st.write("""
            Church Was Located At Arusha Sanawari Oltroto

            For Phone Call Use Those Phone Numbers 

            0756302908

            0618102908
            """
    )
        st.write("---")


with st.container():
    col1_column,col2_column,col3_column,col4_column, = st.columns(4, gap="small")
    with col1_column:
        st.write("Weka Maisha Yako Kwa Mungu")
        st.write("---")
        st.write("""
            Faida Za Kuweka Maisha Yako Kwa Mungu

            1: Mwisho Wa Magonjwa

            2: Furaha Maishani

            3: Amani Ya Milele

            """
    )
    with col2_column:
        st.write("Bring Your Life To Jesus")
        st.write("---")
        st.write("""
            Beneficts Of Bringing Your Life To Jesus

            1: The End Of Deases

            2: Life In Happyness

            3: Endless Peace
            """
    )
    with col3_column:
        st.write("Kataa Sanamu Maishani")
        st.write("---")
        st.write("""
            Sanamu Ni Kile Kitu Ambacho Kina Nafasi Ya Mungu Kwako

            1: Fedha

            2: Mume Au Mke 

            3: Watoto Na Kazalika
            """
    )
    with col4_column:
        st.write("Disagree Other Gods")
        st.write("---")
        st.write("""
            Gods Are Things That Took Place Of Jesus In Your Life

            1: Money

            2: husband or wife

            3: Childrens & etc.
            """
    )
with st.container():
    st.write("##")
    st.header("Also Nguvu Kuu")
    st.write("""In This Section Nguvu Kuu Also Bring To You Many Words That Can Inspire You To Agree
                To Jesus That You Will Became His Childe Forever, If You Agree With Me Pleas Make
                A Pray To Jesus And Say This Words Pleas God I Whant To Be The One Who Will Be Entered To Jerusalem
                The Day Of Our Celebration Place Of Our Events And Jesus Will Responde To You If You Will Be
                The One Pleas Don‛t Forget To Send Your Offer To Jesus Our Church Was Located At Arusha Tanzania
                And God Bless You AMEN
    """)
with st.container():
    st.status(" If We Will Have An Update We Will Bring To You Imediatly Amen")
    st.status(" Kama Kutakuwa Na Mengine Zaidi Hatuta Sita Kuku Tumia Amen")