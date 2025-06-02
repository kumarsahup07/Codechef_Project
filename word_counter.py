import re

def read_input_file(filename):
    """Reads text from a file and returns it as a string."""
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""

def display_results(total_words, search_word, word_frequency):
    """Displays total word count and frequency of the searched word."""
    print(f"\nTotal Words: {total_words}")
    print(f"Frequency of '{search_word}': {word_frequency}")

def count_words_regex(text):
    """Uses regex to extract words (ignores punctuation)."""
    return re.findall(r'\b\w+\b', text)

def word_frequency(words):
    """Prompts user for a word and counts its frequency (case-insensitive)."""
    search_word = input("Enter the word to search: ").strip().lower()
    word_freq = words.count(search_word)
    return word_freq, search_word

if __name__ == "__main__":
    filename = input("Enter the path to the input text file: ").strip()  # Example: input.txt
    text = read_input_file(filename)

    if text:
        words = count_words_regex(text)
        total_words = len(words)

        # Convert all words to lowercase for case-insensitive matching
        words_lower = [word.lower() for word in words]

        word_freq, search_word = word_frequency(words_lower)
        display_results(total_words, search_word, word_freq)