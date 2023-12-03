def is_exact_word_present(sentence, word):
    # Split the sentence into words
    words = sentence.split()

    # Check if the exact word is present
    return any(word.lower() == w.lower() for w in words)

# Example usage
sentence = "This is a sample sentence with exact words."
word_to_check = "ex"

if is_exact_word_present(sentence, word_to_check):
    print(f"The exact word '{word_to_check}' is present in the sentence.")
else:
    print(f"The exact word '{word_to_check}' is not present in the sentence.")
