import streamlit as st
import re
from collections import Counter
import pandas as pd

st.title("Tokenizer App")
st.write("This app tokenizes your text and shows: number of tokens, list of tokens, and most frequent tokens.")

# User input
text = st.text_area("Enter your text here:", height=300)

if st.button("Tokenize"):
    if text.strip() == "":
        st.warning("Please enter some text!")
    else:
        # ---------------------
        # TOKENIZATION (Regex)
        # ---------------------
        # Extract words only (ignore punctuation)
        tokens = re.findall(r"\b\w+\b", text.lower())

        # ---------------------
        # 1️⃣ Number of tokens
        # ---------------------
        st.subheader("1️⃣ Number of Tokens")
        st.write(len(tokens))

        # ---------------------
        # 2️⃣ List of tokens
        # ---------------------
        st.subheader("2️⃣ List of Tokens")
        st.markdown(" ".join([f"`{t}`" for t in tokens]))
        # print(" ".join([f"`{t}`" for t in tokens]))

        # ---------------------
        # 3️⃣ Most Frequent Tokens
        # ---------------------
        st.subheader("3️⃣ Most Frequent Tokens")

        freq = Counter(tokens).most_common()  # Top 5

        # Clean table format
        df = pd.DataFrame(freq, columns=["Token", "Frequency"])
        st.dataframe(df)

        st.success("Tokenization complete!")
