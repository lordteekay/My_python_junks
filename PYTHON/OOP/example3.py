class Item:
    def __init__(self,name: str,price=0,quantity=0):
        print(f"An instances created:{name}") 
        #Run validations to the recieved arguments
        assert quantity>=0,f"{quantity} must be greater than or equal to zero";
        assert price>=0,f"{price} must be greater than or equal to zero";

        #Asssign to self object
        self.name=name;
        self.price=price;
        self.quantity=quantity;

    def calculateTotalPrice(self):
        return self.price*self.quantity;





item1=Item("phone",100,2)
print(item1.calculateTotalPrice());
item2=Item("laptop",200,3)
print(item2.calculateTotalPrice());
