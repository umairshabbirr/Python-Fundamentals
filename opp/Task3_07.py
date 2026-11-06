class car:
    def __init__(self, Brand, model):
        self.Brand = Brand
        self.model = model

    def start(self):
        print(self.Brand,"is starting")
    def stop(self):
        print(self.Brand,"is stopping")


car1 = car("Toyota", "Corolla")
car1.start()
car1.stop()