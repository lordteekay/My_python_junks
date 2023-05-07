import csv
class Item:
    payRate=0.8 #Discount of 20%
    all = []
    def __init__(self,name:str,price:float,quantity=0):
        #Run validation to the recieved arguments
        assert price>=0,f"price {price} is not greater than or equal to zero"
        assert quantity>=0,f"Quantity {quantity} is not greater than or equal to zero"
        #Assign to self Object
        self.name=name;
        self.price=price;
        self.quantity=quantity;

        #Action to execute
        Item.all.append(self);
    def calculateTotalPrice(self):
        return float(self.price*self.quantity);
    def discount(self):
        #Overiding the price attribute
        self.price=self.price*self.payRate;
    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv','r') as file:
            reader=csv.DictReader(file);
            itemList=list(reader);
            print(itemList);
            print('\n');
        for item in itemList:
            print(item);
    def __repr__(self):
        return f"item({self.name},'{self.price}',{self.quantity})"
Item.instantiate_from_csv();




















