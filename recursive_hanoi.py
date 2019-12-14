step = 1

def move(fr, to):
    global step
    print(f"Step {step}:\tMove from {fr} to {to}")
    step += 1

def hanoi(fr, to, via, n):
    if n == 0:
        pass
    else:
        hanoi(fr, via, to, n-1)
        move(fr, to)
        hanoi(via, to, fr, n-1)

n = input("How many layers does your tower of Hanoi have?\n\t")
try:
    n = int(n)
except:
    pass
while type(n) is not int or n < 1:
    n = input("Please enter a positive number as the tower's height!\n\t")
    try:
        n = int(n)
    except:
        pass

print("To solve the tower in the least possible moves, follow these instructions:\n\n")

hanoi(1, 3, 2, n)