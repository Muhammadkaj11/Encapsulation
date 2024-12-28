class myclass:
    __privatevar=22
    def __privatemeth(self):
        print("my message")
    def hello(self):
        print("self.__privatevar")
ob=myclass()
ob.hello()
ob.__privatemeth()