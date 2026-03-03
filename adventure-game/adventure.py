class Room:
    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.item = item
        self.next_room = None


class Player:
    def __init__(self):
        self.inventory = []


def move_to_room(room):
    print("\nYou are in:", room.name)
    print(room.description)

    if room.item:
        print("You found:", room.item)


def take_item(player, room):
    if room.item:
        player.inventory.append(room.item)
        print("You picked up:", room.item)
        room.item = None
    else:
        print("Nothing to take here.")


def show_inventory(player):
    if not player.inventory:
        print("Inventory is empty.")
    else:
        print("Your items:", player.inventory)


def main():
    print("Welcome to the Adventure Game!")
    # Create rooms
    room1 = Room("Entrance", "You see a dark door ahead.", "Key")
    room2 = Room("Hall", "A long hallway with strange noises.")
    room3 = Room("Treasure Room", "A room full of gold!")

    # Connect rooms
    room1.next_room = room2
    room2.next_room = room3

    player = Player()
    current_room = room1

    while True:
        move_to_room(current_room)

        print("\nOptions:")
        print("1. Move forward")
        print("2. Take item")
        print("3. Show inventory")
        print("4. Quit")

        choice = input("Choose: ")

        if choice == "1":
            if current_room.next_room:
                current_room = current_room.next_room
            else:
                print("No more rooms. You won the game! 🎉")
                break

        elif choice == "2":
            take_item(player, current_room)

        elif choice == "3":
            show_inventory(player)

        elif choice == "4":
            print("Game ended.")
            break

        else:
            print("Invalid choice!")


main()
