from Stack import Stack

# Create the stacks
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks = [left_stack, middle_stack, right_stack]

# Enter the number of disks
num_disk = int(input("\nEnter the number of disks: "))

while num_disk < 3:
    num_disk = int(input("\nEnter the number of disks: "))

for disk in range(num_disk, 0, -1):
    left_stack.push(disk)

# Return least number for moves
print("The fastest you can solve this game is {NUM} moves".format(NUM=2 ** num_disk - 1))


# Get user input
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for num in range(len(choices)):
            name = stacks[num].get_name()
            letter = choices[num]
            print("Enter {LETTER} for {NAME}".format(LETTER=letter, NAME=name))
        user_input = input("")
        if user_input in choices:
            for i in range(len(choices)):
                if user_input == choices[i]:
                    return stacks[i]


# Get number of moves
num_moves = 0

while right_stack.get_size() < num_disk:
    print("\n\n\n...Current Stacks...")
    for stack in stacks:
        stack.print_nodes()
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()
        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again")
        elif to_stack.is_empty or from_stack.peek() < to_stack.peek:
            disk = from_stack.pop()
            to_stack.push(disk)
            num_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")


print("\n\nYou completed the game in {MOVES} moves, and the optimal number of moves is {OPT}".format(MOVES=num_moves, OPT=2 ** num_disk - 1))