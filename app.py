import streamlit as st
from Bio.Seq import Seq

st.set_page_config(
    page_title="AI Bioinformatics Assistance",
    page_icon="🧬"
)

st.title("AI Bioinformatics Assistance")
st.write("Welcome to your bioinformatics application!")

dna = st.text_input("Enter a DNA sequence", "ATGCGCGATAT")

if st.button("Analyze DNA"):
    dna = "".join(dna.split()).upper()

    if not dna:
        st.error("Please enter a DNA sequence.")

    elif any(base not in "ATGC" for base in dna):
        st.error("Invalid DNA. Use only A, T, G, and C.")

    else:
        gc = dna.count("G") + dna.count("C")
        gc_percent = gc / len(dna) * 100

        st.subheader("Analysis Results")
        st.write("Sequence:", dna)
        st.write("Length:", len(dna))
        st.write("f"GC content: {gc_percent:.2f}%")
        st.write("Complement:", str(Seq(dna).complement()))
        st.write(
            "Reverse complement:",
            str(Seq(dna).reverse_complement())
        )
