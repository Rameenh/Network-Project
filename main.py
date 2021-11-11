from datetime import datetime


def main():
    global inventory
    inventory = open('inventory.txt', 'r')  # This is to create the inventory file, only if it doesn't already exist
    global inventory_list
    inventory_list = []
    row = inventory.readlines()
    for line in row:
        inventory_list.append(line.split())
    #send_sorted("date")
    #remove("Pear")


def send_sorted(mode):
    if mode == 'name':
        sorted_inventory = sorted(inventory_list, key=lambda x: x[0])
    elif mode == 'quantity':
        sorted_inventory = sorted(inventory_list, key=lambda x: int(x[1]))
    elif mode == 'date':
        sorted_inventory = sorted(inventory_list, key=lambda x: datetime.strptime(x[2], '%m-%d-%Y'))
    else:
        print("Invalid mode specified for sort function")

    #print(sorted_inventory)


def remove(name):
    #print (inventory_list)
    print('\n')
    x = [x for x in inventory_list if name in x][0]
    inventory_list.pop(inventory_list.index(x))
    #print(inventory_list)


main()
