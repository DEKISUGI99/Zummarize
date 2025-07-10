from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = ""
    for chunk in chunks:
        out = summarizer(chunk, max_length=150, min_length=40, do_sample=False)
        summary += out[0]["summary_text"] + " "
    return summary.strip()

# from transformers import pipeline
# from sklearn.feature_extraction.text import CountVectorizer
# import numpy as np
# import nltk
# import re

# nltk.download('punkt')
# from nltk.tokenize import sent_tokenize

# # Load the summarizer (change model if needed)
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# def chunk_text(text, max_words=500):
#     """Split text into chunks of max_words tokens (approx)."""
#     sentences = sent_tokenize(text)
#     chunks = []
#     current_chunk = []

#     word_count = 0
#     for sentence in sentences:
#         words = sentence.split()
#         word_count += len(words)
#         current_chunk.append(sentence)

#         if word_count >= max_words:
#             chunks.append(" ".join(current_chunk))
#             current_chunk = []
#             word_count = 0

#     if current_chunk:
#         chunks.append(" ".join(current_chunk))

#     return chunks

# def summarize_chunk(chunk):
#     """Summarize a single chunk of text."""
#     return summarizer(chunk, max_length=150, min_length=40, do_sample=False)[0]['summary_text']

# def extract_topics(texts, top_k=5):
#     """Extract keywords/topics from multiple summaries using TF-based approach."""
#     vectorizer = CountVectorizer(stop_words='english', max_features=1000)
#     X = vectorizer.fit_transform(texts)
#     summed = np.array(X.sum(axis=0)).flatten()
#     keywords = np.array(vectorizer.get_feature_names_out())[summed.argsort()[::-1]]
#     return keywords[:top_k]

# def generate_final_summary(all_summaries, topics):
#     """Generate final merged summary based on extracted topics."""
#     prompt = "Write a detailed summary covering the following topics:\n"
#     prompt += ", ".join(topics) + ".\n\n"
#     prompt += "Here are partial summaries:\n\n"
#     prompt += "\n\n".join(all_summaries)

#     # You can swap in GPT here if needed
#     final = summarizer(prompt, max_length=300, min_length=100, do_sample=False)
#     return final[0]['summary_text']

# def summarize_text(full_transcript):
#     """Main function: takes a long transcript and produces a smart summary."""
#     chunks = chunk_text(full_transcript)
#     chunk_summaries = [summarize_chunk(chunk) for chunk in chunks]

#     topics = extract_topics(chunk_summaries)
#     final_summary = generate_final_summary(chunk_summaries, topics)

#     return final_summary
