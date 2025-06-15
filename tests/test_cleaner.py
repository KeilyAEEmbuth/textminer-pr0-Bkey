import nltk
from textminer import remove_stopwords

sample_text = "Machine learning is a field of computer science that gives computers the ability to learn without being explicitly programmed."

print("🧹 불용어 제거:")
print(remove_stopwords(sample_text))