from BoardgameSimulator.Core import Point2
from BoardgameSimulator.Core import receive_message_from_process
from BoardgameSimulator.Core import send_message_to_process
from BoardgameSimulator.Enums import BoardgameMessageTypes
from BoardgameSimulator.BoardgameMessages import BoardgameMessage


class BoardgameResponseTurn(BoardgameMessage):
    def __init__(self):
        """
        [ BoardgamePlayer -> World ]
        Response message in return of turn-request.

        Attributes:
            header  Header
            move    BoardgamePlayer's next move
        """
        super(BoardgameResponseTurn, self).__init__()
        self.header: str = BoardgameMessageTypes.RequestTurn
        self.move: Point2 = Point2()

    def print_information(self):
        property_names = [
            "header",
            "move",
        ]
        information_dictionary = self.create_information_dictionary_from_keyword(property_names)
        self.print_information_dictionary(information_dictionary)

    def receive_message_from_process(self) -> None:
        """
        Read message from process and parse into message itself.
        """
        super(BoardgameResponseTurn, self).receive_message_from_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_in = BoardgameMessage.std_in()

        x = int(receive_message_from_process(delim=delim, std_in=std_in))
        y = int(receive_message_from_process(delim=end_of_message, std_in=std_in))
        self.move = Point2(x, y)

    def send_message_to_process(self) -> None:
        """
        Send message to process based on current message data.
        """
        super(BoardgameResponseTurn, self).send_message_to_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_out = BoardgameMessage.std_out()

        send_message_to_process(self.header, delim=delim, std_out=std_out)
        send_message_to_process(self.move.x, delim=delim, std_out=std_out)
        send_message_to_process(self.move.y, delim=end_of_message, std_out=std_out)


if __name__ == "__main__":
    testMessage = BoardgameResponseTurn()
    testMessage.remainTimeMilliseconds = 100
    testMessage.rowCount = 2
    testMessage.columnCount = 3
    testMessage.boardStatus = [[1, 2, 0], [0, 0, 1]]
    testMessage.send_message_to_process()
    print("EOF")
