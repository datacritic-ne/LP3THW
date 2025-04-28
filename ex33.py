#i = 0
#numbers = []

endloop = int(input("What number should I end the loop at? "))
incrloop = int(input("By how many numbers should the loop increment? "))

def loopgame(endloop, incrloop):
    i = 0
    numbers = []
    while i < endloop:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + incrloop

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

loopgame(endloop, incrloop)

for i in range(0, endloop):
    numbers2 = []
    print(f"At the top i is {i}")
    numbers2.append(i)
    
    #i = i + incrloop
    
    print("Numbers now: ", numbers2)
    print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers2:
        print(num)
