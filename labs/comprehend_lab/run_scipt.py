# app.py

import streamlit as st
import boto3

# Set up AWS Comprehend client
comprehend = boto3.client('comprehend', region_name='us-east-1')

st.set_page_config(page_title="Amazon Comprehend NLP Lab", layout="wide")

st.title("🔍 Amazon Comprehend NLP Analyzer")

# Text input
text_input = st.text_area("Enter some text to analyze:", height=200)

if st.button("Analyze with Amazon Comprehend") and text_input.strip():
    with st.spinner("Analyzing..."):
        # Detect language
        lang_response = comprehend.detect_dominant_language(Text=text_input)
        language_code = lang_response['Languages'][0]['LanguageCode']

        st.subheader("Detected Language")
        st.write(f"**Language Code:** {language_code}")

        # Sentiment analysis
        sentiment = comprehend.detect_sentiment(Text=text_input, LanguageCode=language_code)
        st.subheader("Sentiment Analysis")
        st.write(f"**Sentiment:** {sentiment['Sentiment']}")
        st.json(sentiment['SentimentScore'])

        # Entity recognition
        entities = comprehend.detect_entities(Text=text_input, LanguageCode=language_code)
        st.subheader("Entities Detected")
        for ent in entities['Entities']:
            st.write(f"- **{ent['Text']}** ({ent['Type']}) – Confidence: {ent['Score']:.2f}")

        # Key phrase extraction
        key_phrases = comprehend.detect_key_phrases(Text=text_input, LanguageCode=language_code)
        st.subheader("Key Phrases")
        for phrase in key_phrases['KeyPhrases']:
            st.write(f"- {phrase['Text']} (Confidence: {phrase['Score']:.2f})")
