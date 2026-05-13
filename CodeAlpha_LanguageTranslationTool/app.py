import streamlit as st
from deep_translator import GoogleTranslator

# PAGE CONFIG
st.set_page_config(
    page_title="Awanish's Language Translation | CodeAlpha",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

body {
    background-color: #f8f9fa;
}

.main {
    background-color: #f8f9fa;
}

.title {
    font-size: 34px;
    font-weight: 600;
    color: #1a73e8;
    text-align: left;
    margin-top: 10px;
    margin-bottom: 30px;
    font-family: Arial, sans-serif;
}



.stTextArea textarea {
    font-size: 18px !important;
    border-radius: 10px !important;
    border: 1px solid #dcdcdc !important;
    min-height: 220px !important;
    padding: 14px !important;
}

.stSelectbox div[data-baseweb="select"] {
    border-radius: 10px !important;
}

.stButton button {
    background-color: #1a73e8;
    color: white;
    border: none;
    border-radius: 8px;
    height: 48px;
    width: 180px;
    font-size: 17px;
    font-weight: 500;
    transition: 0.3s;
}

.stButton button:hover {
    background-color: #1558b0;
    color: white;
}

.footer {
    text-align: center;
    margin-top: 30px;
    color: gray;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown(
    "<div class='title'>Awanish's Language Translation | CodeAplha</div>",
    unsafe_allow_html=True
)

# LANGUAGE OPTIONS
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Russian": "ru",
    "Arabic": "ar",
    "Urdu" : "ur",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Odia": "or",
    "Sanskrit": "sa",
    "Nepali": "ne",
    "Korean": "ko",
    "Thai": "th",
    "Turkish": "tr",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Greek": "el",
    "Polish": "pl",
    "Swedish": "sv",
    "Finnish": "fi",
    "Danish": "da",
    "Norwegian": "no",
    "Hebrew": "iw",
    "Indonesian": "id",
    "Malay": "ms",
    "Vietnamese": "vi",
    "Ukrainian": "uk",
    "Persian": "fa",
    "Romanian": "ro",
    "Hungarian": "hu",
    "Czech": "cs",
    "Slovak": "sk",
    "Bulgarian": "bg",
    "Croatian": "hr",
    "Serbian": "sr",
    "Slovenian": "sl",
    "Lithuanian": "lt",
    "Latvian": "lv",
    "Estonian": "et",
    "Filipino": "tl",
    "Swahili": "sw",
    "Afrikaans": "af",
    "Irish": "ga",
    "Welsh": "cy",
    "Albanian": "sq",
    "Georgian": "ka",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Basque": "eu",
    "Belarusian": "be",
    "Catalan": "ca",
    "Esperanto": "eo",
    "Haitian Creole": "ht",
    "Icelandic": "is",
    "Latin": "la",
    "Macedonian": "mk",
    "Mongolian": "mn",
    "Sinhala": "si",
    "Zulu": "zu"
}

# MAIN BOX
st.markdown("<div class='translation-box'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("From", list(languages.keys()))
    text = st.text_area("Enter Text")

with col2:
    target_lang = st.selectbox("To", list(languages.keys()))
    translated_placeholder = st.empty()

st.write("")

# BUTTON CENTER
colbtn1, colbtn2, colbtn3 = st.columns([2,1,2])

with colbtn2:
    translate = st.button("Translate")

# TRANSLATION
if translate:

    if text.strip() != "":

        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        with col2:
            translated_placeholder.text_area(
                "Translated Text",
                translated,
                height=220
            )

    else:
        st.warning("Please enter text to translate.")

st.markdown("</div>", unsafe_allow_html=True)

# FOOTER
st.markdown(
    "<div class='footer'>Developed by Awanish • CodeAlpha AI Internship</div>",
    unsafe_allow_html=True
)