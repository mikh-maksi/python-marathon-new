import re
class DataField:
    field_description = "General data"

    def __init__(self, value):
        self.value = None
        self.validate(value)

    def validate(self, value):
        self.value = value

    def __contains__(self, item):
        return item in self.value

    def __str__(self):
        return f"{self.field_description}: {self.value}"


class EmailField(DataField):
    field_description = "Email"
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def validate(self, value):
        if self.EMAIL_REGEX.match(value):
            self.value = value
            print (f"email changed to {value}.")
        else: 
            print (f"{value} is not an email.")


a = EmailField("")
a.validate("mikhail_maksimov@goit.ua")

print("ok")
