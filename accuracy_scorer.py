"""
 Hangman - Accuracy scorer

 Goal - To calculate the accuracy of the program written (hangman_driver.py)
"""

# Ignoring warnings
import warnings
warnings.filterwarnings("ignore")

# Importing required libraries
import time
import pandas as pd

# Importing all dependencies and other helpful moduels 
from helper_modules.utility_functions import preprocess
from hangman_driver import play_game


# Driver Program
if __name__ == '__main__':
    # Reading the words and creating a dictionary
    words = pd.read_csv('words.txt', sep='\n', header=None).iloc[:, 0].tolist()
    dictionary = preprocess('words.txt')
    
    # Initializing the variables required
    start_time = time.time()
    total_guesses = 0
    total_word_g = 0
    total_characters = 0
    
    # Start the prediction for each word
    for word in words:
        total_characters += len(word)
        board = ['_']*len(word)
        
        # Calling the logical prediction function
        temp_1, temp_2 = play_game(board, word, dictionary, False)
        
        # Calculating the words guessed right, and the number of chances taken to predict each word
        total_guesses += temp_2
        total_word_g += temp_1
        
    print("Done!")
    print("Time elapsed:", time.time()-start_time, end="\n\n")
    
    print("Prediction Accuracy (Word-wise)")
    print("INFO: This expalins the number of words predicted rightly\n")
    print("Total words to guess         :", len(words))
    print("Total words predicted rightly:", total_word_g)
    print("\nWord-wise Accuracy         :", round(total_word_g/len(words) * 100, 2), "%\n\n")
    
    print("Prediction Accuracy (character-wise)")
    print("INFO: This expalins the number of chances taken to predicted the entire word_set (words.txt) rightly\n")
    print("Total characters to guess    :", total_characters)
    print("Total guesses taken          :", total_guesses)
    print("\nCharacter-wise Accuracy    :", round(total_characters/total_guesses * 100, 2), "%\n\n")
