#!/usr/bin/env python3

"""
script for simulating dice rolls in Dungeons and Dragons Fifth Edition
designed to work with Python3

by Illimar Rekand
illimar.rekand@gmail.com

March 2019

"""

import random

class dice:
	def roll(a,b,c):
		#a = number of dice, b = number of sides, c = dice modifier
		rolled_sum=0
		rolled_list= []
		for x in range(a):
			rolled = random.randint(1,b)
			rolled_list.append(rolled)
			rolled_sum = rolled_sum + rolled
		rolled_sum = rolled_sum + c
		# The modifier, c, is only added to the total sum of the rolled dice,
		# not to each individual dieroll
		return rolled_sum, rolled_list

#pre-class syntax testing
#print("ex1:", roll(1,6,1))
#print("ex2:", roll(2,6,3))
#print("ex3:", roll(10,8,1))

#class syntax testing 
print(dice.roll(1,6,1))
print(dice.roll(2,6,3))
print(dice.roll(10,8,1))