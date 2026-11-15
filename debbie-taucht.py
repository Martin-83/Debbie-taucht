import streamlit as st
import math

st.title("Debbie taucht. ❤️")
st.write("Diese App ist ein kleines Geschenk für meinen Lieblings-🍑🐟. Sie beinhaltet die wichtigsten theoretischen Punkte zum Thema Nitrox, die man für AN/DP wissen muss.")
st.write("Sie besteht aus einem Rechner, sowie erläuternder Theorie. ")
st.write("Viel Spass! 🎈")

st.divider()

# Rechner-Bereich
st.markdown("### Gas-Berechnungen")

modus = st.radio("Was möchtest du berechnen?", [
                 "Maximum Operation Depth (MOD)", "Best-Mix", "Sauerstoffpartialdruck"], horizontal=True)

if modus == "Maximum Operation Depth (MOD)":
    st.write("""Die MOD gibt dir an, bis zu welcher Tiefe du ein bestimmtes Gas verwenden kannst. 
    Die Grenze wird hierbei durch den zulässigen Sauerstoffpartialdruck p<sub>g</sub> gebildet. 
    Je höher der Sauerstoffanteil f<sub>g</sub> in deinem Gas, umso schneller wird dieser Grenzwert erreicht, d.h. 
    umso weniger tief kannst du mit diesem Gas tauchen.""", unsafe_allow_html=True)

    st.markdown("""
        Typischerweise werden zwei Grenzwerte für den Partialdruck herangezogen:
        - 1.6 bar für die Dekompression
        - 1.4 bar für den eigentlichen Tauchgang
        """)

    st.write("Alles klar? Dann lass uns losrechnen!")

    col1, col2 = st.columns(2)

    with col1:
        partialdruck = st.number_input(
            "Zulässiger Partialdruck (bar):", min_value=0.0, max_value=3.0, value=1.4, step=0.1, format="%.1f")

    with col2:
        sauerstoffanteil = st.number_input(
            "Sauerstoffanteil [-]:", min_value=0.01, max_value=1.0, value=0.21, step=0.01, format="%.2f")

        st.caption(f"entspricht {sauerstoffanteil * 100:.0f}% Sauerstoff")

    umgebungsdruck = partialdruck / sauerstoffanteil
    mod = (umgebungsdruck - 1) * 10
    st.metric("Maximum Operation Depth (MOD):", f"{mod:.1f} m")


