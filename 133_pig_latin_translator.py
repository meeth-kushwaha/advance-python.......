"""
Project 133: Pig Latin Translator
Concepts: string manipulation, string slicing, punctuation preservation.
"""
import re

VOWELS = "aeiouAEIOU"

def word_to_pig_latin(word):
    if not word.isalpha():
        return word
    is_cap = word[0].isupper()
    w = word.lower()
    
    if w[0] in VOWELS:
        res = w + "way"
    else:
        first_vowel_idx = -1
        for idx, ch in enumerate(w):
            if ch in VOWELS:
                first_vowel_idx = idx
                break
        if first_vowel_idx == -1:
            res = w + "ay"
        else:
            res = w[first_vowel_idx:] + w[:first_vowel_idx] + "ay"
            
    return res.capitalize() if is_cap else res

def translate_sentence(sentence):
    tokens = re.findall(r"\w+|[^\w\s]|\s+", sentence)
    result = []
    for token in tokens:
        if token.isalpha():
            result.append(word_to_pig_latin(token))
        else:
            result.append(token)
    return "".join(result)

def main():
    print("=== PIG LATIN TRANSLATOR ===")
    while True:
        phrase = input("\nEnter English phrase (or 'exit'): ").strip()
        if phrase.lower() == 'exit': break
        print(f"🐷 Pig Latin: {translate_sentence(phrase)}")

if __name__ == "__main__":
    main()
