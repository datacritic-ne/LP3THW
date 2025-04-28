# this function is like a script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# but the 'args' is actually useless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this function just takes one arg
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no args
def print_none():
    print("Got nothin' here.")

print_two("Nick", "Emptage")
print_two_again("Nick", "Emptage")
print_one("First!")
print_none()
