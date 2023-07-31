# _name -> use for convention (Private)
# __name
# __name__

class User:
    def __init__(self,username: str) -> None:
        self.userName = username
        self._email = "mr.masoud_mapar@outlook.com"


me = User('masoud')

print(me.userName)
print(me._email)
