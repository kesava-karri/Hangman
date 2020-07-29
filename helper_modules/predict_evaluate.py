"""
    Goal: Predict a letter, evaluate the prediction and update key-things
"""

# Importing the required library
from collections import Counter

def most_occured_letter(rightly_guessed, dictionary):
    """
        A function which returns the most-occured letter in a set of words, also keeps track that the returned word is 
        not in the righty guessed words, or in the missed words
        
        :param rightly_guessed: A list of righly guesses letters by the program
        :param dictionary: Updated list of possible set of words, one of which might be the answer
        
        return <char>
    """
    # Finding the frequency of distribution for each element
    freq_count = Counter(list("".join(dictionary)))
    
    # Leave the characters which are already predicted or in the missing lists
    for letter in rightly_guessed:
        del freq_count[letter]
    
    # Most occured letter    
    letter = freq_count.most_common(1)[0][0]
    
    return letter
    
def predict_a_letter(rightly_guessed, dictionary):
    """
        A function which predicts a letter with the given state of board and dictionary
        
        :param rightly_guessed: A list of righly guesses letters by the program
        :param dictionary: Updated list of possible set of words, one of which might be the answer
        
        return <char>
    """
    guess = most_occured_letter(rightly_guessed, dictionary)
    
    return guess



def find_all_occurences(character, string):
    """
        To find all the occurences of a character in a given string, and return a list of indices
        
        :param character: A character to find locations off
        :param string: A string to find the character-in
        
        return <[int, int...]>
    """
    return [x for x, char in enumerate(string) if char == character]

def update_dictionary(board, dictionary, letter_present, guessed_letter):
    """
     To update the dictionary or set of words
        * Case - I
            If a letter is rightly predicted, then only select the words that have that letter in that specified postions in the board
        * Case - II
            If a letter is not present in the word, remove all the words with that letter in a word
                
        :param board: Defines the state of the board
        :param letter_present: A flag value to represent if the guesssed letter is present in the board
        :param guessed_letter: The guessed letter
        
    return <[string, string, ...]>
    """
    # Case - I
    if letter_present:
        new_words = list()
        blank_freq = find_all_occurences(guessed_letter, ''.join(board))
        
        for word in dictionary:
            if blank_freq == find_all_occurences(guessed_letter, word ):
                new_words.append(word)
        return new_words

    # Case - II
    else:
        new_words = list()
        new_words = [x for x in dictionary if guessed_letter not in x]
        return new_words

def evaluate_prediction(board, dictionary, missed, rightly_guessed, right_word, guessed_letter):
    """
        A function to evaluate the prediction, update the board and the dictionary, missing and rightly predicted letters.
        
        :param board: Defines the state of the board
        :param dictionary: Updated list of possible set of words, one of which might be the answer
        :param missed: A set of words that were wrongly predicted by the program
        :param rightly_guessed: A list of righly guesses letters by the program
        :param right_word: The actual word to predict
        :param guessed_letter: The guessed letter
        
    return <[list], [string...], [char, char...], char>
    """
    letter_present = False
    
    for location, letter in enumerate(list(right_word)):
        if letter == guessed_letter:
            board[location] = guessed_letter
            letter_present = True
    
    updated_dictionary = update_dictionary(board, dictionary, letter_present, guessed_letter)
    
    if letter_present:
        rightly_guessed.add(guessed_letter)
    else:
        missed.add(guessed_letter)
    
    return board, updated_dictionary, missed, rightly_guessed