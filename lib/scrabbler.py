""" Class Scrabbler - Scrabble utilities """

import json

# Scrabble dictionaries that have been loaded -
# keys are file names, values are word/definition dictionaries
DICTIONARIES = {}

# Default dictionary loaded if no other file is given to constructor.
DEFAULT_DICTIONARY = "../data/collins_2019.json"

# Map from letters to counts and scores
LETTERS = {
    '_' : {'count' : 2, 'score' : 0},
    'A' : {'count' : 9, 'score' : 1},
    'B' : {'count' : 2, 'score' : 3},
    'C' : {'count' : 2, 'score' : 3},
    'D' : {'count' : 4, 'score' : 2},
    'E' : {'count' : 12, 'score' : 1},
    'F' : {'count' : 2, 'score' : 4},
    'G' : {'count' : 3, 'score' : 2},
    'H' : {'count' : 2, 'score' : 4},
    'I' : {'count' : 9, 'score' : 1},
    'J' : {'count' : 1, 'score' : 8},
    'K' : {'count' : 1, 'score' : 5},
    'L' : {'count' : 4, 'score' : 1},
    'M' : {'count' : 2, 'score' : 3},
    'N' : {'count' : 6, 'score' : 1},
    'O' : {'count' : 8, 'score' : 1},
    'P' : {'count' : 2, 'score' : 3},
    'Q' : {'count' : 1, 'score' : 10},
    'R' : {'count' : 6, 'score' : 1},
    'S' : {'count' : 4, 'score' : 1},
    'T' : {'count' : 6, 'score' : 1},
    'U' : {'count' : 4, 'score' : 1},
    'V' : {'count' : 2, 'score' : 4},
    'W' : {'count' : 2, 'score' : 4},
    'X' : {'count' : 1, 'score' : 8},
    'Y' : {'count' : 2, 'score' : 4},
    'Z' : {'count' : 1, 'score' : 10}
}

class Scrabbler:
    """ Class implementing utitlity methods to help a Scrabble player """

    def __init__(self, dictionary_file=DEFAULT_DICTIONARY):
        """ Constructor """
        self.dictionary = Scrabbler.load_dictionary(dictionary_file)
        self.letters = LETTERS

    @staticmethod
    def load_dictionary(dictionary_file):
        """ Loads a Scrabble dictionary from a JSON file """
        if not dictionary_file in DICTIONARIES:
            with open(dictionary_file) as file:
                dictionary = json.load(file)
                DICTIONARIES[dictionary_file] = dictionary
        return DICTIONARIES[dictionary_file]

    def foobar(self):
        """ public method to keep PyLint happy """
        print(self.dictionary)
