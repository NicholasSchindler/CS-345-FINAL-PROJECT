import csv
import re
from collections import Counter

def load_and_split_csv(filename):
    ham_data = []
    spam_data = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            label, text = row[0].strip().lower(), row[1].strip()
            if "ham" in label:
                ham_data.append(text)
            elif "spam" in label:
                spam_data.append(text)
    return ham_data, spam_data

def parse_word_frequencies(text_list):
    word_counter = Counter()
    for text in text_list:
        words = re.findall(r"\b\w+\b", text.lower())
        word_counter.update(words)
    return dict(word_counter)


##### Main #####

# Loads the csv and splits it into a ham dataset and a spam dataset.
ham, spam = load_and_split_csv("spam.csv")

# Get the number of ham and the number of spam messages so we can adjust for frequency.
ham_size = len(ham)
spam_size = len(spam)

# Counts the frequency of each word in ham and spam datasets. The first column is the word, and the second is the count.
# Converts everything to lower case so capitalization does not matter.
ham_parsed = parse_word_frequencies(ham)
spam_parsed = parse_word_frequencies(spam)