elif modus == "Best-Mix":
    st.write('''Mit "Best-Mix" ist gemeint, dass man den für eine bestimmte Zieltiefe optimalen Sauerstoffgehalt und somit 
    das optimale Nitrox wählt. 
    Die Idee dahinter ist die folgende: Wir möchten den Sauerstoffgehalt so hoch wie möglich wählen, denn dadurch ist 
    gleichzeitig der Stickstoffgehalt (der die Nullzeit begrenzt) so tief wie möglich. Der maximal mögliche 
    Sauerstoffgehalt wird hierbei durch den zulässigen Sauerstoffpartialdruck p<sub>g</sub> auf der Zieltiefe begrenzt.''', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        partialdruck = st.number_input("Gewünschter Partialdruck (bar):",
                                       min_value=0.0, max_value=3.0, value=1.4, step=0.1, format="%.1f")

    with col2:
        zieltiefe = st.number_input(
            "Zieltiefe (m):", min_value=0, value=30, step=1)
        st.caption(f"entspricht {(zieltiefe / 10) + 1:.1f} bar Umgebungsdruck")

    best_mix = partialdruck / ((zieltiefe / 10) + 1)
    best_mix_prozent = min(math.floor(round(best_mix * 100, 6)), 100)
    best_mix_dezimal = best_mix_prozent / 100

    st.metric(
        "Optimaler Sauerstoffgehalt:", f"{best_mix_dezimal:.2f} = {best_mix_prozent}%")

    st.caption(f"entspricht Nitrox {best_mix_prozent}")


else:
    st.write("""Grundsätzlich lässt sich natürlich auch für jeden Zeitpunkt des Tauchgangs der aktuell vorliegende 
    Sauerstoffpartialdruck p<sub>g</sub> berechnen. Er ist abhängig vom Sauerstoffanteil im Gas, sowie von der Tiefe
    (bzw. dem vorherrschenden Umgebungsdruck).
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        sauerstoffanteil = st.number_input(
            "Sauerstoffanteil [-]:", min_value=0.0, max_value=1.0, value=0.21, step=0.01, format="%.2f")

        st.caption(f"entspricht {sauerstoffanteil * 100:.0f}% Sauerstoff")

    with col2:
        tiefe = st.number_input("Tiefe [m]:", min_value=0, value=30, step=1)

        st.caption(f"entspricht {(tiefe / 10) + 1:.1f} bar Umgebungsdruck")

    partialdruck = sauerstoffanteil * ((tiefe / 10) + 1)

    st.metric("Sauerstoff-Partialdruck:", f"{partialdruck:.2f} bar")


st.divider()

# Theorie-Bereich
st.markdown("### Theoretischer Hintergrund")
st.write("Du möchtest mehr wissen?")

with st.expander("T-im-Kreis"):
    col1, col2 = st.columns(2)

    with (col1):
        st.markdown("##### T-im-Kreis")
        st.markdown("Für die Berechnungen verwendet man am einfachsten das **T-im-Kreis**. Wie es der Name schon sagt, zeichnet man ein T in einem Kreis. Danach fügt man die Formelzeichen ein. ")
        st.html("<br>")
        st.markdown("Diese sind:")

    with (col2):
        st.image("t-im-kreis.png", use_container_width=True)

    with (col1):
        st.markdown("- p<sub>g</sub> = Partialdruck des Gases (bar)",
                    unsafe_allow_html=True)
        st.markdown(
            "- f<sub>g</sub> = Anteil des Gases (Dezimalbruch)", unsafe_allow_html=True)
        st.markdown("- p = Umgebungsdruck (bar)", unsafe_allow_html=True)

    with (col2):
        st.info('''**Eselsbrücke:**   
        ":orange[**P**]anzer:orange[**g**]renadiere :orange[**f**]ahren :orange[**g**]erne :orange[**P**]anzer."
        ''')

    st.markdown("##### Und wie verwendet man das Ganze nun?")
    st.write("Im Prinzip ist es ganz einfach: Die gesuchte Grösse deckst du mit deinem Finger ab, dann ergibt sich eine Formel. Der horizontale Strich entspricht hierbei einer Division, der vertikale einer Multiplikation.")
    st.write("Machen wir ein paar Beispiele: Möchtest du z.B. den Partialdruck p<sub>g</sub> wissen, so deckst du diesen ab. Daraus resultiert die Formel f<sub>g</sub> x p. Möchtest du den Umgebungsdruck wissen, deckst du p ab. Dann erhältst du p<sub>g</sub> / f<sub>g</sub>.", unsafe_allow_html=True)


# Beispiel 1: MOD
with st.expander("Beispiel 1: Maximum Operation Depth (MOD)"):
    st.markdown("""Du planst ein Nitrox 50 als Dekogas zu verwenden und möchtest die maximal mögliche Tiefe (MOD) wissen, 
    in der du es verwenden darfst.""")

    st.markdown("""
    **Gegeben:**
    - p<sub>g</sub> = zulässiger Sauerstoffpartialdruck = 1.6 bar (weil Dekompression)
    - f<sub>g</sub> = Sauerstoffanteil = 0.50 (50%)

    **Gesucht:**
    - Tauchtiefe.
    - Gemäss T-im-Kreis gibt es die Tauchtiefe nicht direkt, aber man kann sie aus dem Umgebungsdruck p ableiten → Tiefe = (p - 1 bar) x 10 m/bar.
    - Gesucht ist somit zunächst der Umgebungsdruck p und dann erst die Tauchtiefe.
    """, unsafe_allow_html=True)

    st.markdown("""
    **Lösung:**
    
    Über T-im-Kreis kannst du die Formel für den Umgebungsdruck p ausfindig machen (hierzu p abdecken) und die Zahlen einsetzen: 

    p = p<sub>g</sub> / f<sub>g</sub> = 1.6 bar / 0.50 = **3.2 bar**

    Tauchtiefe = (p - 1 bar) x 10 m/bar = (3.2 bar - 1 bar) x 10 m/bar = **22 m**
    """, unsafe_allow_html=True)

# Beispiel 2: Best-Mix
with st.expander("Beispiel 2: Best-Mix"):
    st.markdown("""Du planst einen Tauchgang auf 40 m und möchtest wissen, mit welchem Nitrox du die längste Nullzeit 
    bekommst. Dies ist dann der Fall, wenn der Sauerstoffgehalt so hoch wie möglich ist, also wenn der Sauerstoffpartialdruck
    p<sub>g</sub> gerade eingehalten ist. Denn ein maximal möglicher Sauerstoffgehalt entspricht einem minimal möglichen
    Stickstoffgehalt und Letzterer begrenzt ja die Nullzeit.""", unsafe_allow_html=True)

    st.markdown("""
    **Gegeben:**
    - p<sub>g</sub> = zulässiger Sauerstoffpartialdruck = 1.4 bar (weil eigentlicher Tauchgang)
    - p = Umgebungsdruck = 5 bar → ergibt sich aus Umrechnung: (40 m / 10) + 1 bar
    """, unsafe_allow_html=True)

    st.markdown("""
    **Gesucht:**
    - f<sub>g</sub> = optimaler Sauerstoffanteil
    """, unsafe_allow_html=True)

    st.markdown("""
    **Lösung:**

    Über T-im-Kreis kannst du die Formel für den Sauerstoffanteil f<sub>g</sub> ausfindig machen (hierzu f<sub>g</sub> abdecken) 
    und die Zahlen einsetzen:

    f<sub>g</sub> = p<sub>g</sub> / p = 1.4 bar / 5 bar = **0.28 = 28% Sauerstoff** (entspricht Nitrox 28)
    """, unsafe_allow_html=True)

# Beispiel 3: Sauerstoffpartialdruck
with st.expander("Beispiel 3: Sauerstoffpartialdruck"):
    st.markdown("""Du befindest dich auf 30 m und hast Luft in deiner Flasche. Da der Tauchgang gerade etwas langweilig ist,
    möchtest du dich mit einer kleinen Kopfrechenaufgabe fordern und beschliesst, den momentan vorherrschenden Sauerstoffpartialdruck
    zu berechnen.""")

    st.markdown("""
    **Gegeben:**
    - f<sub>g</sub> = Sauerstoffanteil = 0.21 (21%)
    - p = Umgebungsdruck = 4 bar → ergibt sich aus Umrechnung: (30 m / 10) + 1 bar    
    """, unsafe_allow_html=True)

    st.markdown("""
    **Gesucht:**
    - p<sub>g</sub> = aktueller Sauerstoffpartialdruck
    """, unsafe_allow_html=True)

    st.markdown("""
    **Lösung:**

    Über T-im-Kreis kannst du die Formel für den Sauerstoffpartialdruck p<sub>g</sub> ausfindig machen (hierzu 
    p<sub>g</sub> abdecken) und die Zahlen einsetzen:

    p<sub>g</sub> = f<sub>g</sub> x p = 0.21 x 4 bar = **0.84 bar**
    """, unsafe_allow_html=True)

st.write("Alles klar?")
button = st.button("Ja!")
if button:
    st.balloons()

st.divider()
st.caption("Erstellt von Martin mit ❤️ · 15.11.2026")
