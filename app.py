
import streamlit as st
from datetime import date
import streamlit.components.v1 as components

# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="A Little Flower for You ♡",
    page_icon="🌷",
    layout="centered"
)

# =========================
# CREAM AESTHETIC DESIGN
# =========================

st.markdown("""
<style>
.stApp {
    background: #F8F1E7;
    color: #705747;
}

header {
    background: transparent !important;
}

h1, h2, h3 {
    color: #96745E !important;
}

p, label {
    color: #806B5B;
}

.hero {
    background: #FFFDF8;
    border: 1px solid #E8D8C7;
    border-radius: 25px;
    padding: 35px 20px;
    text-align: center;
    margin-bottom: 20px;
}

.hero-title {
    color: #96745E;
    font-size: 34px;
    font-weight: bold;
}

.hero-subtitle {
    color: #A88B75;
    font-style: italic;
}

.flower {
    font-size: 35px;
    text-align: center;
    padding: 10px;
}

.letter {
    background: #FFFDF8;
    border: 1px solid #E8D8C7;
    border-radius: 20px;
    padding: 25px;
    line-height: 2;
    color: #705747;
    font-size: 17px;
}

.reason {
    background: #FFFDF8;
    border: 1px solid #E8D8C7;
    border-radius: 15px;
    padding: 15px;
    margin: 10px 0;
    color: #806B5B;
}

.stButton button {
    background: #D8BFA9;
    color: white;
    border: none;
    border-radius: 25px;
    padding: 10px 20px;
}

.stButton button:hover {
    background: #BFA18A;
    color: white;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("""
<div class="flower">🌷 🌼 🌷</div>

<div class="hero">
    <div class="hero-title">
        A Little Flower for You
    </div>
    <p class="hero-subtitle">
        Made with love by Devaaa ♡
    </p>
    <p>
        A little world dedicated to
        <b>Rahadian Haryo Argani</b>
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# NAVIGATION
# =========================

menu = st.radio(
    "Explore our little world ♡",
    [
        "🏡 Home",
        "💌 Love Letter",
        "🌷 Reasons",
        "📸 Our Memories",
        "🎁 Surprise",
        "🤍 Final Message"
    ],
    label_visibility="visible"
)

st.markdown("---")

# =========================
# HOME
# =========================

if menu == "🏡 Home":

    st.markdown(
        '<div class="flower">🌸 🌿 🌸</div>',
        unsafe_allow_html=True
    )

    st.title("Hai, Rahadian! ♡")

    st.markdown("""
    <div class="letter">
        Selamat datang di dunia kecil yang dibuat
        khusus oleh Devaaa untuk kamu.

        <br><br>

        Website ini mungkin sederhana,
        tetapi setiap bagian di dalamnya
        dibuat dengan penuh perhatian.

        <br><br>

        Semoga ketika kamu membukanya,
        ada senyum kecil yang hadir di wajahmu.

        <br><br>

        Enjoy your little surprise! ♡
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("Buka surat kecil 💌"):
        st.info("Yuk, pilih halaman Love Letter di atas! 🌷")

# =========================
# LOVE LETTER
# =========================

elif menu == "💌 Love Letter":

    st.title("A Letter for You")
    st.markdown(
        '<div class="flower">💌 🌷 💌</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="letter">
        Dear Rahadian Haryo Argani,

        <br><br>

        Hai kamu! Ini adalah surat kecil dari Devaaa
        yang ingin menyampaikan beberapa hal.

        <br><br>

        Terima kasih sudah hadir dan menjadi
        seseorang yang berarti dalam cerita ini.

        Aku mungkin tidak selalu pandai merangkai
        kata-kata, tetapi aku ingin kamu tahu
        bahwa setiap momen sederhana bersamamu
        punya arti tersendiri.

        <br><br>

        Semoga kita selalu bisa saling mendukung,
        memahami, menghargai, dan tumbuh menjadi
        pribadi yang lebih baik.

        <br><br>

        Jika suatu hari kamu merasa lelah,
        semoga kamu ingat bahwa kamu juga pantas
        mendapatkan hal-hal baik dan kebahagiaan.

        <br><br>

        Terima kasih sudah menjadi bagian
        dari cerita indah ini.

        <br><br>

        With lots of love,

        <br>
        <b>Devaaa ♡</b>
    </div>
    """, unsafe_allow_html=True)

# =========================
# REASONS
# =========================

elif menu == "🌷 Reasons":

    st.title("10 Reasons Why I Love You")
    st.write("A little list, with a lot of love. ♡")

    reasons = [
        "Karena kamu punya cara tersendiri untuk membuatku tersenyum.",
        "Karena aku senang mendengar cerita-ceritamu.",
        "Karena kehadiranmu membuat hari terasa lebih berwarna.",
        "Karena kamu punya keunikan yang tidak tergantikan.",
        "Karena aku bisa belajar banyak hal darimu.",
        "Karena momen sederhana bersamamu terasa berharga.",
        "Karena kamu membuatku ingin menjadi lebih baik.",
        "Karena aku menghargai setiap perhatian kecil darimu.",
        "Karena aku senang bisa menjadi bagian dari ceritamu.",
        "Karena kamu adalah kamu, dan itu sudah istimewa."
    ]

    for i, reason in enumerate(reasons, 1):
        st.markdown(
            f'<div class="reason">🌷 {i}. {reason}</div>',
            unsafe_allow_html=True
        )

# =========================
# PHOTO GALLERY
# =========================

elif menu == "📸 Our Memories":

    st.title("Our Little Memories")
    st.write(
        "Setiap foto punya cerita. "
        "Tambahkan kenangan favorit kalian di sini. ♡"
    )

    st.markdown(
        '<div class="flower">📷 🌼 📷</div>',
        unsafe_allow_html=True
    )

    photos = st.file_uploader(
        "Pilih foto dari iPad kamu",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    if photos:
        st.success(
            f"{len(photos)} foto berhasil dimuat!"
        )

        for i in range(0, len(photos), 2):
            cols = st.columns(2)

            for j, col in enumerate(cols):
                index = i + j

                if index < len(photos):
                    with col:
                        st.image(
                            photos[index],
                            caption=f"Our Memory #{index + 1}",
                            use_container_width=True
                        )

        st.info(
            "Foto yang diunggah di sini hanya tampil "
            "selama sesi aplikasi berlangsung. "
            "Untuk galeri permanen, kita akan menambahkan "
            "file foto ke penyimpanan website secara terpisah."
        )

    else:
        st.info(
            "Belum ada foto. Pilih tombol di atas "
            "untuk menambahkan foto kenangan kalian. 🌷"
        )

# =========================
# SURPRISE
# =========================

elif menu == "🎁 Surprise":

    st.title("A Little Surprise")
    st.markdown(
        '<div class="flower">🎀 🌷 🎀</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Ada pesan kecil yang disiapkan "
        "khusus untuk Rahadian."
    )

    if st.button("Klik untuk membuka kejutan ♡"):

        st.balloons()

        st.markdown("""
        <div class="letter">
            <h2>You're Special! ♡</h2>

            Rahadian, jangan lupa bahagia hari ini.

            <br><br>

            Terima kasih sudah menjadi bagian
            dari cerita Devaaa.

            <br><br>

            Semoga hari-harimu dipenuhi
            hal-hal baik, kebahagiaan,
            dan banyak alasan untuk tersenyum.

            <br><br>

            Sending you flowers! 🌷🌷🌷
        </div>
        """, unsafe_allow_html=True)

# =========================
# FINAL MESSAGE
# =========================

elif menu == "🤍 Final Message":

    st.markdown(
        '<div class="flower">🤍 🌷 🤍</div>',
        unsafe_allow_html=True
    )

    st.title("One Last Thing...")

    st.markdown("""
    <div class="letter">
        Dear Rahadian,

        <br><br>

        Terima kasih sudah meluangkan waktu
        untuk melihat hadiah kecil ini.

        <br><br>

        Website ini dibuat oleh Devaaa
        sebagai salah satu cara sederhana
        untuk menyampaikan rasa sayang.

        <br><br>

        Tidak harus selalu ada hal besar
        untuk membuat sebuah momen menjadi indah.

        <br><br>

        Sometimes, little things mean a lot.

        <br><br>

        Take care of yourself, okay?

        <br><br>

        With love,

        <br>
        <b>Your Devaaa ♡</b>
    </div>
    """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================

st.markdown("---")

st.markdown("""
<div class="flower">🌷 🌼 🌷</div>

<p style="text-align:center; color:#96745E;">
Made with ♡ by Devaaa
<br>
Especially for Rahadian Haryo Argani
<br><br>
A Little Flower for You · 2026
</p>
""", unsafe_allow_html=True)
