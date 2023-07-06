



class Player:
    def __init__(self, player_info):
        self.name = player_info ["name"]
        self.age = player_info ["age"]
        self.position = player_info ["position"]
        self.team = player_info ["team"]


    @classmethod
    def add_players(cls, player_info):
        player_new_list = []
        for dict in player_info:
            player_new_list.append(cls(dict))
            return player_new_list


kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}


player_kevin = Player(kevin)
print(player_kevin)

player_jason = Player(jason)
print(player_jason)

player_kyrie = Player(kyrie)
print(player_kyrie)






