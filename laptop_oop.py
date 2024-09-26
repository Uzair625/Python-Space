class Laptop:
    def __init__(self, name, processor, gen, window):
        self.name = name
        self.processor = processor
        self.gen = gen
        self.window = window
        self.laptop_start = False

    def On(self):
        if not self.laptop_start:
            print("Starting Laptop")
            self.laptop_start = True
        else:
            print("The Laptop is already on start")

    def shutdown(self):
        if self.laptop_start:
            print("Laptop is shutting down..")
            self.laptop_start = False
        else:
            print("Laptop is already off..!")

    def features(self):
        print("The Features of the Laptop..!")
        print(self.name)
        print(self.gen)
        print(self.window)


if __name__ == "__main__":
    pc = Laptop(name='Hp', processor='2.7ghz', gen='i5', window='Ms Windows 11')
    pc.On()
    pc.features()
    pc.shutdown()
