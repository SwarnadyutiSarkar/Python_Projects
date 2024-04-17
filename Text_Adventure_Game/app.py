# Define game states
class GameState:
    START = 0
    ROOM1 = 1
    ROOM2 = 2
    ROOM3 = 3
    END = 4

# Game variables
current_state = GameState.START
inventory = []

# Game functions
def start_game():
    global current_state
    print("You wake up in a mysterious room with three doors.")
    current_state = GameState.ROOM1

def room1():
    global current_state
    print("You enter Room 1.")
    print("There is a key on the table.")
    action = input("What do you want to do? (take/leave/go back) ").lower()
    
    if action == 'take':
        print("You take the key.")
        inventory.append('key')
        current_state = GameState.ROOM2
    elif action == 'leave':
        print("You leave the key on the table.")
        current_state = GameState.ROOM2
    elif action == 'go back':
        print("You go back to the starting room.")
        current_state = GameState.START
    else:
        print("Invalid choice.")
        room1()

def room2():
    global current_state
    print("You enter Room 2.")
    print("There is a locked door and a chest.")
    action = input("What do you want to do? (open chest/use key/go back) ").lower()
    
    if action == 'open chest':
        print("You open the chest and find a map.")
        inventory.append('map')
        current_state = GameState.ROOM3
    elif action == 'use key':
        if 'key' in inventory:
            print("You unlock the door and enter Room 3.")
            current_state = GameState.ROOM3
        else:
            print("You don't have the key.")
            room2()
    elif action == 'go back':
        print("You go back to Room 1.")
        current_state = GameState.ROOM1
    else:
        print("Invalid choice.")
        room2()

def room3():
    global current_state
    print("You enter Room 3.")
    print("There is a treasure chest.")
    action = input("What do you want to do? (open chest/go back) ").lower()
    
    if action == 'open chest':
        if 'map' in inventory:
            print("You open the chest and find a treasure!")
            current_state = GameState.END
        else:
            print("You don't have the map.")
            room3()
    elif action == 'go back':
        print("You go back to Room 2.")
        current_state = GameState.ROOM2
    else:
        print("Invalid choice.")
        room3()

def end_game():
    print("Congratulations! You have completed the adventure.")
    print("Thanks for playing!")

# Main game loop
while current_state != GameState.END:
    if current_state == GameState.START:
        start_game()
    elif current_state == GameState.ROOM1:
        room1()
    elif current_state == GameState.ROOM2:
        room2()
    elif current_state == GameState.ROOM3:
        room3()

# End game
end_game()
