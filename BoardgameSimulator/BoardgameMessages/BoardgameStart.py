from typing import Sequence

from BoardgameSimulator.Core import receive_message_from_process
from BoardgameSimulator.Core import send_message_to_process
from BoardgameSimulator.Enums import BoardgameMessageTypes
from BoardgameSimulator.BoardgameMessages import BoardgameMessage


class BoardgameStart(BoardgameMessage):
    def __init__(self):
        """
        [ World -> Everyone ]
        Notification message of game start.

        Attributes:
            header                  Header
            total_player_count      Count of every enrolled player
            player_indexes          BoardgamePlayer number for each player, Same order as player_names
            player_names            BoardgamePlayer name for each player, Same order as player_numbers
            timer_reset_triggers    Condition for timer reset for each player, Same order as player_numbers
            time_limit_milliseconds Initial time limit for each player, Same order as player_numbers
        """
        super(BoardgameStart, self).__init__()
        self.header: str = BoardgameMessageTypes.Start
        self.total_player_count: int = 0
        self.player_indexes: Sequence[int] = []
        self.player_names: Sequence[int] = []
        self.timer_reset_triggers: Sequence[int] = []
        self.time_limit_milliseconds: Sequence[int] = []

        def print_information(self):
            property_names = [
                "header",
                "total_player_count",
                "player_indexes",
                "player_names",
                "times_reset_triggers",
                "time_limit_milliseconds",
            ]
            information_dictionary = self.create_information_dictionary_from_keyword(property_names)
            self.print_information_dictionary(information_dictionary)

    def receive_message_from_process(self) -> None:
        """
        Read message from process and parse into message itself.
        """
        super(BoardgameStart, self).receive_message_from_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_in = BoardgameMessage.std_in()

        self.player_indexes = []
        self.player_names = []
        self.timer_reset_triggers = []
        self.time_limit_milliseconds = []

        self.total_player_count = int(receive_message_from_process(delim=delim, std_in=std_in))
        for i in range(self.total_player_count):
            self.player_indexes.append(int(receive_message_from_process(delim=delim, std_in=std_in)))
            self.player_names.append(receive_message_from_process(delim=delim, std_in=std_in))
            self.timer_reset_triggers.append(int(receive_message_from_process(delim=delim, std_in=std_in)))
            self.time_limit_milliseconds.append(int(receive_message_from_process(
                delim=delim if i != self.total_player_count - 1 else end_of_message, std_in=std_in)))

    def send_message_to_process(self) -> None:
        """
        Send message to process based on current message data.
        """
        super(BoardgameStart, self).send_message_to_process()

        delim = BoardgameMessage.delim()
        end_of_message = BoardgameMessage.end_of_message()
        std_out = BoardgameMessage.std_out()

        send_message_to_process(self.header, delim=delim, std_out=std_out)
        send_message_to_process(self.total_player_count, delim=delim, std_out=std_out)
        for i in range(self.total_player_count):
            send_message_to_process(self.player_indexes[i], delim=delim, std_out=std_out)
            send_message_to_process(self.player_names[i], delim=delim, std_out=std_out)
            send_message_to_process(self.timer_reset_triggers[i], delim=delim, std_out=std_out)
            if i != self.total_player_count - 1:
                send_message_to_process(self.time_limit_milliseconds[i], delim=delim, std_out=std_out)
            else:
                send_message_to_process(self.time_limit_milliseconds[i], delim=end_of_message, std_out=std_out)


if __name__ == "__main__":
    testMessage = BoardgameStart()
    testMessage.total_player_count = 5
    testMessage.player_indexes = [1, 2, 3, 5, 4]
    testMessage.player_names = ["joe", "john", "kim", "heo", "kli"]
    testMessage.timer_reset_triggers = [0, 0, 0, 0, 0]
    testMessage.time_limit_milliseconds = [1000, 2000, 1000, 2000, 50000]
    testMessage.send_message_to_process()
    testMessage.receive_message_from_process()
    testMessage.send_message_to_process()
