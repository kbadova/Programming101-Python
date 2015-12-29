import time


def input_command():
    print("Enter a command>")
    command = input()
    list_of_inputs = command.split(" ")
    return list_of_inputs


def main():
    print("Hello and Welcome! \n\
Choose an option.")
    print("1. meal - to write what are you eating now. \n\
2. list <dd.mm.yyyy> - lists all the meals that you ate that day,")
    map_of_foods = {}
    list_of_foods = []
    current_time = time.strftime("%d.%m.%Y")
    list_of_inputs = input_command()
    while list_of_inputs[0] != "list":
        if list_of_inputs[0] == "meal":
            list_of_foods.append(list_of_inputs[1])
            print("Ok.It is saved.")
            map_of_foods = {current_time: list_of_foods}
            list_of_inputs = input_command()
    if list_of_inputs[0] == "list":
        print(map_of_foods[current_time])


if __name__ == '__main__':
    main()
