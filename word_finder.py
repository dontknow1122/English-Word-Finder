import itertools

def load_words(file_path):
    with open(file_path, 'r') as file:
        loaded_words = set(file.read().split())
    return loaded_words

#find word combinations
def find_combinations(letters, words_set, word_size=None):
    possible_combinations = set()
    for i in range(1, len(letters)+1):
        if word_size and i != word_size:
            continue
        for combo in itertools.permutations(letters, i):
            word = ''.join(combo)
            if word in words_set:
                possible_combinations.add(word)
    return possible_combinations

if __name__ == "__main__":
    # Load the list of words
    words_file_path = 'words.txt'
    words_set = load_words(words_file_path)

    while True:
        # Get user input for letters
        input_letters = input("Enter the letters to combine (without spaces): ").lower()

        word_size = input("Enter the word size (optional, press enter to skip): ").strip()
        word_size = int(word_size) if word_size.isdigit() else None

        found_words = find_combinations(input_letters, words_set, word_size)
        print("\n"f"{' - '.join(found_words)}""\n")
