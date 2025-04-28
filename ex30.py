# variable specifying the number of people
people = 30
# variable specifying the number of cars
cars = 40
# variable specifying the number of trucks
trucks = 15

# if statement specifying that the following command only applies if cars > people
if cars > people:
    # Print string if condition is met
    print("We should take the cars.")
# elif statemnt specifying that the following command applies if cars < people AND first condition isn't met
elif cars < people: # another option for the code if the "if" condition above isn't met
    # print string if elif condition is met
    print("We should not take the cars.")
else: # one last option for the code if neither of the conditions in "if" or "elif" are met
    # print string if neither if or elif conditions are met
    print("We can't decide.")

# if statement specifying that the following command only applies if trucks > cars
if trucks > cars:
    # Print string if condition is met
    print("That's too many trucks.")
# elif statement specifying that the following command applies of trucks < cars and first condition isn't met
elif trucks < cars:
    # Print string if condition is met
    print("Maybe we could take the trucks.")
# one last option for the code if neither of the conditions in "if" or "elif" are met
else:
    # Print string if condition is met
    print("We still can't decide.")

# if statement specifying that the following command only applies if people > trucks
if people > trucks:
    # Print string if condition is met
    print("All right, let's just take the trucks.")
# Alternative option for the code if the "if" condition isn't met
else:
    # Print string if condition is met
    print("Whatever, let's just stay home.")

if cars > people or trucks < cars:
    print("We should take the cars.")
elif trucks > people and cars < people:
    print("We should really take the trucks.")
else:
    print("We're totally confused and will stay home.")

