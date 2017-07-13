import string
from random import randint
import re
from getpass import getpass
import os
import sys
# Roll Dice Function
def diceroll(x,y,z):
        print(x+'d'+y+z)
        temp = 1
        dice1 = []
        if y == '0':
                print("Cannot use d0")
        else:
                while temp <= int(x):
                        dice1.insert(temp-1,randint(1,int(y)))
                        temp += 1
                print(dice1)
                print(sum(dice1)+int(z))
        print()

def application(dices):
        # Neaten string input
        dice = re.sub(' +', ' ', dices)
        if dice == "exit" or dice ==  "q" or dice == "quit":
                print('exiting')
                os._exit(0)

        dice = filter(lambda x: x =='0' or x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or x=='8' or x=='9' or x=='d' or x==' ' or x=='+' or x=='-', dice)
        dice = list(dice)
        if (dice[len(dice)-1] != ' '):
                dice.append(' ')

        # Sort dice rolls
        realdice = []
        while ' ' in dice:
                temp = []
                number = dice.index(' ')
                while number>=0:
                        temp.insert(0,dice[number])
                        dice.pop(number)
                        number-=1
                try:
                        a=temp.index('+')
                except:
                        try:
                                a=temp.index('-')
                        except:
                                temp.append('+0')
                realdice.append(''.join(temp).replace(" ",""))

        # Extract data from dice rolls
        realroll = []
        rolls = 0
        while rolls<len(realdice):
                rolldice = list(realdice[rolls])
                dee = rolldice.index('d')
                count = dee
                rolldice.pop(dee)
                temp = []
                while count>0:
                        temp.insert(count-1, rolldice[count-1])
                        rolldice.pop(count-1)
                        count-=1
                realroll.append(''.join(temp))
                try:
                        mod = rolldice.index('-')
                except:
                        mod = rolldice.index('+')
                count = mod
                temp = []
                while count>0:
                        temp.insert(0, rolldice[count-1])
                        rolldice.pop(count-1)
                        count-=1
                realroll.append(''.join(temp))
                realroll.append(''.join(rolldice))
                rolls+=1
        #Roll Dice
        while realroll != []:
                diceroll(realroll[0], realroll[1], realroll[2])
                counter = 0
                while counter < 3:
                        realroll.pop(0)
                        counter+=1

while True:
        try:
                application(input("Roll Dice: "))
        except KeyboardInterrupt:
                sys.exit()
        except:
                print("Please use correct syntax (#d#+# )")
