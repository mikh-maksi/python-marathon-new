class Record:
    def __init__(self):
        self.fields = []
        self.name = "Oleg"
        self.phone = "+380631234567"
        self.skill = "Python"
        self.city = "Kyiv"
        self.rate = 2000

    def __eq__(self, other):
        return self.rate == other.rate    
    def __gt__(self, other):
        return self.rate **>** other.rate
    def __lt__(self, other):
        return self.rate < other.rate

b = Record()
c = Record()
c.name = "Igor"
c.rate = 3000

if c>b:
    print (f"{c.name} зарабатывает больше чем {b.name}")

