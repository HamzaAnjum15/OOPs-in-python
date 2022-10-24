class train:
    def __init__(self,name,seatno,charges):
        self.name=name
        self.seatno=seatno
        self.charges=charges
    def info(self):
        print(f"the name of the train is {self.name}")
        print(f"the seatno of the train is {self.seatno}")
        print(f"the charges of the train is {self.charges}")
    def bookticket(self):
        if self.seatno>0:
            print(f"your seat number is {self.seatno}")
            self.seatno=self.seatno-1
        else:
            print("the seats are full")
passenger=train("hyderabad express",1,4000)
passenger.info()
passenger.bookticket()
passenger.bookticket()
        