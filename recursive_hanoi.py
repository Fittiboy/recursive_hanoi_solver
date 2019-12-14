step = 0

def move(fr, to):
    global step
    step += 1
    print(f"Step {step}:\tMove from {fr} to {to}")

def hanoi(fr, to, via, n):
    if n == 0:
        pass
    else:
        hanoi(fr, via, to, n-1)
        move(fr, to)
        hanoi(via, to, fr, n-1)

n = input("\n\nHow many layers does your tower of Hanoi have?\t")
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

print("\nTo solve the tower in the least possible moves, follow these instructions:")
input("(press Enter to start)\n")

hanoi(1, 3, 2, n)
print(f"\nCompleted in {step} steps.\n")