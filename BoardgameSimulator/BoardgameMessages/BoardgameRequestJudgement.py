from typing import List

from BoardgameSimulator.Core import receive_message_from_process
from BoardgameSimulator.Core import send_message_to_process
from BoardgameSimulator.Enums import BoardgameMessageTypes
from BoardgameSimulator.BoardgameMessages import BoardgameMessage


class BoardgameRequestJudgement(BoardgameMessage):
    def __init__(self):
        """
        [ World -> BoardgameJudge ]
        Request for judge whether game is over or not.

        Attributes:
            header          Header
            total_player_count  Count of every enrolled player
            player_indexes      BoardgamePlayer number for each player, Same order as player_names
            row_count           Board row count (Expected not to be use, still remains for future development)
            column_count        Board column count (Expected not to be use, still remains for future development)
            board_status        Board status as list of list, including blanks
        """
        super(BoardgameRequestJudgement, self).__init__()
        self.header: str = BoardgameMessageTypes.RequestJudgement
        self.total_player_count: int = 0
        self.player_indexes: List[int] = []
        self.row_count: int = 0
        self.column_count: int = 0
        self.board_status: List[List[int]] = [[]]

    def print_information(self):
        property_names = [
            "header",
            "total_player_count",
            "player_indexes",
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
        super(BoardgameRequestJudgement, self).receive_message_from_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_in = BoardgameMessage.std_in()

        self.player_indexes = []
        self.board_status = [[]]

        self.total_player_count = int(receive_message_from_process(delim=delim, std_in=std_in))
        for i in range(self.total_player_count):
            self.player_indexes.append(int(receive_message_from_process(delim=delim, std_in=std_in)))

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
        super(BoardgameRequestJudgement, self).send_message_to_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_out = BoardgameMessage.std_out()

        send_message_to_process(self.header, delim=delim, std_out=std_out)
        send_message_to_process(self.row_count, delim=delim, std_out=std_out)
        send_message_to_process(self.column_count, delim=delim, std_out=std_out)

        for i in range(self.row_count):
            for j in range(self.column_count):
                send_message_to_process(
                    self.board_status[i][j],
                    delim=delim if (i + 1) * (j + 1) != (self.row_count * self.column_count) else end_of_message,
                    std_out=std_out)


if __name__ == "__main__":
    testMessage = BoardgameRequestJudgement()
    testMessage.row_count = 2
    testMessage.column_count = 3
    testMessage.board_status = [[1, 2, 0], [0, 0, 1]]
    testMessage.send_message_to_process()
    print("EOF")
