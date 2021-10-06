from BoardgameSimulator.Enums import BoardgameMessageTypes

class GamePlayer_ACK:

    def __init__(self):
        '''
        This module imitates the process of confirming any work done by human.
        header temporary in here
        '''
        self.header_temp = ''

    def get_header(self, header):
        self.header_temp = header

    def header_for_playing(self, header_p):
        if header_p == BoardgameMessageTypes.RequestTurn:
            pass
            '''
            This is not used.
            Still remains for future development
            '''

    def receive_from_process(self):
        '''
        :return:    player recognizes about message and returns about "good to go"

        header list :
        ACK
        PRE
        STT
        END
        EXT
        RQT
        TRN

        '''
        # 누군가로부터 player에게 ACK 메세지를 보냈을 경우
        if self.header_temp == BoardgameMessageTypes.Acknowledgement:
            return "ACK_OK"

        # prepare message를 받았을 경우
        if self.header_temp == BoardgameMessageTypes.Prepare:
            return self.send_to_process(BoardgameMessageTypes.Enroll)

        # start message를 받았을 경우
        if self.header_temp == BoardgameMessageTypes.Start:
            return "STT_OK"

        # End message를 받았을 경우
        if self.header_temp == BoardgameMessageTypes.End:
            return "END_OK"

        # terminate message를 받았을 경우
        if self.header_temp == BoardgameMessageTypes.Terminate:
            return "EXT_OK"

        # turn 진행 message를 받았을 경우
        if self.header_temp == BoardgameMessageTypes.RequestTurn:
            self.header_for_playing(self.header_temp)
            return "RQT_OK"

        # otherturn message를 받았을 경우
        if self.header_temp == BoardgameMessageTypes.NotifyOtherTurn:
            return "TRN_OK"

    def send_to_process(self, header_s):
        '''
        :param header_s:    header that player should send message
        :return:            text that what header should be used

        header list :
        ENR
        '''

        # enroll message를 보내야 하는 경우
        if header_s == BoardgameMessageTypes.Enroll:
            return "ENR_OK"

if __name__ == "__main__":
    pass


