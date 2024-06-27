class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * capacity

    def park_vehicle(self, vehicle_number, slot_number):
        if slot_number < 1 or slot_number > self.capacity:
            print(f"Invalid slot number. Please choose a slot between 1 and {self.capacity}.")
            return False
        if self.slots[slot_number - 1] is None:
            self.slots[slot_number - 1] = vehicle_number
            print(f"Vehicle {vehicle_number} parked in slot {slot_number}.")
            return True
        else:
            print(f"Slot {slot_number} is already occupied. Please choose a different slot.")
            return False

    def exit_vehicle(self, vehicle_number):
        for i in range(self.capacity):
            if self.slots[i] == vehicle_number:
                self.slots[i] = None
                print(f"Vehicle {vehicle_number} has exited from slot {i + 1}.")
                return True
        print(f"Vehicle {vehicle_number} not found in the parking lot.")
        return False

    def display_slots(self):
        print("Parking Slots Status:")
        for i, slot in enumerate(self.slots):
            status = slot if slot is not None else "Empty"
            print(f"Slot {i + 1}: {status}")

def main():
    parking_lot = ParkingLot(20)
    while True:
        print("\nWelcome to the Parking Lot Management System")
        print("1. Park Vehicle")
        print("2. Exit Vehicle")
        print("3. Display Parking Slots")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            vehicle_number = input("Enter vehicle number: ")
            slot_number = int(input("Enter parking slot number (1-20): "))
            parking_lot.park_vehicle(vehicle_number, slot_number)
        elif choice == '2':
            vehicle_number = input("Enter vehicle number to exit: ")
            parking_lot.exit_vehicle(vehicle_number)
        elif choice == '3':
            parking_lot.display_slots()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
