import time
import sys
import json


def input_command():
    print("Enter a command>")
    command = input()
    list_of_inputs = command.split(" ")
    return list_of_inputs


def food_input(list_of_inputs):
    print("How much have you eaten?")
    eaten_food = input()
    if eaten_food[len(eaten_food) - 1] == 'g':
        if eaten_food[len(eaten_food) - 2:] == 'kg':
            list_of_inputs.append(int(eaten_food[0:(len(eaten_food)-2)])*1000)
            return list_of_inputs
        else:
            list_of_inputs.append(eaten_food[0:len(eaten_food)-1])
    return list_of_inputs


def open_json(name_json):
    with open(name_json, 'r') as json_file:
        data = json.load(json_file)
    return data


def write_unknown_food(food, calories):
    data = open_json(sys.argv[1])
    data.update({food: calories})
    with open(sys.argv[1], 'w') as new_json:
        json.dump(data, new_json)


def calc_calories(list_of_inputs):
    data = open_json(sys.argv[1])
    food = list_of_inputs[1]
    if food not in data:
        print("I don't have " + food + " in the calories database. \n\
            How much calories per 100g?")
        calories = input()
        write_unknown_food(food, int(calories))
        data = open_json(sys.argv[1])
    calories = data[food]
    total_calories = int(list_of_inputs[2]) * calories // 100
    return ('Ok, this is a total of ' + str(total_calories) + ' calories')


def write_in_list(key, value):
    data = open_json(sys.argv[2])
    if key in data:
        data[key].append(value)
    else:
        data[key] = value
    with open(sys.argv[2], 'w') as new_json:
        json.dump(data, new_json)


def main():
    print("Hello and Welcome! \n\
        Choose an option. \n\
        1. meal - to write what are you eating now. \n\
        2. list <dd.mm.yyyy> - lists all the meals that you ate that day,")
    current_time = time.strftime("%d.%m.%Y")
    list_of_inputs = input_command()
    meal = list_of_inputs[1]
    command = list_of_inputs[0]
    while command != "list":
        if command == "meal":
            food_input(list_of_inputs)
            print(calc_calories(list_of_inputs))
            write_in_list(current_time, meal)
            list_of_inputs = input_command()
    if command == "list":
        data = open_json(sys.argv[2])
        print(data[meal])


if __name__ == '__main__':
    main()
