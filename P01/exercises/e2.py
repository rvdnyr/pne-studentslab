# EXERCISE 2
# Write a Python program that first creates a null sequence and then a valid sequence. It should print the two objects.

class Seq():
    def __init__(self, strbases=None):
        self.strbases = strbases
        if strbases == None:
            print("NULL sequence created")
        else:
            print("New sequence created!")

    def __str__(self):
        if self.strbases == None:
            return "NULL"
        else:
            return self.strbases

    def __len__(self):
        return len(self.strbases)



print("-----| Practice 1, Exercise 2 |------")

# -- Creating a Null sequence
s1 = Seq()
# -- Creating a valid sequence
s2 = Seq("TATAC")

print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
