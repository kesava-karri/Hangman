"""
 Goal : Choose a random word from a given dictionary
"""

# Importing the required libraries
import random
import pandas as pd


def get_a_word():
    """
        A function to read the words, also select a random word, return the board and the word.
        
        return <[char, char...], string> 
    """
    words = pd.read_csv('words.txt', sep='\n', header=None).iloc[:, 0].tolist()

    word = random.choice(words)
    blank = ['_'] * len(word)

    return (blank, word)

