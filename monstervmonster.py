from dnd_dice import dice

"""
Creatures can see up 'till 2 miles (10560ft) according to DMG, page 243
"""

def attack_roll(attack_modifier, AC):
	Hit = False
	attack = dice.roll("1d20+%", % attack_modifier)
	if attack >= AC:
		return Hit = True
	elif attack - attack_modifier = 20:
		return Hit = True, print("Critical hit!")
	else:
		return "Miss"

distance = 10560

#monster1: Hill giant

m1_HP = 105
m1_AC = 13
speed1 = 40

m1_a1 =  dice.roll("1d6")
print(m1_a1)

#monster2: Frost giant

m2_HP = 138
m2_AC = 15
speed1 = 40

