class Car:
    def __init__(self,engine,gear,colour,model):
        self.engine=engine;
        self.gear=gear;
        self.colour=colour;
        self.model=model;
    def displayInformation(self):
        print("Model:"+str(self.model),"Engine:"+str(self.engine),"Gear:"+str(self.gear),"Colour:"+str(self.colour))

car1=Car("V6","5-Gear-box","Red","Toyota");
car2=Car("V4","4-Gear-box","Whine","Nissan");
car1.displayInformation();
car2.displayInformation();
