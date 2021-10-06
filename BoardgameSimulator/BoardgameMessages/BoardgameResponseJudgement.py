from typing import Sequence

from BoardgameSimulator.Core import receive_message_from_process
from BoardgameSimulator.Core import send_message_to_process
from BoardgameSimulator.Enums import BoardgameMessageTypes
from BoardgameSimulator.BoardgameMessages import BoardgameMessage


class BoardgameResponseJudgement(BoardgameMessage):
    def __init__(self):
        """
        [ BoardgameJudge -> World ]
        Response message in return of request of judgement-request.

        Attributes:
            header              Header
            is_game_end         Whether the game is end
            win_player_count    Number of players won
            win_players         List of players won
            lose_player_count   Number of players lose
            lose_players        List of players lose
            win_by              Cause of win
        """
        super(BoardgameResponseJudgement, self).__init__()
        self.header: str = BoardgameMessageTypes.ResponseJudgement
        self.is_game_end: bool = False
        self.win_player_count: int = 0
        self.win_player_indexes: Sequence[int] = []
        self.lose_player_count: int = 0
        self.lose_player_indexes: Sequence[int] = []
        self.win_by: int = 0

    def print_information(self):
        property_names = [
            "header",
            "is_game_end",
            "win_player_count",
            "win_player_indexes",
            "lose_player_count",
            "lose_player_indexes",
            "win_by"
        ]
        information_dictionary = self.create_information_dictionary_from_keyword(property_names)
        self.print_information_dictionary(information_dictionary)

    def receive_message_from_process(self) -> None:
        """
        Read message from process and parse into message itself.
        """
        super(BoardgameResponseJudgement, self).receive_message_from_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_in = BoardgameMessage.std_in()

        self.win_player_indexes = []
        self.lose_player_indexes = []

        self.is_game_end = bool(receive_message_from_process(delim=delim, std_in=std_in))
        self.win_player_count = int(receive_message_from_process(delim=delim, std_in=std_in))
        for i in range(self.win_player_count):
            self.win_player_indexes.append(int(receive_message_from_process(delim=delim, std_in=std_in)))

        self.lose_player_count = int(receive_message_from_process(delim=delim, std_in=std_in))
        for i in range(self.lose_player_count):
            if i != self.lose_player_count - 1:
                self.lose_player_indexes.append(int(receive_message_from_process(delim=delim, std_in=std_in)))
            else:
                self.lose_player_indexes.append(int(receive_message_from_process(delim=end_of_message, std_in=std_in)))

    def send_message_to_process(self) -> None:
        """
        Send message to process based on current message data.
        """
        super(BoardgameResponseJudgement, self).send_message_to_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_out = BoardgameMessage.std_out()

        send_message_to_process(self.header, delim=delim, std_out=std_out)
        send_message_to_process(int(self.is_game_end), delim=delim, std_out=std_out)
        send_message_to_process(self.win_player_count, delim=delim, std_out=std_out)
        for i in range(self.win_player_count):
            send_message_to_process(self.win_player_indexes[i], delim=delim, std_out=std_out)

        send_message_to_process(self.lose_player_count, delim=delim, std_out=std_out)
        for i in range(self.lose_player_count):
            if i != self.lose_player_count - 1:
                send_message_to_process(self.lose_player_indexes[i], delim=delim, std_out=std_out)
            else:
                send_message_to_process(self.lose_player_indexes[i], delim=end_of_message, std_out=std_out)


if __name__ == "__main__":
    testMessage = BoardgameResponseJudgement()
    testMessage.is_game_end = True
    testMessage.win_player_count = 5
    testMessage.win_player_indexes = [1, 2, 3, 5, 4]
    testMessage.lose_player_count = 2
    testMessage.lose_player_indexes = [6, 7]
    testMessage.send_message_to_process()
    testMessage.receive_message_from_process()
    testMessage.send_message_to_process()
