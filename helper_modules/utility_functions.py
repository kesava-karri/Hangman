"""
    Goal : Placing all the utility functions
"""

# Importing the required library
import pandas as pd

def preprocess(file_name):
    """
        A function to preprocess the file, sort according to the length of words, for faster access
        
        :param file_name: Path to file
        
        return <[string, string...]
    """
    # Read the words
    df = pd.read_csv('words.txt', sep='\n', header=None)
    
    # Find the length of each word and create a column
    df['len_of_word'] = df.iloc[:, 0].apply(lambda x: len(x))
    df.columns = ['word', 'len_of_word']
    
    # Find the unique lengths
    unique_lengths = df['len_of_word'].unique()
    word_dictionary = dict()
    for i in unique_lengths:
        word_dictionary[i] = list()
        
    # Initialize
    words = df['word'].tolist()
    lengths = df['len_of_word'].tolist()
    
    # Create a dictionary, with length as keys and words as list
    for u_length in unique_lengths:
        for word, length in zip(words, lengths):
            if length == u_length: 
                word_dictionary[u_length].append(word)
    
    return word_dictionary