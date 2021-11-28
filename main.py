from datetime import datetime
from socket import *


def main():
    global inventory
    inventory = open('inventory.txt', 'r')  # This is to create the inventory file, only if it doesn't already exist
    global inventory_list
    inventory_list = []
    row = inventory.readlines()
    for line in row:
        inventory_list.append(line.split())
    # send_sorted("date")
    # remove("Pear")
    # update_quantity("Xbox", 18)

    serverSocket = socket(AF_INET, SOCK_STREAM)
    webPort = 65432
    serverSocket.bind(('127.0.0.1', webPort))

    serverSocket.listen(1)

    connectionSocket, addr = serverSocket.accept()

    while True:
        print("connected")

        try:
            message = connectionSocket.recv(1024).decode()
            remote_input = message.split()
            print(remote_input)
            if (remote_input[0] == '1'):
                mode = remote_input[1]
                tmp = send_sorted(mode)

                tmp = str(tmp)

                connectionSocket.sendall(tmp.encode())

            elif (remote_input[0] == '2'):
                item_to_rem = remote_input[1]
                remove(item_to_rem)
            elif (remote_input[0] == '3'):
                item_to_upd = remote_input[1]
                new_num = remote_input[2]
                update_quantity(item_to_upd, new_num)
            else:
                print('invalid remote input')

        except IOError:
            print("IOError")
            connectionSocket.close()
            serverSocket.close()


def send_sorted(mode):
    if mode == 'name':
        return sorted(inventory_list, key=lambda x: x[0])
    elif mode == 'quantity':
        return sorted(inventory_list, key=lambda x: int(x[1]))
    elif mode == 'date':
        return sorted(inventory_list, key=lambda x: datetime.strptime(x[2], '%m-%d-%Y'))
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
