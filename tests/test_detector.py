from textminer import (
    extract_keywords,
    detect_language
)

sample_text = "Machine learning is a field of computer science that gives computers the ability to learn without being explicitly programmed."

print(extract_keywords(sample_text))
print(detect_language(sample_text))