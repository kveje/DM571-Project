class User:
    def __init__(self, id, role, username, password):
        self.id = id
        self.role = role #TODO: Snak omkring roller
        self.username = username  #Maybe?
        self._password = password  #Maybe?
        
        def set_password(self, password):
            self._password = password