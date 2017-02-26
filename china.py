import sys
import random

people_daily = open("people_daily.txt").readlines()
bloomberg = open("bloomberg.txt").readlines()

space = " "

random.shuffle(people_daily)
random.shuffle(bloomberg)


for content1,content2 in zip(people_daily,bloomberg):
        content1 = content1.strip()
        content2 = content2.strip()
        r = random.randrange(40, 60)
        print content1[:130-r]
        print space*r, content2[:130-r]