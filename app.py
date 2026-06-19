import streamlit as st
import openai
import json

st.set_page_config(page_title="eBay Titel Optimierer")
st.title("eBay Titel Optimierer")
st.write("Gib deinen eBay-Titel und die Beschreibung ein - und die KI optimiert sie für dich!")

API_KEY = "DEINEN_API_KEY_HIER_EINFÜGEN"

title = st.text_input("Aktueller Titel")
desc = st.text_area("Aktuelle Beschreibung")
if st.button("Optimieren!"):
    if not title or not desc:
        st.warning("Bitte fülle beide Felder aus!")
    else:
        with st.spinner("KI denkt nach..."):
            client = openai.OpenAI(api_key=API_KEY)
            prompt = f"""
            Optimiere diesen eBay-Artikel:
            Titel: {title}
            Beschreibung: {desc}
            Gib mir:
            1. 3 neue Titel
            2. Neue Beschreibung
            3. Preisempfehlung in EUR
            Antwort als JSON:
            {{"titles": ["Titel1", "Titel2", "Titel3"], "new_description": "...", "price_recommendation": 49.99}}
            """
            antwort = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            ergebnis = json.loads(antwort.choices[0].message.content)
            st.success("Optimierung erfolgreich!")
            st.subheader("Neue Titel:")
            for i, t in enumerate(ergebnis["titles"], 1):
                st.write(f"{i}. {t}")
            st.subheader("Neue Beschreibung:")
            st.write(ergebnis["new_description"])
            st.subheader(f"Preisempfehlung: {ergebnis['price_recommendation']} EUR")
