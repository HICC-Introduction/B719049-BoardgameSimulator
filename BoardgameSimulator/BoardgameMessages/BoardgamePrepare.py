from BoardgameSimulator.Core import receive_message_from_process
from BoardgameSimulator.Core import send_message_to_process
from BoardgameSimulator.Enums import BoardgameMessageTypes
from BoardgameSimulator.BoardgameMessages import BoardgameMessage


class BoardgamePrepare(BoardgameMessage):
    def __init__(self):
        """
        [ World -> BoardgamePlayer ]
        Background information of current boardgame.

        Attributes:
            header          Header
            game_name       Name of game
            row_count       Board row count
            column_count    Board column count
        """
        super(BoardgamePrepare, self).__init__()
        self.header: str = BoardgameMessageTypes.Prepare
        self.game_name: str = ""
        self.row_count: int = 0
        self.column_count: int = 0

    def print_information(self):
        property_names = [
            "header",
            "game_name",
            "row_count",
            "column_count",
        ]
        information_dictionary = self.create_information_dictionary_from_keyword(property_names)
        self.print_information_dictionary(information_dictionary)

    def receive_message_from_process(self) -> None:
        """
        Read message from process and parse into message itself.
        """
        super(BoardgamePrepare, self).receive_message_from_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_in = BoardgameMessage.std_in()

        self.game_name = receive_message_from_process(delim=delim, std_in=std_in)
        self.row_count = int(receive_message_from_process(delim=delim, std_in=std_in))
        self.column_count = int(receive_message_from_process(delim=end_of_message, std_in=std_in))

    def send_message_to_process(self) -> None:
        """
        Send message to process based on current message data.
        """
        super(BoardgamePrepare, self).send_message_to_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_out = BoardgameMessage.std_out()

        send_message_to_process(self.header, delim=delim, std_out=std_out)
        send_message_to_process(self.game_name, delim=delim, std_out=std_out)
        send_message_to_process(self.row_count, delim=end_of_message, std_out=std_out)
        send_message_to_process(self.column_count, delim=end_of_message, std_out=std_out)


if __name__ == "__main__":
    testMessage = BoardgamePrepare()
    print(testMessage.__getattribute__("header"))
    testMessage.send_message_to_process()
    print("EOF")
