class Record:
    phone = "+380631234567"
    skill = "Python"
    city = "Kyiv"
   
    def get_phone(self):
        return self.phone

    def get_skill(self):
        return self.skill

    def get_city(self):
        return self.city

b =Record()
print(b.get_city())
