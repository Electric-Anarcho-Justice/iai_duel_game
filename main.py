from random import randint

#########
# RULES #
#########

# Exploding dice
def roll_d10():
    roll_d10_result = randint(1,10)
    if roll_d10_result == 10:
        roll_d10_result += roll_d10()
    return roll_d10_result

# Define characters
class bushi:
    def __init__(self, name, awareness, agility, earth, iaijutsu, void, armor):
        self.name = str(name)
        self.awareness = int(awareness)
        self.agility = int(agility)
        self.earth = int(earth)
        self.iaijutsu = int(iaijutsu)
        self.void = int(void)
        self.health_points = 8 * self.earth
        self.armor = int(armor)

class stance:
    def __init__(self,challenger,challenged, target_number):
        self.challenger = challenger
        self.challenged = challenged
        self.tn = int(target_number)

    def result(self):
        result_stance = []
        for i in range(challenger.awareness + challenger.iaijutsu):
            result_stance.append(roll_d10())
        result_stance.sort(reverse=True)
        return result_stance

    def stance_menu_raise(self):
        print("|------------------------------------------------------------|")
        print("You can raise your Target Number to learn about your opponent:")
        print("1. One fact at default Target Number of 15")
        print("2. Two facts at Target Number of 20")
        print("3. All three facts at Target Number of 25")
        print("|------------------------------------------------------------|")
        chosen_tn = input("What is your choice?\n")
        if chosen_tn == str(1):
            self.tn = 15
        elif chosen_tn == str(2):
            if challenger.void < 2:
                print("You Void score is too low.")
                print("You cannot raise more than your Void trait.")
                self.stance_menu_raise()
            else:
                self.tn = 20
        elif chosen_tn == str(3):
            if challenger.void < 3:
                print("You Void score is too low.")
                print("You cannot raise more than your Void trait.")
                self.stance_menu_raise()
            else:
                self.tn = 25
        else:
            print("I did not understand your choice.")
            self.stance_menu_raise()

    def stance_menu_facts_main(self):
        evaluate_opponent = input('As you face your enemy, do you wish to determine one of three facts about him?\nYes or No?\n').lower()
        if evaluate_opponent.startswith('y'):
            self.stance_menu_raise()
            print(self.tn)
            if self.tn == 15:
                self.stance_menu_facts_1()
            elif self.tn == 20:
                self.stance_menu_facts_2()
            elif self.tn == 25:
                self.stance_menu_facts_3()
            else:
                print("I did not get what you wanted.")
                exit()
        else:
            print('Your arrogance could be your death.\nPrepare to draw your katana...\n')

    def stance_menu_facts_1(self):
        choice_evaluate = input('What do you wish to know?\nAgility, Iaijutsu or Void?\n').lower()
        if choice_evaluate.startswith('a'):
            roll = self.result()
            print("You rolled", roll)
            stance_sum = sum(roll[:challenger.awareness])
            print(f"Your score is {stance_sum}.")
            if stance_sum >= self.tn:
                print("The agility of", challenged.name,"is",challenged.agility)
            else:
                print("You couldn't evaluate your enemy.")
        elif choice_evaluate.startswith('i'):
            roll = self.result()
            print("You rolled", roll)
            stance_sum = sum(roll[:challenger.awareness])
            print(f"Your score is {stance_sum}.")
            if stance_sum >= self.tn:
                print("The Iaijutsu of", challenged.name,"is",challenged.iaijutsu)
            else:
                print("You couldn't evaluate your enemy.")
        elif choice_evaluate == "Void":
            roll = self.result()
            print("You rolled", roll)
            stance_sum = sum(roll[:challenger.awareness])
            print(f"Your score is {stance_sum}.")
            if stance_sum >= 15:
                print("The Void of", challenged.name,"is",challenged.void)
            else:
                print("You couldn't evaluate your enemy.")
        else:
            print("Please select a proper trait.")

    def stance_menu_facts_2(self):
        print("|---------------------------------------------|")
        print('What do you wish to learn about your opponent?')
        print('1. Agility and Iaijutsu')
        print('2. Agility and Void')
        print('3. Iaijutsu and Void')
        print("|---------------------------------------------|")
        choice_menu_2 = input("What is your choice?\n")
        if choice_menu_2 == str(1):
            roll = self.result()
            print("You rolled", roll)
            stance_sum = sum(roll[:challenger.awareness])
            print(f"Your score is {stance_sum}.")
            if stance_sum >= self.tn:
                print("The Agility of", challenged.name,"is",challenged.agility)
                print("The Iaijutsu of", challenged.name,"is",challenged.iaijutsu)
            else:
                print("You couldn't evaluate your enemy.")
        elif choice_menu_2 == str(2):
            roll = self.result()
            print("You rolled", roll)
            stance_sum = sum(roll[:challenger.awareness])
            print(f"Your score is {stance_sum}.")
            if stance_sum >= self.tn:
                print("The Agility of", challenged.name,"is",challenged.agility)
                print("The Void of", challenged.name,"is",challenged.void)
            else:
                print("You couldn't evaluate your enemy.")
        elif choice_menu_2 == str(3):
            roll = self.result()
            print("You rolled", roll)
            stance_sum = sum(roll[:challenger.awareness])
            print(f"Your score is {stance_sum}.")
            if stance_sum >= 15:
                print("The Iaijutsu of", challenged.name,"is",challenged.iaijutsu)
                print("The Void of", challenged.name,"is",challenged.void)
            else:
                print("You couldn't evaluate your enemy.")
        else:
            print("Please select a proper number.")
            self.stance_menu_facts_2()

    def stance_menu_facts_3(self):
        print("So you wish to know all facts about your opponent?")
        roll = self.result()
        print("You rolled", roll)
        stance_sum = sum(roll[:challenger.awareness])
        print(f"Your score is {stance_sum}.")
        if stance_sum >= self.tn:
            print("Here are all the facts about your opponent:")
            print("Agility:",challenged.agility)
            print("Iaijutsu:",challenged.iaijutsu)
            print("Void:",challenged.void)
        else:
            print("You couldn't evaluate your enemy.")

    

challenger = bushi('Daisuke',4,3,3,3,3,0)
challenged = bushi('Setsune',3,3,3,2,2,0)

s = stance(challenger,challenged,15)
s.stance_menu_facts_main()
