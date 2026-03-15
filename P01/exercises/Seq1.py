# Seq class module

class Seq():
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def __len__(self):
        return len(self.strbases)
