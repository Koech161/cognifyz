from collections import Counter
import string
def count_word(file_path):
    with open(file_path,"r") as file:
        text = file.read().lower()

        text = text.translate(str.maketrans('','',string.punctuation))
        words = text.split()
        words_count = Counter(words)

        for word, count in sorted(words_count.items()):
            print(f'{word}: {count}')

file_path = input('Enter file_path : ')
count_word(file_path)