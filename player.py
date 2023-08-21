class player:


    def __init__(self) -> None:

        self.players = {}

    
    def valid_player(self, name):

        self.name = name

        if name != '' and len(name) >= 3 and isinstance(name, str):
            return True

        return False
    
    
    def def_player(self, char, name):
        
        if self.valid_player(name):
            self.players.update({
                char : name
            })
            return True
        
        return False