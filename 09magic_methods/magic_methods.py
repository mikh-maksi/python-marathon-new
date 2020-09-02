
class Record:
    def __init__(self):
        self.fields = []
        self.phone = "+380631234567"
        self.skill = "Python"
        self.city = "Kyiv"
 
    def get_skill(self):
        return self.skill

    def get_phone(self):
        return self.phone

    def get_city(self):
        return self.city

b =Record()
print(b.get_city())
