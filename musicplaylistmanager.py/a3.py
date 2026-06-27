class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, my name is", self.name)

# Create objects
tom = Robot("Tom")
jerry = Robot("Jerry")

# Introduce themselves
tom.introduce()
jerry.introduce()