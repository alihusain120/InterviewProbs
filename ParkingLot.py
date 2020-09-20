# Parking Lot program
#
#

class ParkingLot:
    def __init__(self, maxCapacity):
        self.maxCapacity = maxCapacity
        self.currentCapacity = 0
        self.spaces = [None] * maxCapacity
        

    def isFull(self):
        return self.maxCapacity == self.currentCapacity

    def park(self, Vehicle):
        
        if self.isFull():
            #no spots available
            print("The parking lot is full. Please try again later.")
            return

        else:
            #park the car
            
            i = 0
            while i < len(self.spaces):
                if self.spaces[i].isAvailable():
                    #found spot, park vehicle
                    if not self.spaces[i].size >= Vehicle.size:
                        i += 1
                        continue
                        
                    self.spaces[i].vehicleAtSpot = Vehicle
                    self.currentCapacity += 1
                    Vehicle.parkingSpot = i
                    print("Your car was successfully parked in spot " + str(i))
                    return

            print("There are no available parking spots. Please try again later.")
            return

    def remove(self, Vehicle):

        if Vehicle.parkingSpot >= 0 and Vehicle.parkingSpot < len(self.spaces):
            toReturnVehicle = self.spaces[parkingSpot]
            self.spaces[Vehicle.parkingSpot].vehicleAtSpot = None
            self.currentCapacity -= 1
            Vehicle.parkingSpot = -1
            return toReturnVehicle
            
        else:
            print("Your vehicle is not in the parking lot.")
            return


    def checkSpot(self, i):
        if self.spaces[i].isAvailable():
            print("This spot is free.")
        else:
            print("There is a car in this spot")
            
        return self.spaces[i]
    

class ParkingSpace:

    def __init__(self, size):
        self.size = size
        self.vehicleAtSpot = None

    def isAvailable(self):
        if self.vehicleAtSpot is None:
            return True
        else:
            return False


class Vehicle:

    def __init__(self, size, licensePlate):
        self.size = size
        self.licensePlate = licensePlate
        self.parkingSpot = -1

    def getPlate(self):
        return self.licensePlate

    def getParkingSpot(self):
        return self.parkingSpot

    
        


            
                    
                   
            
