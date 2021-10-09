'''
All variable below this line is Global variable. Share with all class.
boardtemp               info about game board
gameinfo2               info about game
'''
boardtempJ = ''
gameinfo2 = {}

class repo:
    def __init__(self):
        '''
        board               info about game board - for backup
        '''

        self.board = []

    def get_gameinfo2(self, *args, **kwargs):
        global boardtempJ
        global gameinfo2

        self.board = args
        boardtempJ = self.board
        for i in kwargs.keys():
            gameinfo2[i] = kwargs[i]

class judge_logic:
    # 심판
    def __init__(self):
        self.is_game_end : bool = False
        self.win_player_count = 1
        self.win_player_indexes = [1]
        self.lose_player_count = 1
        self.lose_player_indexes = [2]
        self.win_by = 0

    def logic(self):
        self.boardT = list(boardtempJ)

        Boardfullvalue = 0
        for i in self.boardT:
            for j in i:
                if j != 0:
                    pass
                else:
                    Boardfullvalue += 1

        indexes = gameinfo2["player_indexes"]

        def get_winner(board, index1, index2):
            # test all possibilities
            if ((board[0][0]==index1 and board[0][1]==index1 and board[0][2]==index1) or
                (board[1][0]==index1 and board[1][1]==index1 and board[1][2]==index1) or
                (board[2][0]==index1 and board[2][1]==index1 and board[2][2]==index1) or
                    (board[0][0]==index1 and board[1][0]==index1 and board[2][0]==index1) or
                    (board[0][1]==index1 and board[1][1]==index1 and board[2][1]==index1) or
                    (board[0][2]==index1 and board[1][2]==index1 and board[2][2]==index1) or
                    (board[0][0]==index1 and board[1][1]==index1 and board[2][2]==index1) or
                    (board[2][0]==index1 and board[1][1]==index1 and board[0][2]==index1)):
                return [True, index1]

            # test all possibilities
            elif ((board[0][0]==index2 and board[0][1]==index2 and board[0][2]==index2) or
                (board[1][0]==index2 and board[1][1]==index2 and board[1][2]==index2) or
                (board[2][0]==index2 and board[2][1]==index2 and board[2][2]==index2) or
                    (board[0][0]==index2 and board[1][0]==index2 and board[2][0]==index2) or
                    (board[0][1]==index2 and board[1][1]==index2 and board[2][1]==index2) or
                    (board[0][2]==index2 and board[1][2]==index2 and board[2][2]==index2) or
                    (board[0][0]==index2 and board[1][1]==index2 and board[2][2]==index2) or
                    (board[2][0]==index2 and board[1][1]==index2 and board[0][2]==index2)):
                return [True, index2]

            # if there is no winner
            else:
                if Boardfullvalue == 0:
                    # board is full.
                    # there is no winner, result is draw
                    return [False, "Draw"]

                elif Boardfullvalue > 0:
                    # board is not full.
                    # game is not finished, so game should resume
                    return [False, "GameResume"]

        result = get_winner(self.boardT, indexes[0],indexes[1])

        # process for game end
        if result[0] == True:
            self.is_game_end = True
            self.win_player_count = 1
            self.win_player_indexes = [result[1]]
            self.lose_player_count = 1
            index_temp = indexes.remove(result[1])
            self.lose_player_indexes = indexes

        # if there is no winner
        elif result[0] == False:
            # if result is Draw
            # 무승부의 경우 결과처리를 어떻게 해야할 지?
            if result[1] == "Draw":
                self.is_game_end = True
                self.win_player_count = 0
                self.win_player_indexes = []
                self.lose_player_count = 0
                self.lose_player_indexes = []

            # if result is GameResume
            if result[1] == "GameResume":
                self.is_game_end = False
                self.win_player_count = 0
                self.win_player_indexes = []
                self.lose_player_count = 0
                self.lose_player_indexes = []













