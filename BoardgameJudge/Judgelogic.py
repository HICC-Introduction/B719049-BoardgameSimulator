class repo:
    def __init__(self):
        '''
        gameinfo2           info about game
        board               info about game board
        '''
        self.gameinfo2 = {}
        self.board = []

    def get_gameinfo2(self, *args, **kwargs):
        self.board = args
        for i in kwargs.keys():
            self.gameinfo2[i] = kwargs[i]

class judge_logic:
    def __init__(self):
        self.is_game_end : bool = True
        self.win_player_count = 1
        self.win_player_indexes = [1]
        self.lose_player_count = 1
        self.lose_player_indexes = [2]
        self.win_by = 0

    def logic(self):
        '''
        This is not used.
        Still remains for future development.
        '''






