ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not 10 things in this list. Let's fix that.")

stuff = ten_things.split(' ') # split(ten_things)
more_stuff = ["Day", "Night", "Song", "Frisbee", 
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop(more_stuff)
    print("Adding: ", next_one)
    stuff.append(next_one) # append(stuff)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff)) # stuff.join()
print('#'.join(stuff[3:5])) #stuff.join(3:5)
      