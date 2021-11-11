from pathlib import Path
from datetime import datetime


def main():
    global inventory
    inventory = open('inventory.txt', 'r')  # This is to create the inventory file, only if it doesn't already exist
    send_sorted("date")


def send_sorted(mode):
    inventory_list = []
    row = inventory.readlines()
    for line in row:
        inventory_list.append(line.split())

    if mode == 'name':
        sorted_inventory = sorted(inventory_list, key=lambda x: x[0])
    elif mode == 'quantity':
        sorted_inventory = sorted(inventory_list, key=lambda x: int(x[1]))
    elif mode == 'date':
        sorted_inventory = sorted(inventory_list, key=lambda x: datetime.strptime(x[2], '%m-%d-%Y'))
    else:
        print("Invalid mode specified for sort function")

    print(sorted_inventory)

main()