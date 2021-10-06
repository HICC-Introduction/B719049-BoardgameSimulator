from BoardgameSimulator.BoardgameMessages import *
from BoardgameSimulator.Core import Point2
from BoardgamePlayer import PlayerACK
from BoardgamePlayer import Playerinfo
from BoardgamePlayer import Playerlogic
from BoardgameJudge import Judgelogic
from BoardgameJudge import JudgeACK
import sys

'''
1. Game Reset
Prepare : [World] -> [BoardgamePlayer]
Enroll : [BoardgamePlayer] -> [World]
ACK : [World] -> [BoardgamePlayer]
'''

# 설정
PlayerM = PlayerACK.GamePlayer_ACK()
PlayerIR = Playerlogic.info_repo()
PlayerL = Playerlogic.player_logic()
JudgeM = JudgeACK.GameJudge_ACK()
JudgeIR = Judgelogic.repo()
JudgeL = Judgelogic.judge_logic()

# prepare : BoardgamePrepare
# test : TicTacToe;3;3

def Pre():
    # get information from process
    prepare = BoardgamePrepare()
    prepare.receive_message_from_process()
    game_name = prepare.game_name
    row_count = prepare.row_count
    column_count = prepare.column_count

    # send info to Playerlogic
    PlayerIR.get_gameinfo(1,
        **{"game_name" : game_name,
           "row_count" : row_count,
           "column_count" : column_count
           }
    )

    # send header to PlayerACK
    PlayerM.get_header(prepare.header)
    return PlayerM.receive_from_process()

# enroll : BoardgameEnroll
# 랜덤으로 생성된 player에 대한 정보를 process로 전달

def Enr():
    enroll = BoardgameEnroll()

    # get info from Playerinfo
    Selected_player = Playerinfo.Player()
    enroll.current_player_name = Selected_player.Playerselect()
    enroll.author = Selected_player.author
    enroll.creation_date = Selected_player.creation_date
    enroll.version = Selected_player.version

    # send info to Playerlogic
    PlayerIR.get_gameinfo(2,**{"current_player_name" : Selected_player.Playerselect()})

    # send info to process
    enroll.send_message_to_process()

if Pre() == "ENR_OK":
    Enr()

def PreACK():
    # get ACK from process
    ACK_GameReset = BoardgameAcknowledgement()
    ACK_GameReset.receive_message_from_process()

    # send ACK to PlayerACK
    PlayerM.get_header(ACK_GameReset.header)
    return PlayerM.receive_from_process()


'''
2. Game Start
Start : [World] -> [BoardgamePlayer]
ACK : [BoardgamePlayer] -> [World]
'''

# Start : BoardgameStart
# test : 2;1;user1;0;3000;2;Park;0;5000

def gamestart():
    # get info from process
    Start = BoardgameStart()
    Start.receive_message_from_process()
    startheader = Start.header
    playernum = Start.total_player_count
    playerindex = Start.player_indexes
    playername = Start.player_names
    playertimeresettrigger = Start.timer_reset_triggers
    playertimelimit = Start.time_limit_milliseconds

    # send info to Playerlogic
    PlayerIR.get_gameinfo(2,
        **{"total_player_count" : playernum,
           "player_indexes" : playerindex,
           "player_names" : playername,
           "timer_reset_triggers" : playertimeresettrigger,
           "time_limit_milliseconds" : playertimelimit
           }
    )

    # send header to PlayerACK
    PlayerM.get_header(startheader)
    return PlayerM.receive_from_process()

Temp1 = ''
if PreACK() == "ACK_OK":
    Temp1 = gamestart()
    PlayerIR.get_myinfo()

def ACK_gamestart():
    ACK_Gamestart = BoardgameAcknowledgement()
    ACK_Gamestart.send_message_to_process()

# Start에 대한 정보를 전달받았으면 ACK message를 전송
if Temp1 == "STT_OK":
    ACK_gamestart()

'''
3-1. BoardgamePlayer Turn
MakeTurn : [World] -> [BoardgamePlayer]
ACK : [BoardgamePlayer] -> [World]
TurnResult : [BoardgamePlayer] -> [World]
'''

# MakeTurn : BoardgameRequestTurn
# test : 4000;3;3;0;0;0;2;0;0;0;0;0

def maketurn():
    # get info from process
    MakeTurn = BoardgameRequestTurn()
    MakeTurn.receive_message_from_process()

    TimeRemain = MakeTurn.remain_time_milliseconds
    row_num = MakeTurn.row_count
    column_num = MakeTurn.column_count
    board = MakeTurn.board_status

    # send info to Playerlogic
    PlayerIR.get_gameinfo(3,
        **{"remain_time_milliseconds" : TimeRemain,
           "row_count" : row_num,
           "column_count" : column_num,
           "board_status" : board,
           }
    )

    # send info to PlayerACK
    PlayerM.get_header(MakeTurn.header)
    return PlayerM.receive_from_process()

def ACK_maketurn():
    ACK_MakeTurn = BoardgameAcknowledgement()
    ACK_MakeTurn.send_message_to_process()

TempA = maketurn()
if TempA == "RQT_OK":
    ACK_maketurn()


# !!! MakeTurn Logic !!!









# TurnResult : BoardgameResponseTurn

