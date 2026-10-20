
            
import streamlit as st
import requests

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

source = st.selectbox("Translate from:", list(languages.keys()))
target = st.selectbox(
    "Translate to:", list(languages.keys()), index=1
)

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text.")
    elif source == target:
        st.warning("Choose different languages.")
    else:
        try:
            response = requests.get(
                "https://api.mymemory.translated.net/get",
                params={
                    "q": text,
                    "langpair": (
                        f"{languages[source]}|{languages[target]}"
                    )
                },
                timeout=20
            )
            response.raise_for_status()
            data = response.json()

            if data.get("responseStatus") == 200:
                result = data["responseData"]["translatedText"]
                st.subheader("Translated Text")
                st.text_area("Result", value=result)
            else:
                st.error(
                    "Translation service limit reached "
                    "or request failed. Please try later."
                )

        except requests.RequestException:
            st.error(
                "Network error. Please try again later."
            )
        except (KeyError, ValueError):
            st.error("Unexpected translation response.")


        
    
            
            
            

