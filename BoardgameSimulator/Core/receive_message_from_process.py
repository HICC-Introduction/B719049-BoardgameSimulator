from _io import TextIOWrapper
import sys


def receive_message_from_process(delim: str = ";", std_in: [TextIOWrapper, sys.stdin] = sys.stdin) -> str:
    """
    Read message from process and parse into message itself.
    :param delim: delimiter character
    :param std_in: alternative standard input for redirection
    :return: message, read until delim
    """
    sys.stdin = std_in
    if len(delim) >= 1:
        delim = delim[0]
    if not isinstance(delim, str):
        return ""

    result: str = ""
    while True:
        read_char = std_in.read(1)
        if read_char == delim:
            break
        result += read_char

    return result

if __name__ == "__main__":
    test_result = receive_message_from_process(delim=';')
    print(test_result)
