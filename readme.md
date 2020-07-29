# Hangman

## Project Description
Hangman is a popular game. It involves guessing words rightly in a given number of chances.
It starts when an opponent gives you a word (where the actual letter in the words are hidden, i.e, only the lenght of word is given). The player starts guessing with each letter.

This project is a simulation of the same game, but both the players here are managed by the computer. It does not involve a human.
Given a list of words `words.txt` in the repository, the computer picks a random word from the dictionary and assigns it to the other program `hangman_driver.py`

The `hangman_driver.py` has the knowledge of the dictionary and it starts guessing the words by analysing the most occurred letter in the dictionary for the given lenght of word. It guesses the word and evaluates the result. Once it gets the letter right, it refines its search for that particular words where the rightly guessed pattern is present.

## Code - Components
There are two major files related to python code <br>

* `hangman_driver.py` -- The driver code, which drives the entire gameplay. Starts by picking out a random word from the dictionary (`words.txt`) and goes on to guess the letter, evaluates the result, refines the search-words and the process continues till the right word is guessed.<br>
It uses some `helper_modules/` for picking, guessing, evaluate and search-refined-words. <br>
* `accuracy_scorer.py` -- A code file which uses `hangman_driver.py` and runs on all the words in the dictionary `words.txt`. Metrics are displayed below this section <br>

## How to run
1. pip install -r requirements.txt
2. python hangman_driver.py
3. python accuracy_scorer.py

## Metrics
```
Prediction Accuracy (Word-wise)
INFO: This expalins the number of words predicted rightly

Total words to guess         : 4507
Total words predicted rightly: 4504
Word-wise Accuracy         : 99.93 %


Prediction Accuracy (character-wise)
INFO: This expalins the number of chances taken to predicted the entire word_set (words.txt) rightly

Total characters to guess    : 41016
Total guesses taken          : 45280

Character-wise Accuracy    : 90.58 %
```

Also, the code is well-documented. <br>
Cheers :)