def turnresult():
    TurnResult = BoardgameResponseTurn()

    # get info from Playerlogic
    playermove = PlayerL.playermove
    TurnResult.move=playermove

    # send info to process
    TurnResult.send_message_to_process()

turnresult()

'''
3-2. Other Turn
OtherTurn : [World] -> [BoardgamePlayer]
ACK : [BoardgamePlayer] -> [World]
'''

# OtherTurn : BoradgameNotifyOtherTurn
# test : 2;1;1;4000

def otherturn():
    # get info from process
    OtherTurn = BoardgameNotifyOtherTurn()
    OtherTurn.receive_message_from_process()
    player_index = OtherTurn.player_index
    move = OtherTurn.move
    remain_time_milliseconds = OtherTurn.remain_time_milliseconds

    # send info to Playerlogic
    PlayerIR.get_gameinfo(5,
        **{"player_index" : player_index,
           "move" : [move.x, move.y],
           "remain_time_milliseconds" : remain_time_milliseconds
           }
    )

    #send info to PlayerACK
    PlayerM.get_header(OtherTurn.header)
    return PlayerM.receive_from_process()

def ACK_otherturn():
    ACK_Other = BoardgameAcknowledgement()
    ACK_Other.send_message_to_process()

TempB = otherturn()
if TempB == "TRN_OK":
    ACK_otherturn()


'''
3-3. Request judge
RequestJudge : [World] -> [BoardgameJudge]
ACK : [BoardgameJudge] -> [World]
ReturnJudge : [BoardgameJudge] -> [World]
'''

# RequestJudge : BoardgameRequestJudgement
# test : 2;1;2;3;3;1;1;2;1;2;1;2;1;2

def requestjudge():
    # get info from process
    RequestJudge = BoardgameRequestJudgement()
    RequestJudge.receive_message_from_process()

    playernum2 = RequestJudge.total_player_count
    playerindex2 = RequestJudge.player_indexes
    row_count2 = RequestJudge.row_count
    column_count2 = RequestJudge.column_count
    boardstatus = RequestJudge.board_status

    # send info to Judgelogic
    JudgeIR.get_gameinfo2(
        *boardstatus,
        **{"total_player_count" : playernum2,
           "player_indexes" : playerindex2,
           "row_count" : row_count2,
           "column_count" : column_count2,
           }
    )

    # send info to JudgeACK
    JudgeM.get_header2(RequestJudge.header)
    return JudgeM.receive_from_process2()

def ACK_judgerequest():
    ACK_Judgerequest = BoardgameAcknowledgement()
    ACK_Judgerequest.send_message_to_process()

Temp2 = requestjudge()
if Temp2 == "RQJ_OK":
    ACK_judgerequest()

# !!! BoardgameJudge logic !!!







# ReturnJudge : BoardgameResponseJudgement
def returnjudge():
    ReturnJudge = BoardgameResponseJudgement()
    GameResult = JudgeL

    # send info to process
    ReturnJudge.is_game_end = GameResult.is_game_end
    ReturnJudge.win_player_count = GameResult.win_player_count
    ReturnJudge.win_player_indexes = GameResult.win_player_indexes
    ReturnJudge.lose_player_count = GameResult.lose_player_count
    ReturnJudge.lose_player_indexes = GameResult.lose_player_indexes
    ReturnJudge.win_by = GameResult.win_by
    ReturnJudge.send_message_to_process()

    return GameResult.is_game_end

isgameend = returnjudge()

'''
4. Game End
GameEnd : [World] -> [BoardgamePlayer]
ACK : [BoardgamePlayer] -> [World]
'''

# GameEnd : BoardgameEnd
# test : 1;1;1;2

def gameend():
    # get info from process
    GameEnd = BoardgameEnd()
    GameEnd.receive_message_from_process()

    win_player_count = GameEnd.win_player_count
    win_player_indexes = GameEnd.win_player_indexes
    lose_player_count = GameEnd.lose_player_count
    lose_player_indexes = GameEnd.lose_player_indexes
    win_by = GameEnd.win_by

    # send info to Playerlogic
    PlayerIR.get_gameinfo(4,
        **{"win_player_count" : win_player_count,
           "win_player_indexes" : win_player_indexes,
           "lose_player_count" : lose_player_count,
           "lose_player_indexes": lose_player_indexes,
           "win_by": win_by
           }
    )
    PlayerIR.get_myresult()

    # send header to PlayerACK
    PlayerM.get_header(GameEnd.header)
    return PlayerM.receive_from_process()

def ACK_gameend():
    ACK_Gameend = BoardgameAcknowledgement()
    ACK_Gameend.send_message_to_process()

if isgameend == True:
    Temp3 = gameend()
    if Temp3 == "END_OK":
        ACK_gameend()

'''
5. Game Terminate
GameTerminate : [World] -> [BoardgamePlayer]
'''

# GameTerminate : BoardgameTerminate
GameTerminate = BoardgameTerminate()
GameTerminate.receive_message_from_process()
PlayerM.get_header(GameTerminate.header)
if PlayerM.receive_from_process() == "EXT_OK":
    # while로 빠져나가게 할 수도 있지만, 현재로서는 복잡해지므로 일단 sys 모듈을 import하여 사용
    sys.exit()




