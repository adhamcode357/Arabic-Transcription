import streamlit as st 

# =========================
# IMPORT YOUR CLASSES
# =========================
from arabic import ArabicTranscription
from EDialect import EgyDialect
from GDialect import GulfDialect
from IrDialect import IraqiDialect
from LDialect import LevDialect
from MagDialect import MaghrebiDialect
from morphological import Morphological
from active import ActiveParticiple

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Arabic Transcription System",
    page_icon="🧠",
    layout="wide"
)

# =========================
# STYLE
# =========================
st.markdown("""
<style>
.big-title {
    font-size: 40px;
    font-weight: bold;
    color: #1f77b4;
}
.result-box {
    background-color: #111;
    color: #00ffcc;
    padding: 15px;
    border-radius: 10px;
    font-size: 20px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# INIT OBJECTS
# =========================
at = ArabicTranscription()

dialects = {
    "MSA ": at,
    "Egyptian 🇪🇬": EgyDialect(),
    "Gulf 🇸🇦": GulfDialect(),
    "Iraqi 🇮🇶": IraqiDialect(),
    "Levantine 🇸🇾": LevDialect(),
    "Maghrebi 🇲🇦": MaghrebiDialect()
}

morph = Morphological(at)
active = ActiveParticiple(at)

# =========================
# HEADER
# =========================
st.markdown('<div class="big-title">🧠 Arabic Transcription Platform</div>', unsafe_allow_html=True)
st.write("Convert Arabic text into IPA + analyze morphology + verb transformation")

# =========================
# TABS
# =========================
tab1, tab2, tab3 = st.tabs([
    "🔤 Transcription",
    "🧩 Morphological Analysis",
    "⚙️ Verb → Active Participle"
])

# =========================
# TAB 1: TRANSCRIPTION
# =========================
with tab1:
    st.subheader("Arabic → IPA")

    text = st.text_input("Enter Arabic word")

    dialect_name = st.selectbox("Choose Dialect", list(dialects.keys()))

    if st.button("Transcribe"):
        if text:
            engine = dialects[dialect_name]

            try:
                result = engine.transcribe(text)
                st.markdown(f'<div class="result-box">/{result}/</div>', unsafe_allow_html=True)
            except:
                st.error("Error during transcription")

# =========================
# TAB 2: MORPHOLOGY
# =========================
with tab2:
    st.subheader("Morphological Analysis")

    word = st.text_input("Enter word for morphology", key="morph")

    if st.button("Analyze"):
        if word:
            result = morph.transcribe_morph(word)
            st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

# =========================
# TAB 3: ACTIVE PARTICIPLE
# =========================
with tab3:
    st.subheader("Verb → Active Participle")

    verb = st.text_input("Enter verb", key="verb")

    if st.button("Convert"):
        if verb:
            result = active.transcribe_word(verb)
            st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.write("---")
st.caption("Made for Arabic NLP 🔥")