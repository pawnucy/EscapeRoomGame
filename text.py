import json
# from main import MainMenu


class GameText:
    """ Class for texts used, for example, in menus, welcome screen and others. """
    @classmethod
    def welcome(cls):
        # Display game logo.
        filename = 'text/logo.json'
        with open(filename, 'r', encoding="utf8") as f:
            logo = json.loads(f.read())
        for line in logo:
            print(line)

    @classmethod
    def wakeup_msg(cls):
        # Displays message when player starts new game in first room.
        filename = 'text/wakeup.txt'
        with open(filename, 'r') as f:
            wakeup = f.read()
            print(wakeup)
            cls.help_text()

    @classmethod
    def help_text(cls):
        # Displays command and help for player
        filename = 'text/help.txt'
        with open(filename, 'r') as f:
            help_txt = f.read()
            print(help_txt)

    @classmethod
    def complete_room1(cls):
        # Displays text when player complete room1.
        filename = 'text/complete_room1.txt'
        with open(filename, 'r') as f:
            complete = f.read()
            print(complete)
            quit()
        # MainMenu.logo()


class RoomDescription:
    """ Class for room description"""
    @classmethod
    def room1(cls):
        filename = 'text/places/cloudy_room_dscrp.txt'
        with open(filename, 'r') as f:
            describe = f.read()
            print(describe)


class RoomPlace:
    """ Class for places in rooms. """
    def __init__(self, place_name):
        self.place_name = place_name

    def name(self, place_name):
        # Place description.
        if place_name == "window":
            # Room1 place with window.
            filename = 'text/places/window.txt'
            with open(filename, 'r') as f:
                describe = f.read()
                print(describe)
        elif place_name == 'chest':
            # Room1 place with chest.
            filename = 'text/places/chest.txt'
            with open(filename, 'r') as f:
                describe = f.read()
                print(describe)
        elif place_name == 'desk':
            # Room1 place with desk.
            filename = 'text/places/desk.txt'
            with open(filename, 'r') as f:
                describe = f.read()
                print(describe)
        elif place_name == 'door':
            # Room1 place with door.
            filename = 'text/places/door.txt'
            with open(filename, 'r') as f:
                describe = f.read()
                print(describe)


class Event:
    """ Class for events in game. """
    @classmethod
    def open_chest(cls):
        # Displays text when open chest in room1.
        filename = 'text/events/open_chest.txt'
        with open(filename, 'r') as f:
            text = f.read()
            print(text)

    @classmethod
    def open_desk(cls):
        # Displays text when open desk in room1.
        filename = 'text/events/open_desk.txt'
        with open(filename, 'r') as f:
            text = f.read()
            print(text)

    @classmethod
    def read_paper(cls):
        # Displays text when item is in inventory and command 'use'.
        print('On the piece of paper are written numbers: 21')

    @classmethod
    def read_plaque(cls):
        # Displays text when item is in inventory and command 'use'.
        print('The wooden plate bears the engraved numbers: 37')

    @classmethod
    def try_padlock(cls):
        combination = input('Enter combinations: ')
        if combination == '2137':
            GameText.complete_room1()
        else:
            print('Wrong combination! Use padlock to try again or type another command.')
