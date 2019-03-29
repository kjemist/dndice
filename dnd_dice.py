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
	def roll(input_string, give_rolls=False):
		"""
		die syntax: "adb+c", e.g. 3d6+1
		a = number of dice
		b = number of sides
		c = dice modifier
		d = denotes a die/dice being used in input string.
			This part also "splits" the string into an "a-part" and a "b+c" part
		give_rolls: Optional argument. If set to "True", returns the roll,
		and a list of all the rolls
		"""

		#--------- Determining a, b and c -----------------------------

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

		rolled_sum = 0
		rolled_list = []
		for x in range(a):
			rolled = random.randint(1,b)
			rolled_list.append(rolled)
			rolled_sum = rolled_sum + rolled
		rolled_sum = rolled_sum + c
		# The modifier, c, is only added to the total sum of the rolled dice,
		# not to each individual dieroll
		if give_rolls:
			return rolled_sum, rolled_list
		else:
			return rolled_sum

	def mobsave(mobnumber, DC, modifier):
		"""
		Function for when an entire mob has to make a save against the
		same spell/attack, for example Turn Undead.
		mobnumber = number of enemies in the mob
		DC = the difficulty class of the roll (See the PHB, page ###)
		Modifier = the modifier the enemy has for the roll
		Returns a printed statement of how many enemies fail the roll
		"""
		saved = 0
		for save in range(mobnumber):
			roll = dice.roll("1d20+%d" % modifier)
			if roll >= DC:
				saved += 1
		return "%d of %d passed the save" % (saved, mobnumber)


#def syntax testing
#print("ex1:", roll(1, 6, 1))
#print("ex2:", roll(2, 6, 3))
#print("ex3:", roll(10, 8, 1))

#class syntax testing 
#print(dice.roll("1d600-123"))
#print(dice.roll("1d600-123"))

#print(dice.roll("2d6+3"))
#print(dice.roll("10d8+1")) 
#print(dice.roll("1d60"))
#print(dice.roll("5d20-1"))
#print(dice.roll("5d8+3", True))

#mobsave testing:

print( dice.mobsave(200, 14, 3))