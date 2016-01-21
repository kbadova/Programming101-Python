import re


def to_character(string):
    list_of_digits = []
    for item in string:
        list_of_digits.append(item)
    return list_of_digits


def count_words(arr):
    dictionary = dict()
    for i in arr:
        dictionary[i] = arr.count(str(i))
    return dictionary


def nan_expand(times):
    list_of_a = []
    if times == 0:
        return ""
    for i in range(0, times):
        list_of_a.append("Not a")
    list_of_a.append("NaN")
    return " ".join(str(x) for x in list_of_a)
print(nan_expand(0))


def iterations_of_nan_expand(expanded):
    if "NaN" not in expanded:
        return False
    "".join(to_character(expanded))
    return expanded.replace(" ", "").count("Nota")
# print(iterations_of_nan_expand("Not a Not a NaN"))


def append_list(list_of_nums):
    index = 1
    firs_elem = list_of_nums[0]
    result = [firs_elem]
    while index < len(list_of_nums) and firs_elem == list_of_nums[index]:
        result.append(list_of_nums[index])
        index += 1
    return result


def group(list_of_group):
    result = []
    while len(list_of_group) != 0:
        current_group = append_list(list_of_group)
        result.append(current_group)
        list_of_group = list_of_group[len(current_group):]
    return result


def max_consecutive(items):
    list1_of_len = []
    for i in group(items):
            list1_of_len.append(len(i))
    return max(list1_of_len)


def sum_of_numbers(str):
    suma = 0
    for i in re.findall('\d+', str):
        suma += int(i)
    return suma


def check_first_station(stations, result, tank_size):
    for i in range(0, len(stations)):
        if stations[i] > tank_size:
            result.append(stations[i-1])
            break
    return result


def gas_stations(distance, tank_size, stations):
    stations.append(distance)
    result, list_of_max_distance = [], []
    check_first_station(stations, result, tank_size)

    for i in range(0, len(stations)):
        for j in range(1, len(stations) - 1):
            if stations[j] - stations[i] < tank_size:
                list_of_max_distance.append(stations[j])
            maxi = max(list_of_max_distance)
        if maxi not in result:
            result.append(maxi)
    return result


def dictionary(number, count):
    dictionary = {}
    dictionary[0] = [" "]
    dictionary[2] = ["a", "b", "c"]
    dictionary[3] = ["d", "e", "f"]
    dictionary[4] = ["g", "h", "i"]
    dictionary[5] = ["j", "k", "l"]
    dictionary[6] = ["m", "n", "o"]
    dictionary[7] = ["p", "q", "r", "s"]
    dictionary[8] = ["t", "u", "v"]
    dictionary[9] = ["w", "x", "y", "z"]
    if count >= len(dictionary[number]):
        return dictionary[number][count - number - 1]
    return dictionary[number][count]


def numbers_to_message(sequence):
    string = ""
    index = 0
    for i in range(0, len(sequence)):
        if index+1 < len(sequence) and i < index:
            i = index + 1
        if sequence[i] == -1:
            i += 1
        if sequence[i] == 1:
            count = 0
            while i+1 < len(sequence) and sequence[i+1] == sequence[i+2]:
                count += 1
                i += 1
            string += (dictionary(sequence[i], count)).upper()
            i += 2
        count = 0
        while i+1 < len(sequence) and sequence[i] == sequence[i+1]:
            count += 1
            i += 1
        string += dictionary(sequence[i], count)
        index = i
        if index == len(sequence)-1:
            break
    return string


def diction(el):
    dictionary = {}
    dictionary[" "] = [0]
    dictionary["a"] = [2]
    dictionary["b"] = [2, 2]
    dictionary["c"] = [2, 2, 2]
    dictionary["d"] = [3]
    dictionary["e"] = [3, 3]
    dictionary["f"] = [3, 3, 3]
    dictionary["g"] = [4]
    dictionary["h"] = [4, 4]
    dictionary["i"] = [4, 4, 4]
    dictionary["j"] = [5]
    dictionary["k"] = [5, 5]
    dictionary["l"] = [5, 5, 5]
    dictionary["m"] = [6]
    dictionary["n"] = [6, 6]
    dictionary["o"] = [6, 6, 6]
    dictionary["p"] = [7]
    dictionary["q"] = [7, 7]
    dictionary["r"] = [7, 7, 7]
    dictionary["s"] = [7, 7, 7, 7]
    dictionary["t"] = [8]
    dictionary["u"] = [8, 8]
    dictionary["v"] = [8, 8, 8]
    dictionary["w"] = [9]
    dictionary["x"] = [9, 9]
    dictionary["y"] = [9, 9, 9]
    dictionary["z"] = [9, 9, 9, 9]
    return dictionary[el]


def message_to_numbers(message):
    message += " "
    list_message = []
    for el in range(0, len(message)-1):
        current = message[el]
        next_el = message[el + 1]
        if current != next_el:
            if current.isupper():
                list_message.append(1)
                current = current.lower()
        for number in diction(current):
            list_message.append(number)
        if el != len(message) - 2:
            if diction(current)[0] == diction(next_el.lower())[0]:
                list_message.append(-1)
    return list_message

# print(message_to_numbers("Ivo e Panda"))
