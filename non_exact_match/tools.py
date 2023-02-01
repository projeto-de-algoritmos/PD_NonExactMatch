from string import punctuation
import re


def string_normalize(string):
    string = string.lower()
    string = string.replace("\n", "")
    string = re.sub(' +', ' ', string)
    string = ' '.join(word.strip(punctuation) for word in string.split())
    return string


def generate_ngrams(text,ngram=1):
    words = [word for word in string_normalize(text).split(" ")]
    temp = zip(*[words[i:] for i in range(0, ngram)])
    ngrams_result = [" ".join(ngram) for ngram in temp]
    return ngrams_result