#!/usr/bin/env python3


"""
script for simulating dice rolls in Dungeons and Dragons Fifth Edition
inputs number of dice, number of sides and dice modifier
outputs the total sum of the dice roller, including the modifier on top
designed to work with Python3

by Illimar Rekand
illimar.rekand@gmail.com

March 2019

"""

import random

class dice:
	#def roll(a,b,c):
	def roll(input_string):
		"""
		die syntax: "adb+c", e.g. 3d6+1
		a = number of dice
		b = number of sides
		c = dice modifier
		d = denotes a die/dice being used in input string
		"""

#----------------- Determining a, b and c -----------------------------

		if "d" in input_string:
			input_string_split = input_string.split("d")
			a = int(input_string_split[0])
			if "+" in input_string:
				sign_split = input_string_split[1].split("+")
				b = int(sign_split[0])
				c = int(sign_split[1])
			elif "-" in input_string:
				sign_split = input_string_split[1].split("-")
				b = int(sign_split[0])
				c = -int(sign_split[1])
			else:
				b = int(input_string_split[1])
				c = 0
					
#--------------- Rolling the actual dice ------------------------------

		rolled_sum=0
		rolled_list= []
		for x in range(a):
			rolled = random.randint(1,b)
			rolled_list.append(rolled)
			rolled_sum = rolled_sum + rolled
		rolled_sum = rolled_sum + c
		# The modifier, c, is only added to the total sum of the rolled dice,
		# not to each individual dieroll
		return rolled_sum, rolled_list,  input_string_split, a, b, c

#def syntax testing
#print("ex1:", roll(1,6,1))
#print("ex2:", roll(2,6,3))
#print("ex3:", roll(10,8,1))

#class syntax testing 
print(dice.roll("1d600-123"))
print(dice.roll("2d6+3"))
print(dice.roll("10d8+1")) 
print(dice.roll("1d60"))
print(dice.roll("5d20-1"))

