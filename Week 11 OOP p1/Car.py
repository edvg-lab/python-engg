class Car:
    classification = "vehicle"
    
    def print_classification(self):
        print(self.classification)
        
    def set_class(self, classification):
        Car.classification = classification
        
car1 = Car()
car2 = Car()

Car.classification = "lala"

car1.print_classification()
car2.print_classification()

car1.set_class("test")

car1.print_classification()
car2.print_classification()

