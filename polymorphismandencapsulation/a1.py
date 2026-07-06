class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score =  score
    
    def info(self):
        print(f"Cricket - {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} hits a six!")

    def get_score (self):
        return self.__score
    
    def set_score(self, score):
        if score >- 0:
            self.__score = score


class Football:   
    def __init__(self, player, score):
        self.__player = player
        self.__score =  score
    
    def info(self):
        print(f"Football - {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} scores a goal!")

    def get_score (self):
        return self.__score
    
    def set_score(self, score):
        if score >- 0:
            self.__score = score



c = Cricket("Rohit", 85)
f = Football("Arjun", 2)

for game in (c, f):
    game.info()
    game.play()

c.__score = 999
print(c.get_score())




 