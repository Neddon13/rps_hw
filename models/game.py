class Game:

    def __init__(self):
        self.check_result = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock",
        }

    def play(self, player_1, player_2):

        winner = None

        if self.check_result[player_1.move.lower()] == player_2.move.lower():
            winner = player_1
        else: 
            self.check_result[player_2.move.lower()] == player_1.move.lower()
            winner = player_2

            return winner

