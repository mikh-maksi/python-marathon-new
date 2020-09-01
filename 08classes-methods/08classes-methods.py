class ThreeAdder:
    name = "" #name = "Mikhail"
    age = 23
    rate = 1234
    def setRate (self,rate):
        self.rate = rate

a = ThreeAdder()
a.setRate(1000)
print(a.rate)