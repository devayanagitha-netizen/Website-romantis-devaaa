import streamlit as st

st.set_page_config(
    page_title="A Little Flower for You",
    page_icon="🌷",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #F8F1E7;
    color: #725747;
}
h1, h2, h3 {
    color: #96745E;
    text-align: center;
}
p {
    color: #806B5B;
    font-size: 17px;
}
.stButton button {
    background-color: #D8BFA9;
    color: white;
    border-radius: 20px;
    border: none;
    padding: 10px 25px;
}
.flower {
    text-align: center;
    font-size: 35px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="flower">🌷 🌼 🌷</div>',
    unsafe_allow_html=True
)

st.title("A Little Flower for You")

st.markdown(
    "<center><i>Made with love by Devaaa ♡</i></center>",
    unsafe_allow_html=True
)

st.header("Hai, Rahadian Haryo Argani! ♡")

st.write(
    "Ada sesuatu yang ingin Devaaa tunjukkan "
    "khusus untuk kamu."
)

if st.button("Buka hadiah kecil dari Devaaa 💌"):
    st.balloons()
    st.success(
        "Hai Rahadian! Terima kasih sudah menjadi "
        "bagian dari cerita indah Devaaa. ♡"
    )

st.markdown("---")
st.markdown("<center>Made with ♡ by Devaaa</center>",
            unsafe_allow_html=True)
