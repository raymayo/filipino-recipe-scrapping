def partial_match(word, sentence):
    return word in sentence


def match_words(sentence, word_array):
    matching_words = []
    for word in word_array:
        if partial_match(word, sentence):
            matching_words.append(word)
    return matching_words


sentence = "I like mangoes."

word_array = ["mango", "banana"]
result = match_words(
    sentence.lower(), word_array
)  # Convert to lowercase for case-insensitive matching
print(result)
