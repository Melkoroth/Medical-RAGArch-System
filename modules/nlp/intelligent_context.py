
# Inteligencia Contextual con Transformers, LangDetect y NLTK

from langdetect import detect
from transformers import pipeline
import nltk
nltk.download('punkt')

class IntelligentContext:
    def __init__(self, text):
        self.text = text

    def detect_language(self):
        return detect(self.text)

    def summarize_text(self):
        summarizer = pipeline('summarization')
        summary = summarizer(self.text, max_length=150, min_length=50, do_sample=False)
        return summary[0]['summary_text']

    def extract_keywords(self):
        tokens = nltk.word_tokenize(self.text)
        keywords = [word for word in tokens if word.isalpha()]
        return keywords
