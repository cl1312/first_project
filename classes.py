
class flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

indigo = flight(3)

people = ["sachin","kohli","dravid","starc","smith"]

for passenger in people:
    success = indigo.add_passenger(passenger)
    if success:
        print (f"We added {passenger} to flight")
    else:
        print(f"No available seats for {passenger}")

