class Record:
    def __init__(self):
        self.fields = []

    def get_rate(self):
        for field in self.fields:
            # PUT YOUR CODE HERE
            if field.field_description == "Rate":
                return field.value