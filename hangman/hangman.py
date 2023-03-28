#!/usr/bin/env python
#-*- coding:utf-8 -*-

from hangbaner import *
import random
import os

def merge_list(lst, sep):
    merged = ''
    for element in lst:
        if type(element) == type(''):
            merged += ''.join(element + sep)
   
    return merged

def find_positions(letter, word ):
    positions = []
    for n in range(0, len(word)):
        if word[n] == letter:
            positions.append(n)    
    return positions

def print_view(hangman, count, blank):
    os.system("clear")
    print(banner) 
    
    print("==============================")
    print(hangman[count])
    word = merge_list(blank, ' ')
    print(f"WORD: {word}")
    print("==============================")
   
hangman = [one, two, three,four, five, six, seven]

listWords = []

hangmanCounter = 0

with open("nouns.txt", "r") as words:
    myWords = words.readlines()
    listWords = [word.split()[0] for word in myWords if len(word.split()[0]) > 7 ]
    
random_word = random.choice(listWords)

blanked_word  = []
for n in range(0, len(random_word) ):
    blanked_word += '❎'


print_view(hangman, hangmanCounter, blanked_word)            

letter_from_user = input("Get letter: ")
       
while hangmanCounter < len(hangman)-1 and blanked_word != random_word:

    while blanked_word != random_word:        

        if letter_from_user in random_word and letter_from_user not in blanked_word:
           
            positions = find_positions( letter_from_user, random_word )
            blanked_word = list(blanked_word)
            for pos in positions:
                blanked_word[pos] = letter_from_user
                
            blanked_word = ''.join(blanked_word)
            print_view(hangman, hangmanCounter, blanked_word)            

        else:
            hangmanCounter += 1
        
        if blanked_word == random_word:
            print_view(hangman, hangmanCounter, blanked_word)
            print(f"You are WINNER!")
            print("==============================")
            break
                    
        elif hangmanCounter < len(hangman) -1:
            print_view(hangman, hangmanCounter, blanked_word)                        
            letter_from_user = input("Get letter: ")
        
        else:
            print_view(hangman, hangmanCounter, blanked_word)            
            break
        