# _name -> use for convention (Private)
# __name
# __name__

class User:
    def __init__(self,username: str) -> None:
        self.userName = username
        self._email = "mr.masoud_mapar@outlook.com"
    
    def login(self, gotPassword):
        if self._password == gotPassword:
            print("logon user")
        else:
            print("you are not logged in")


me = User('masoud')

print(me.userName)
print(me._email)
