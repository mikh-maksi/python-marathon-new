class DataField:
    def __init__(self, value):
        self.value = None
        self.validate(value)

    def validate(self, value):
        self.value = value

    def __contains__(self, item):
        return item in self.value