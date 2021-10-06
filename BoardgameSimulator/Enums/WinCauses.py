from enum import Enum


class WinCauses(Enum):
    FinishingMove: int = 0
    OpponentIllegalMove: int = 1
    OpponentForfeit: int = 2
    OpponentTimeOut: int = 3
    GameEndConditionMet: int = 4