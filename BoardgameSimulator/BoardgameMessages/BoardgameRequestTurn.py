from typing import Sequence

from BoardgameSimulator.Core import receive_message_from_process
from BoardgameSimulator.Core import send_message_to_process
from BoardgameSimulator.Enums import BoardgameMessageTypes
from BoardgameSimulator.BoardgameMessages import BoardgameMessage


class BoardgameRequestTurn(BoardgameMessage):
    def __init__(self):
        """
        [ World -> BoardgamePlayer ]
        Request for making single move.

        Attributes:
            header                      Header
            remain_time_milliseconds    Currently remaining time for player, in milliseconds
            row_count                   Board row count
            column_count                Board column count
            board_status                Board status as list of list, including blanks
        """
        super(BoardgameRequestTurn, self).__init__()
        self.header: str = BoardgameMessageTypes.RequestTurn
        self.remain_time_milliseconds: int = 0
        self.row_count: int = 0
        self.column_count: int = 0
        self.board_status: Sequence[Sequence[int]] = [[]]

    def print_information(self):
        property_names = [
            "header",
            "remain_time_milliseconds",
            "row_count",
            "column_count",
            "board_status",
        ]
        information_dictionary = self.create_information_dictionary_from_keyword(property_names)
        self.print_information_dictionary(information_dictionary)

    def receive_message_from_process(self) -> None:
        """
        Read message from process and parse into message itself.
        """
        super(BoardgameRequestTurn, self).receive_message_from_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_in = BoardgameMessage.std_in()

        self.remain_time_milliseconds = int(receive_message_from_process(delim=delim, std_in=std_in))
        self.row_count = int(receive_message_from_process(delim=delim, std_in=std_in))
        self.column_count = int(receive_message_from_process(delim=delim, std_in=std_in))
        self.board_status = [[] for _ in range(self.column_count)]

        for i in range(self.row_count):
            for j in range(self.column_count):
                self.board_status[i].append(int(receive_message_from_process(
                    delim=delim if (i + 1) * (j + 1) != (self.row_count * self.column_count) else end_of_message,
                    std_in=std_in)))

    def send_message_to_process(self) -> None:
        """
        Send message to process based on current message data.
        """
        super(BoardgameRequestTurn, self).send_message_to_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_out = BoardgameMessage.std_out()

        send_message_to_process(self.header, delim=delim, std_out=std_out)
        send_message_to_process(self.remain_time_milliseconds, delim=delim, std_out=std_out)
        send_message_to_process(self.row_count, delim=delim, std_out=std_out)
        send_message_to_process(self.column_count, delim=delim, std_out=std_out)

        for i in range(self.row_count):
            for j in range(self.column_count):
                send_message_to_process(
                    self.board_status[i][j],
                    delim=delim if (i + 1) * (j + 1) != (self.row_count * self.column_count) else end_of_message,
                    std_out=std_out)


if __name__ == "__main__":
    testMessage = BoardgameRequestTurn()
    testMessage.remain_time_milliseconds = 100
    testMessage.row_count = 2
    testMessage.column_count = 3
    testMessage.board_status = [[1, 2, 0], [0, 0, 1]]
    testMessage.send_message_to_process()
    print("EOF")
