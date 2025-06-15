import nltk
from textminer import summarize_text

with open("Some_News.txt", mode='r', encoding='utf-8') as f:
    Text_data = f.read()

sample_text = "Machine learning is a field of computer science that gives computers the ability to learn without being explicitly programmed."

with open("Summarized_News.txt", mode='w', encoding='utf-8') as f:
    f.write(summarize_text(Text_data))