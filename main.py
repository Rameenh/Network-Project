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

    sorted_name = sorted(inventory_list, key=lambda x: x[0])

    print(sorted_name)

main()