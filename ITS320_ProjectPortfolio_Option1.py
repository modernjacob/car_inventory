#ITS320_ProjectPortfolio_Option1
#Jacob Huckleberry
#6-12-2022


# Car Input Class
class Car_entry():

    def __init__(self):
        self.make = ''
        self.model = ''
        self.color = ''
        self.year = 0
        self.mileage = 0

    def attribute(self):
        try:
            self.make = str(input('Enter Make of Car: '))
            self.model = str(input('Enter Model of Car: '))
            self.color = str(input('Enter Color of Car: '))
            self.year = int(input('Enter Year of Car: '))
            self.mileage = int(input('Enter Mileage of Car: '))
            return True
        except ValueError:
            print('You made a mistake\n')
            return False

    def __str__(self):
        return '\t'.join(str(x) for x in ['', self.make, self.model, self.color, self.year, self.mileage])


# Inventory Class 
class Inventory:

    def __init__(self):
        self.list = []

    def add_inv(self):
        car = Car_entry()
        if car.attribute() == True:
            self.list.append(car)
            print('Car added to inventory.\n')

    def inv_display(self):
        print('\t'.join(['', 'Make', 'Model', 'Year', 'Color', 'Mileage']))
        for i, car in enumerate(self.list):
            print(i + 1, car)
        print()


car_inventory = Inventory()


# 3 - While & if-statement | Main-line Logic
while True:

    print('Enter 1 to view the current inventory')
    print('Enter 2 to add a car to the inventory')
    print('Enter 3 to delete a car from the inventory')
    print('Enter 4 to update a car in the inventory')
    print('Enter 5 to export the inventory to a text file')
    print('Enter 6 to exit the program\n')

    try:
        selection = int(input('Enter an command: '))
    except ValueError:
        print('Enter a number for a command')
        selection = 0


    if selection == 1:
        # INVENTORY DISPLAY  
        if len(car_inventory.list) < 1:
            print('No data in the car inventory \n')
        else:
            car_inventory.inv_display()
    elif selection == 2:
        # ADD CAR
        car_inventory.add_inv()
    elif selection == 3:
        # DELETE CAR
        delete_num = 0
        if len(car_inventory.list) < 1:
            print('No data in the car inventory to delete \n')
        else:
            car_inventory.inv_display()
            delete_num = int(input('Choose the number associated with the car to delete from inventory: '))
            if delete_num - 1 > len(car_inventory.list) or delete_num < 1:
                print('Invalid entry number\n')
            else:
                car_inventory.list.remove(car_inventory.list[delete_num - 1])
                print('Car entry deleted\n')
    elif selection == 4:
        # UPDATE CAR INFORMATION
        if len(car_inventory.list) < 1:
            print('No data in the car inventory to delete\n')
        else:
            car_inventory.inv_display()
            update_num = int(input('Choose the number associated with the car to update its information: '))
            if update_num - 1 > len(car_inventory.list) or update_num < 1:
                print('Invalid entry number\n')
            else:
                update_car = Car_entry()
                if update_car.attribute() == True:
                    car_inventory.list.remove(car_inventory.list[update_num - 1])
                    car_inventory.list.insert(update_num - 1, update_car)
                    print('The car information has been updated\n')
    elif selection == 5:
        # EXPORT INVENTORY TO FILE
        if len(car_inventory.list) < 1:
            print('No data in the car inventory to delete')
        else:
            inv_file = open('Car-Inventory', 'w')
            inv_file.write('\t'.join(['', 'Make', 'Model', 'Year', 'Color', 'Mileage']))
            inv_file.write('\n')
            for i, car in enumerate(car_inventory.list):
                inv_file.write(f'{i}{car}\n')
            inv_file.close()
            print('Car inventory Exported\n')
    elif selection == 6:
        # PROGRAM EXIT
        print('Program Exit')
        break
    else:
        print('Invalid Input\n')