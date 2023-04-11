import string
def get_etaoin_shrdlu_score(text):
    # Define the expected frequency distribution of letters in English text
    freq_dist = {'e': 12.7, 't': 9.1, 'a': 8.2, 'o': 7.5, 'i': 7.0, 'n': 6.7, 's': 6.3, 'h': 6.1, 'r': 6.0, 'd': 4.3, 'l': 4.0, 'u': 2.8, 'c': 2.8, 'm': 2.4, 'w': 2.4, 'f': 2.2, 'g': 2.0, 'y': 2.0, 'p': 1.9, 'b': 1.5, 'v': 1.0, 'k': 0.8, 'j': 0.2, 'x': 0.2, 'q': 0.1, 'z': 0.1}
    
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    
    # Count the frequency of each letter in the text
    letter_counts = {letter: text.count(letter) for letter in freq_dist.keys()}
    
    # Calculate the score based on the difference between the expected and actual frequency of each letter
    score = sum([abs(freq_dist[letter] - letter_counts[letter]) for letter in freq_dist.keys()])
    
    return score
