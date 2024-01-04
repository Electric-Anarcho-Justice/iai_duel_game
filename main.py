# Exploding dice
def roll_d10():
    roll_d10_result = randint(1,10)
    if roll_d10_result == 10:
        roll_d10_result += roll_d10()
    return roll_d10_result
