from BoardgameSimulator.Core import Point2

boardtempP = ''


class info_repo:
    def __init__(self):
        '''
        gameinfo                basic information about game
        playerinfo              information about player
        playinfo                information about actual game playing
        resultinfo              information about game result
        otherplayergameinfo     information about other player's turn
        board                   information about board

        win                     count how many my player win
        lose                    count how many my player lose
        draw                    count how many my player draw
        '''

        self.gameinfo = {}
        self.playerinfo = {}
        self.playinfo = {}
        self.resultinfo = {}
        self.otherplayergameinfo = {}
        self.board = ''

        self.win :int = 0
        self.lose : int = 0
        self.draw : int = 0

    def get_gameinfo(self, n, **kwargs):
        if n == 1:
            for i in kwargs.keys():
                self.gameinfo[i] = kwargs[i]

        if n == 2:
            for j in kwargs.keys():
                self.playerinfo[j] = kwargs[j]

        if n == 3:
            for k in kwargs.keys():
                if k != "board_status":
                    self.playinfo[k] = kwargs[k]
                else:
                    self.board = kwargs[k]
                    global boardtempP
                    boardtempP = self.board

        if n == 4:
            for l in kwargs.keys():
                self.resultinfo[l] = kwargs[l]

        if n == 5:
            for m in kwargs.keys():
                self.otherplayergameinfo[m] = kwargs[m]

    def get_myinfo(self):
        '''
        myname              my player's name
        mynum               my player's index number(which uses for list indexing)
        myindex             my player's index
        mytimelimit         my player's time limit in milliseconds
        '''

        self.myname = self.playerinfo["current_player_name"]
        self.mynum = self.playerinfo["player_names"].index(self.myname)
        self.myindex = self.playerinfo["player_indexes"][self.mynum]
        self.mytimelimit = self.playerinfo["time_limit_milliseconds"][self.mynum]

    def get_myresult(self):
        if self.myindex in self.resultinfo["win_player_indexes"]:
            self.win += 1
        elif self.myindex in self.resultinfo["lose_player_indexes"]:
            self.lose += 1
        else:
            self.draw += 1

class player_logic:
    def __init__(self):
        self.playermove = Point2(0,0)
        self.boardresult = ''

    def logicP(self):
        board_use = boardtempP
        pass


if __name__ == "__main__":
    printlogic = info_repo()
    print(printlogic.gameinfo)