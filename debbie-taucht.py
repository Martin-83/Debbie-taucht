import streamlit as st

st.title("Debbie taucht. ❤️")
st.write("Diese App ist ein kleines Geschenk für meinen lieblings 🍑🐟. Sie beinhaltet die wichtigsten theoretischen Punkte, die man für AN/DP wissen muss.")
st.write("Sie besteht aus einem Rechner, sowie erläuternder Theorie. ")
st.write("Viel Spass! 🎈")

st.divider()

# Rechner-Bereich
st.markdown("### Gas-Berechnungen")
modus = st.radio("Was möchtest du berechnen?", ["Maximum Operation Depth (MOD)", "Best-Mix", "Partialdruck eines Gases"], horizontal=True)

if modus == "Maximum Operation Depth (MOD)":
    st.write("Die MOD gibt dir an, bis zu welcher Tiefe du ein bestimmtes Gas verwenden kannst. Die Grenze wird hierbei durch den zulässigen Sauerstoffpartialdruck p<sub>g</sub> gebildet. Je höher der Sauerstoffanteil f<sub>g</sub> in deinem Gas, umso schneller wird der Grenzwert erreicht. ", unsafe_allow_html=True)
    st.write("Typischerweise werden zwei Grenzwerte für den Partialdruck herangezogen:")
    st.write("- 1.6 Bar für die Dekompression")
    st.write("- 1.4 Bar für den eigentlichen Tauchgang")
    st.write("Alles klar? Dann lass uns losrechnen!")

elif modus == "Best-Mix":
    st.write("Text und Rechner für den Best-Mix")
else:
    st.write("Text und Rechner für den Partialdruck")







st.divider()
# Theorie-Bereich
st.markdown("### Theoretischer Hintergrund")
st.write("Du möchtest mehr wissen?")

with st.expander("T-im-Kreis"):
    col1, col2 = st.columns(2)

    with(col1):
        st.markdown("##### T-im-Kreis")
        st.markdown("Für die Berechnungen verwendet man am einfachsten das **T-im-Kreis**. Wie es der Name schon sagt, zeichnet man ein T in einem Kreis. Danach fügt man die Formelzeichen ein. ")
        st.html("<br>")
        st.markdown("Diese sind:")
        
    with(col2):
        st.image("t-im-kreis.png", use_container_width=True)

    with(col1):
        st.markdown("- p<sub>g</sub> = Partialdruck des Gases (bar)", unsafe_allow_html=True)
        st.markdown("- f<sub>g</sub> = Anteil des Gases (Dezimalbruch)", unsafe_allow_html=True)
        st.markdown("- p = Umgebungsdruck (bar)", unsafe_allow_html=True)
    
    with(col2):
        st.info('''**Eselsbrücke:**   
        ":orange[**P**]anzer:orange[**g**]renadiere :orange[**f**]ahren :orange[**g**]erne :orange[**P**]anzer."
        ''')

    
    st.markdown("##### Und wie verwendet man das Ganze nun?")
    st.write("Im Prinzip ist es ganz einfach: Die gesuchte Grösse deckst du mit deinem Finger ab, dann ergibt sich eine Formel. Der horizontale Strich entspricht hierbei einer Division, der vertikale einer Multiplikation.")
    st.write("Machen wir ein paar Beispiele: Möchtest du z.B. den Partialdruck p<sub>g</sub> wissen, so deckst du diesen ab. Daraus resultiert die Formel f<sub>g</sub> x p. Möchtest du den Umgebungsdruck wissen, deckst du p ab. Dann erhältst du p<sub>g</sub> / f<sub>g</sub>.", unsafe_allow_html=True)

    
with st.expander("Beispiel 1: Maximum Operation Depth (MOD)"):     
    st.markdown("Du planst ein Nitrox 50 als Dekogas zu verwenden und möchtest die maximal mögliche Tiefe (MOD) wissen, in der du es verwenden darfst.")

st.write("Alles klar?")
button = st.button("Ja!")
if button:
    st.balloons()


st.divider()
st.caption("Erstellt von Martin mit ❤️ · 13.11.2026")
