# your code goes here!

import collections


class Anagram:
    def __init__(self, word):
        self.word = word


    def match(self, word_list):
        return [w for w in word_list if self.is_anagram(w.lower())]

    def is_anagram(self, other_word):
        return sorted(self.word) == sorted(other_word)