class city: #defining class
    def __init__(self,city,state):
        self.city = city
        self.state = state
    
    def greet(self): #defining method
        print(f'hi the capital of {self.state} is {self.city}')
    

citycapital = city("Bangalore","Karnataka") #calling class
citycapital.greet() #calling method
