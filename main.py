from text import *


class MainMenu:
    """ Class for game main menu """

    @classmethod
    def logo(cls):
        # Displays the logo.
        GameText.welcome()
        MainMenu.menu()

    @classmethod
    def menu(cls):
        # Displays the main menu where player can start new game or quit application.
        print('\n\tGAME MENU\n==================\n\t1) New Game\n\t2) Quit\n')
        try:
            menu_input = int(input('Your choice: '))
        except ValueError:
            print('Incorrect data entered, make sure you are entering numbers!')
            MainMenu.menu()
        else:
            if menu_input == 1:
                NewGame.start_game()
            elif menu_input == 2:
                print('You are leaving?! How dare you!')
                quit()
            else:
                print('Please enter number 1 or 2.')
                MainMenu.menu()


class NewGame:
    """ Class for new game. """
    player_name = None

    @classmethod
    def start_game(cls):
        print('\nWelcome to the amazing adventure of "Cloud Mystery"!')
        p_name = input('Please enter your name: ')
        cls.name(p_name)

    @classmethod
    def name(cls, p_name):
        cls.player_name = p_name
        cls.welcome_player()

    @classmethod
    def welcome_player(cls):
        print(f'\nWelcome {cls.player_name}, your adventure has just begun!\n')
        GameText.wakeup_msg()
        Game.actual_room = 'room1'
        Game.command()


class Room:
    """ Class for room"""
    def __init__(self, name, description, places, items=None):
        self.name = name
        self.description = description
        self.items = items
        self.places = places

    def __str__(self):
        return self.description


class Game:
    # Main class for game
    actual_room = None
    actual_place = None
    inventory = []

    @classmethod
    def command(cls):
        # Commands that the player can choose.
        command = input('\n\tYour choice: ').lower()
        if command == 'help':
            # Displays help with a list of available commands.
            GameText.help_text()
            Game.command()
        elif command == 'describe':
            # Displays room description with places where player can go.
            if cls.actual_room == 'room1':
                RoomDescription.room1()
                Game.command()
        elif command.startswith('take'):
            # Adds item to inventory.
            take_item = command.split()[1]
            Item.take(take_item)
        elif command.startswith('use'):
            # Use item from inventory.
            use_item = command.split()[1]
            Item.use(use_item)
        elif command == 'inventory':
            # Displays actual inventory.
            Inventory.show()
            Game.command()
        elif command.startswith('go'):
            # Player moves to selected location.
            place = command.split()[1]
            Game.move(place)
        elif command == 'quit game':
            quit()
        else:
            print('Such a command does not exist!')
            Game.command()

    @classmethod
    def move(cls, place_name):
        # A method for moving to specific locations in a room.
        if place_name in room1.places:
            place = RoomPlace(place_name)
            place.name(place_name)
            Game.actual_place = place_name
            Game.command()
        else:
            print('There is no such place in this room.')
            Game.command()


class Item:
    # Clas for items
    desk_open = False

    @classmethod
    def take(cls, item):
        # A method for taking items in location.
        if Game.actual_room == 'room1':
            if item in Game.inventory:
                print('You have this item in your inventory.')
            elif item == 'plaque' and not Item().desk_open:
                print('There is no such item in this place.')
            elif Game.actual_place in room1_items.keys() and item in room1_items[Game.actual_place]:
                print(f'You take the {item} and put it in your pocket.')
                Inventory.add(item)
            else:
                print('There is no such item in this place.')
        Game.command()

    @classmethod
    def use(cls, item):
        # A method for using items.
        if Game.actual_place == 'door' and item == 'padlock':
            Event.try_padlock()
        elif item in Game.inventory:
            # Using items in room1
            if item == 'paper':
                Event.read_paper()
            elif item == 'plaque':
                Event.read_plaque()
            elif Game.actual_place == 'chest' and item == 'key':
                Inventory.delete(item)
                Event.open_chest()
            elif Game.actual_place == 'desk' and item == 'dagger':
                Inventory.delete(item)
                Event.open_desk()
                Item.desk_open = True
            else:
                print(f'You try to use the {item}, but find no use for it.')
        else:
            print("You don't have this item in your inventory.")
        Game.command()


class Inventory:
    # Class for player inventory.
    @classmethod
    def add(cls, item):
        # A method for adding item to inventory.
        Game.inventory.append(item)

    @classmethod
    def delete(cls, item):
        # A method for deleting item from inventory.
        Game.inventory.remove(item)
        print(f'The {item} has been removed from your inventory.')

    @classmethod
    def show(cls):
        # Shows actual inventory.
        print(f'Inventory: {Game.inventory}')


# Room creating.
room1_places = ['window', 'desk', 'chest', 'door']
room1_items = {'window': 'key', 'chest': ['paper', 'dagger'], 'desk': 'plaque', 'door': 'lock'}
room1 = Room("Cloudy Room", RoomDescription.room1, room1_places, room1_items)


if __name__ == '__main__':
    MainMenu.logo()
