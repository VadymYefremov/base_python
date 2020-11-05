""" For word processing techniques """
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import util_nl as ut


def token_file():
    """ performs tokenize words & sentences
    used in file util_nl.py argument '--a' """
    print(len(sent_tokenize(ut.data_read)))
    print(len(word_tokenize(ut.data_read)))


def lemm_file():
    """ performs lemmatize words
     used in file util_nl.py argument '--a'"""
    lemm = WordNetLemmatizer()
    ls_dw = [lemm.lemmatize(word) for word in word_tokenize(ut.data_read)]
    print(ls_dw)


def stem_file():
    """ performs Stemmer text
      used in file util_nl.py argument '--a'"""
    p_s = PorterStemmer()
    words = word_tokenize(ut.data_read)
    for _w in words:
        print(p_s.stem(_w))


def stop_word():
    """ removes stop words
    used in file util_nl.py argument '--b'"""
    new_words = []
    [new_words.append(w.lower()) for w in word_tokenize(ut.data_read)]
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in new_words if not w in stop_words]
    print(filtered_sentence)


def word_count_all():
    """ counts all duplicate words in the text
    used in file util_nl.py argument '--с' """
    all_words = []
    [all_words.append(w.lower()) for w in word_tokenize(ut.data_read)]
    all_words = nltk.FreqDist(all_words)
    print(all_words.most_common())


def word_count():
    """ displays the specified number of frequent words
    used in file util_nl.py argument '--d'  """
    all_words = []
    [all_words.append(w.lower()) for w in word_tokenize(ut.data_read)]
    all_words = nltk.FreqDist(all_words)
    print(all_words.most_common(ut.d))
