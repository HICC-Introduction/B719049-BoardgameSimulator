from BoardgameSimulator.Core import Point2
from BoardgameSimulator.Core import receive_message_from_process
from BoardgameSimulator.Core import send_message_to_process
from BoardgameSimulator.Enums import BoardgameMessageTypes
from BoardgameSimulator.BoardgameMessages import BoardgameMessage


class BoardgameNotifyOtherTurn(BoardgameMessage):
    def __init__(self):
        """
        [ World -> BoardgamePlayer ]
        Information message about other players move.

        Attributes:
            header                      Header
            player_index                BoardgamePlayer number
            move                        Given player's move
            remain_time_milliseconds    Given player's remaining time, in milliseconds
        """
        super(BoardgameNotifyOtherTurn, self).__init__()
        self.header: str = BoardgameMessageTypes.NotifyOtherTurn
        self.player_index: int = 0
        self.move: Point2 = Point2(0, 0)
        self.remain_time_milliseconds: int = 0

    def print_information(self):
        property_names = [
            "header",
            "player_index",
            "move",
            "remain_time_milliseconds",
        ]
        information_dictionary = self.create_information_dictionary_from_keyword(property_names)
        self.print_information_dictionary(information_dictionary)

    def receive_message_from_process(self) -> None:
        """
        Read message from process and parse into message itself.
        """
        super(BoardgameNotifyOtherTurn, self).receive_message_from_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_in = BoardgameMessage.std_in()

        self.player_index = int(receive_message_from_process(delim=delim, std_in=std_in))
        given_x = int(receive_message_from_process(delim=delim, std_in=std_in))
        given_y = int(receive_message_from_process(delim=delim, std_in=std_in))
        self.move = Point2(given_x, given_y)
        self.remain_time_milliseconds = int(receive_message_from_process(delim=end_of_message, std_in=std_in))

    def send_message_to_process(self) -> None:
        """
        Send message to process based on current message data.
        """
        super(BoardgameNotifyOtherTurn, self).send_message_to_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_out = BoardgameMessage.std_out()

        send_message_to_process(self.header, delim=delim, std_out=std_out)
        send_message_to_process(self.player_index, delim=delim, std_out=std_out)
        send_message_to_process(self.move.x, delim=delim, std_out=std_out)
        send_message_to_process(self.move.y, delim=delim, std_out=std_out)
        send_message_to_process(self.remain_time_milliseconds, delim=end_of_message, std_out=std_out)


if __name__ == "__main__":
    testMessage = BoardgameNotifyOtherTurn()
    testMessage.send_message_to_process()
    print("EOF")
