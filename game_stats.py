class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        self.high_score = open("highscore.txt", "r")
        self.high_score = int(self.high_score.read())
        print(self.high_score)

    def reset_stats(self):
            """Init statistics that can change during the game"""
            self.ships_left = self.settings.ship_limit
            self.score = 0
            self.level = 1

    def save_stats(self):
         save_high_score = open("highscore.txt", "w")
         save_high_score.write(str(self.high_score))

