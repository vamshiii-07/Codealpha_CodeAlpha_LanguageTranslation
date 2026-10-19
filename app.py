
import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍"
)

st.title("🌍 AI Language Translation Tool")
st.write("Translate text into different languages.")

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "French": "fr",
    "Spanish": "es"
}

text = st.text_area("Enter your text:")

source = st.selectbox(
    "Translate from:",
    list(languages.keys())
)

target = st.selectbox(
    "Translate to:",
    list(languages.keys()),
    index=1
)

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text.")
    elif source == target:
        st.warning("Choose different languages.")
    else:
        try:
            result = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.subheader("Translated Text")
            st.text_area("Result", value=result)

        except Exception:
            st.error(
                "Translation failed. Please check your internet."
            )

