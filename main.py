from pathlib import Path


def main():
    global inventory
    inventory = open('inventory.txt', 'r')  # This is to create the inventory file, only if it doesn't already exist
    send_sorted()


def send_sorted():
    inventory_list = []
    row = inventory.readlines()
    for line in row:
        inventory_list.append(line.split())

    for x in range(len(inventory_list)):
        print(inventory_list[x])

main()