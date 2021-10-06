from _io import TextIOWrapper
import sys
from typing import Any


def send_message_to_process(obj: Any, delim: str = ';', std_out: [sys.stdout, TextIOWrapper] = sys.stdout):
    """
    Send message to process based on current message data.
    :param obj: data to send
    :param delim: delimiter to append at end
    :param std_out: alternative standard output for redirection
    """
    if not isinstance(delim, str):
        pass
    if len(delim) != 1:
        pass

    std_out.write(str(obj))
    std_out.write(delim)
