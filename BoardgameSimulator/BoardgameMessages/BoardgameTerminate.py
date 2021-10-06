from BoardgameSimulator.Core import send_message_to_process
from BoardgameSimulator.Enums import BoardgameMessageTypes
from BoardgameSimulator.BoardgameMessages import BoardgameMessage


class BoardgameTerminate(BoardgameMessage):
    def __init__(self):
        """
        [ World -> Everyone ]
        Notification message for monitoring program termination.

        Attributes:
            header  Header
        """
        super(BoardgameTerminate, self).__init__()
        self.header: str = BoardgameMessageTypes.Terminate

    def print_information(self):
        property_names = [
            "header",
        ]
        information_dictionary = self.create_information_dictionary_from_keyword(property_names)
        self.print_information_dictionary(information_dictionary)

    def receive_message_from_process(self) -> None:
        """
        Read message from process and parse into message itself.
        """
        super(BoardgameTerminate, self).receive_message_from_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_in = BoardgameMessage.std_in()

    def send_message_to_process(self) -> None:
        """
        Send message to process based on current message data.
        """
        super(BoardgameTerminate, self).send_message_to_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_out = BoardgameMessage.std_out()

        send_message_to_process(self.header, delim=end_of_message, std_out=std_out)


if __name__ == "__main__":
    testMessage = BoardgameTerminate()
    testMessage.send_message_to_process()
    print("EOF")
