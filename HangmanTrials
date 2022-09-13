import unittest


class Player:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        name = input("Please enter a player name: ")
        return name


class TestPlayerName(unittest.TestCase):
    def runTest(self):
        print('start test')
        name = Player.get_name(self)
        print(name)
        message = "Name cannot be blank."
        self.assertNotEqual(name, '', message)


class PlayerNumber:
    def __init__(self, nbr_players):
        self.nbr_players = nbr_players

    def get_nbr_players(self):
        self.nbr_players = input('Please choose the number of players. Maximum of 4: \n')
        self.nbr_players = int(self.nbr_players)
        return self.nbr_players


class TestNbrPlayers(unittest.TestCase):
    def runTest(self):
        print('start test')
        test = PlayerNumber.get_nbr_players(self)
        print(test)
        values = [1, 2, 3, 4]
        message = 'The number of players must be between 1 and 4.'
        self.assertIn(test, values, message)


unittest.main()
