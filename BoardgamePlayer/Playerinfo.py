class Player:
    player_name_list = ["Park", "Kim", "White", "Brown", "Green"]

    def __init__(self):
        self.author = "PSY"
        self.creation_date = "20211007"
        self.version = "1.0.0"

    def Playerselect(self):
        # 원래는 어떤 함수를 이용하여 랜덤한 이름을 불러오려고 했지만 일단 고정된 이름을 사용
        # 플레이어는 일단 1명만 제출
        N = 0
        self.Selected_player = self.player_name_list[N]
        return self.Selected_player

if __name__ == "__main__":
    printvalue = Player()
    print(printvalue.Playerselect())
