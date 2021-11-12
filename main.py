from datetime import datetime


def main():
    global inventory
    inventory = open('inventory.txt', 'r')  # This is to create the inventory file, only if it doesn't already exist
    global inventory_list
    inventory_list = []
    row = inventory.readlines()
    for line in row:
        inventory_list.append(line.split())
    # send_sorted("date")
    remove("Pear")
    #update_quantity("Xbox", 18)


def send_sorted(mode):
    if mode == 'name':
        sorted_inventory = sorted(inventory_list, key=lambda x: x[0])
    elif mode == 'quantity':
        sorted_inventory = sorted(inventory_list, key=lambda x: int(x[1]))
    elif mode == 'date':
        sorted_inventory = sorted(inventory_list, key=lambda x: datetime.strptime(x[2], '%m-%d-%Y'))
    else:
        print("Invalid mode specified for sort function")

    # print(sorted_inventory)


def remove(name):
    # print (inventory_list)
    # print('\n')
    inventory2 = open('inventory.txt', 'w')
    x = [x for x in inventory_list if name in x][0]
    inventory_list.pop(inventory_list.index(x))

    for element in inventory_list:
        inventory2.write(str(' '.join(str(v) for v in element)))
        inventory2.write("\n")
    inventory2.close()


def update_quantity(name, quantity):
    # print (inventory_list)
    # print('\n')
    inventory2 = open('inventory.txt', 'w')
    x = [x for x in inventory_list if name in x][0]
    inventory_list[inventory_list.index(x)][1] = quantity

    for element in inventory_list:
        inventory2.write(str(' '.join(str(v) for v in element)))
        inventory2.write("\n")
    inventory2.close()


main()
