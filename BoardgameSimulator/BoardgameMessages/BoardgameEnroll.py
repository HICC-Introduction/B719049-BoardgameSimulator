from BoardgameSimulator.Core import Point2
from BoardgameSimulator.Core import receive_message_from_process
from BoardgameSimulator.Core import send_message_to_process
from BoardgameSimulator.Enums import BoardgameMessageTypes
from BoardgameSimulator.BoardgameMessages import BoardgameMessage


class BoardgameEnroll(BoardgameMessage):
    def __init__(self):
        """
        [ BoardgamePlayer -> World ]
        Message used to enroll player into game entry list.

        Attributes:
            header              Header
            current_player_name BoardgamePlayer name, numbers and english, some symbols are allowed
            author              Programmer name
            creation_date       Build date
            version             Build version
        """
        super(BoardgameEnroll, self).__init__()
        self.header: str = BoardgameMessageTypes.Enroll
        self.current_player_name: str = ""
        self.author: str = ""
        self.creation_date: str = ""
        self.version: str = ""

    def print_information(self):
        property_names = [
            "header",
            "current_player_name",
            "author",
            "creation_date",
            "version",
        ]
        information_dictionary = self.create_information_dictionary_from_keyword(property_names)
        self.print_information_dictionary(information_dictionary)

    def receive_message_from_process(self) -> None:
        """
        Read message from process and parse into message itself.
        """
        super(BoardgameEnroll, self).receive_message_from_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_in = BoardgameMessage.std_in()

        self.current_player_name = receive_message_from_process(delim=delim, std_in=std_in)
        self.author = receive_message_from_process(delim=delim, std_in=std_in)
        self.creation_date = receive_message_from_process(delim=delim, std_in=std_in)
        self.version = receive_message_from_process(delim=end_of_message, std_in=std_in)

    def send_message_to_process(self) -> None:
        """
        Send message to process based on current message data.
        """
        super(BoardgameEnroll, self).send_message_to_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_out = BoardgameMessage.std_out()

        send_message_to_process(self.header, delim=delim, std_out=std_out)
        send_message_to_process(self.current_player_name, delim=delim, std_out=std_out)
        send_message_to_process(self.author, delim=delim, std_out=std_out)
        send_message_to_process(self.creation_date, delim=delim, std_out=std_out)
        send_message_to_process(self.version, delim=end_of_message, std_out=std_out)


if __name__ == "__main__":
    testMessage = BoardgameEnroll()
    testMessage.print_information()
    testMessage.send_message_to_process()
    print("EOF")
