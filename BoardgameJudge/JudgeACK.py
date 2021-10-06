from BoardgameSimulator.Enums import BoardgameMessageTypes

class GameJudge_ACK:
    def __init__(self):
        '''
        This module imitates the process of confirming any work done by human.
        header temporary in here
        '''
        self.header_temp2 = ''

    def get_header2(self, header):
        self.header_temp2 = header

    def receive_from_process2(self):
        '''

        header list :
        RQJ

        '''
        if self.header_temp2 == BoardgameMessageTypes.RequestJudgement:
            return "RQJ_OK"

    def send_to_process(self, header_s):
        '''

        header list :
        RPJ

        '''
        if header_s == BoardgameMessageTypes.ResponseJudgement:
            return "RPJ_OK"


