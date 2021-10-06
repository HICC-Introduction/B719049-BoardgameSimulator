from BoardgameSimulator.Core import send_message_to_process
from BoardgameSimulator.Enums import BoardgameMessageTypes
from BoardgameSimulator.BoardgameMessages import BoardgameMessage


class BoardgameAcknowledgement(BoardgameMessage):
    def __init__(self):
        """
        [ World -> Everyone ] [ Everyone -> World ]
        Message used as reply, acknowledgement.

        Attributes:
             header Header
        """
        super(BoardgameAcknowledgement, self).__init__()
        self.header: str = BoardgameMessageTypes.Acknowledgement

    def print_information(self):
        property_names = [
            "header",
        ]
        information_dictionary = self.create_information_dictionary_from_keyword(property_names)
        self.print_information_dictionary(information_dictionary)

    def receive_message_from_process(self) -> None:
        """
        Read message from process and parse into message itself
        """
        super(BoardgameAcknowledgement, self).receive_message_from_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_in = BoardgameMessage.std_in()

    def send_message_to_process(self) -> None:
        """
        Send message to process based on current message data
        """
        super(BoardgameAcknowledgement, self).send_message_to_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_out = BoardgameMessage.std_out()

        send_message_to_process(self.header, delim=end_of_message, std_out=std_out)


if __name__ == "__main__":
    testMessage = BoardgameAcknowledgement()
    testMessage.print_information()
    testMessage.send_message_to_process()
    print("EOF")
