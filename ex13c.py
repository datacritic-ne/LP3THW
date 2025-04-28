from sys import argv

#times = input("How many times have you been to Berkeley?")
#bdegree = input("Why were you going to go to Berkeley?")
#reason = input("Why would Berkeley not have worked out?")
#where = input("Where did you go instead?")
#mdegree = input("What degree did you get instead?")

script, first, second, third, fourth, fifth = argv
judge = input("Was this a good thing? ")

print("The number of times you've been to Berkeley: ", first) # 4
print("The reason you almost went to Berkeley: ", second) # PhD
print("The reason Berkeley may not have worked out: ", third) # Politics
print("Where you went instead: ", fourth) # Michigan
print("The degree you have now: ", fifth) # MAE
print("Was this a good thing? ", judge)


