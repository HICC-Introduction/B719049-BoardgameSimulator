from enum import Enum


class BoardgameMessageTypes:
    Acknowledgement: str = "ACK"
    Enroll: str = "ENR"
    Prepare: str = "PRE"
    Start: str = "STT"
    Terminate: str = "EXT"
    NotifyOtherTurn: str = "TRN"
    End: str = "END"
    RequestTurn: str = "RQT"
    ResponseTurn: str = "RPT"
    RequestJudgement: str = "RQJ"
    ResponseJudgement: str = "RPJ"
