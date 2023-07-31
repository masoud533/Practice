# _name -> use for convention (Private)
# __name
# __name__

class User:
    def __init__(self,username: str) -> None:
        self.userName = username
        self._email = "mr.masoud_mapar@outlook.com"
        self._password = "123"
        self.__message = "I love my Car"

    def __sayHello__(self):
        print(f"Hello {self.userName}")
    
    def login(self, gotPassword):
        if self._password == gotPassword:
            print("logon user")
        else:
            print("you are not logged in")


me = User('masoud')

print(me.userName)
me.__sayHello__()
print(me._email)
#print(me.__message) --> error return
