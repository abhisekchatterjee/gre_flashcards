import streamlit as st
import pandas as pd
import random

def extract_words_from_csv(csv_file):
    # Assuming CSV file has columns 'word', 'definition', 'part of speech', and 'example'
    df = pd.read_csv(csv_file)
    words_and_meanings = [(row['word'], row['definition'], row['part of speech'], row['example']) for _, row in df.iterrows()]
    return words_and_meanings

csv_file = "examples.csv"  # Update with your CSV file path
words_and_meanings = extract_words_from_csv(csv_file)

# def flashcards(words_and_meanings):
#     if 'word_index' not in st.session_state:
#         st.session_state.word_index = 0

#     word, meaning, part_of_speech, example = words_and_meanings[st.session_state.word_index]

#     st.markdown("<h1 style='text-align: center;'>GRE Flashcards</h1>", unsafe_allow_html=True)
#     st.markdown("<h2 style='text-align: center; font-family: serif;'>Word: {}</h2>".format(word), unsafe_allow_html=True)
#     st.markdown("<h3 style='text-align: center; font-family: serif;'>Part of Speech: {}</h3>".format(part_of_speech), unsafe_allow_html=True)
#     # st.markdown("<p style='text-align: center; font-family: serif;'>Definition: {}</p>".format(meaning), unsafe_allow_html=True)
#     # st.markdown("<p style='text-align: center; font-family: serif;'>Example: {}</p>".format(example), unsafe_allow_html=True)

#     col1, col2, col3 = st.columns([1, 8, 1])
#     with col1:
#         st.write("")  # Empty column for spacing

#     with col2:
#         if st.button("Flip"):
#             st.markdown("<h2 style='text-align: center; font-family: serif;'>{}</h2>".format(meaning), unsafe_allow_html=True)
#             st.markdown("<p style='text-align: center; font-family: serif;'>Example: {}</p>".format(example), unsafe_allow_html=True)

#     with col3:
#         if st.button("Next"):
#             st.session_state.word_index = (st.session_state.word_index + 1) % len(words_and_meanings)  # Move to next word
#             st.experimental_rerun()

def flashcards(words_and_meanings):
    if 'word_index' not in st.session_state:
        st.session_state.word_index = random.randint(0, len(words_and_meanings) - 1)

    word, meaning, part_of_speech, example = words_and_meanings[st.session_state.word_index]

    st.markdown("<h1 style='text-align: center;'>GRE Flashcards</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-family: serif;'>Word: {}</h2>".format(word), unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-family: serif;'>Part of Speech: {}</h3>".format(part_of_speech), unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 8, 1])
    with col1:
        st.write("")  # Empty column for spacing

    with col2:
        if st.button("Flip"):
            st.markdown("<h2 style='text-align: center; font-family: serif;'>{}</h2>".format(meaning), unsafe_allow_html=True)
            if str(example).lower() == 'na':
                st.markdown("<p style='text-align: center; font-family: serif;'>Example: Not Available</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p style='text-align: center; font-family: serif;'>Example: {}</p>".format(example), unsafe_allow_html=True)

    with col3:
        if st.button("Next"):
            st.session_state.word_index = random.randint(0, len(words_and_meanings) - 1)
            st.experimental_rerun()

def main():
    flashcards(words_and_meanings)

if __name__ == "__main__":
    main()
