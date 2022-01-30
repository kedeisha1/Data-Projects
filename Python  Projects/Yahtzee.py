# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 07:31:23 2021

@author: kbryan
"""
import random
new_line = '\n'

Start = input('Ready to play Triple Yahtzee? Type Yes ')
if Start == 'Yes' or Start == 'yes':
    Dice_1 = random.randint(1,6)
    Dice_2 = random.randint(1,6)
    Dice_3 = random.randint(1,6)
    Dice_4 = random.randint(1,6)
    Dice_5 = random.randint(1,6)
    print(f'You rolled: {new_line} dice 1 = {Dice_1} {new_line} dice 2 = {Dice_2}\
          {new_line} dice 3 = {Dice_3} {new_line} dice 4 = {Dice_4} {new_line} dice 5 = {Dice_5}')
Roll_2_decision = input('Which dice would you like to keep? Example: 123 etc ')
all_dice = [Dice_1, Dice_2, Dice_3, Dice_4, Dice_5]
keep = []
roll_again = []
for x in Roll_2_decision:
    if x not in keep:
        keep.append(x)
nums = ['1', '2', '3', '4', '5', '6']

if '1' not in keep:
    Dice_1 = random.randint(1,6)
    keep.append(Dice_1)
elif '2' not in keep:
    
        
print(keep)



    
    
#for x in Roll_2_decision:
 #   if '1' in Roll_2_decision:
        
        
#if Roll_2_decision == 'Yes' or Roll_2_decision == 'yes' :
    #all_dice = [Dice_1, Dice_2, Dice_3, Dice_4, Dice_5]
    
    

