import sys
from _io import TextIOWrapper
recieve = 1

class BoardgameMessage:
    __delim: str = ';'
    __end_of_message: str = '\n'
    __std_in: [sys.stdin, TextIOWrapper] = sys.stdin
    __std_out: [sys.stdout, TextIOWrapper] = sys.stdout
    __information_key_length: int = 32

    def __init__(self):
        """
        [ UNUSED ]
        Message base structure. User MUST NOT use this class.

        Attributes:
            __delim             Message delimiter
            __end_of_message    Message end character
            __std_in            Standard input
            __std_out           Standard output
        """
        self.header: str = ""

    def print_information(self) -> None:
        pass

    def create_information_dictionary_from_keyword(self, keywords: list):
        information_dictionary: dict = dict()
        for keyword in keywords:
            information_dictionary[keyword] = self.__getattribute__(keyword)
        return information_dictionary

    def print_information_dictionary(self, info_dictionary: dict):
        for item in info_dictionary.items():
            print(f"{item[0]:{BoardgameMessage.information_key_length()}}{item[1]}")

    def receive_message_from_process(self) -> None:
        """
        Read message from process and parse into message itself.
        """
        pass

    def send_message_to_process(self) -> None:
        """
        Send message to process based on current message data.
        """
        pass

    @classmethod
    def delim(cls):
        return cls.__delim

    @classmethod
    def end_of_message(cls):
        return cls.__end_of_message

    @classmethod
    def std_in(cls):
        return cls.__std_in

    @classmethod
    def std_out(cls):
        return cls.__std_out

    @classmethod
    def information_key_length(cls):
        return cls.__information_key_length
