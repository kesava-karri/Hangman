"""
 Hangman

 Goal: The most optimized solution for predicting a word. Given only the length of the word and the knowledge of a dictionary.
"""
# Ignoring warnings
import warnings
warnings.filterwarnings("ignore")

# Importing all dependencies and other helpful moduels 
from helper_modules.word_chooser import get_a_word
from helper_modules.utility_functions import preprocess
from helper_modules.predict_evaluate import predict_a_letter, evaluate_prediction


def print_board(board, guessed_letter, missed):
    """
        A function to print the current state of the board
        
    :param board: Defines the state of the board
    :param guessed_letter: Predicted letter by the program
    :param missed: A set of words that were wrongly predicted by the program
    """
    print("\n\nguess:", guessed_letter, end="\n")
    
    for element in board:
        print(element, sep=' ', end=" ")
    
    print("missed:", end='')
    for element in missed:
        print(element, sep=',', end=" ")
 

def play_game(board, right_word, dictionary, verbose=True):
    """
        The `main` function which drives the logic of the program    
    :param board: Defines the state of the board
    :param right_word: The actual word to predict
    :param dictionary: Updated list of possible set of words, one of which might be the answer
    :param verbose: A flag vale to print/ not print the status of board at every level
    
    return (<0/1>, <int>)
    """
    # Picking the words which are of the given length for faster results
    len_word = len(board)
    updated_dictionary = dictionary[len_word]
    
    missed = set()
    rightly_guessed = set([''])
    if verbose:
        print("\n\nActual word", right_word)
        print_board(board, "", "")

    # Keep guessing until there are no blanks in the board
    while ('_' in board):
        # Predict a letter, evaluate the letter, update the dictionary and missed set
        guessed_letter = predict_a_letter(rightly_guessed, updated_dictionary)
        
        board, updated_dictionary, missed, rightly_guessed = evaluate_prediction(board, updated_dictionary, missed, rightly_guessed, right_word, guessed_letter)
        
        if verbose:
            print_board(board, guessed_letter, missed)
        
        # If missed letters are more than 6, terminate the prediction system
        if len(missed) > 6:
            total_guesses = len(right_word) + len(missed)
            return (0, total_guesses)
            
     
    # Total guesses taken by the program to predict a given word
    total_guesses = len(right_word) + len(missed)
    
    return (1, total_guesses)
    
# Driver Program
if __name__ == '__main__':
    
    # Generating a random word
    board, right_word = get_a_word()
    
    # Preprocessing the words.txt file to sort according to the length and form a dictionary, for fastest access.
    dictionary = preprocess('words.txt')     
    
    # Starting the prediction program
    play_game(board, right_word, dictionary)
    
    

