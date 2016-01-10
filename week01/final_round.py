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

# print(count_words(["apple", "banana", "apple", "pie"]))


def nan_expand(times):
    list_of_a = []
    for i in range(0, times):
        list_of_a.append("Not a")
    list_of_a.append("NaN")
    return " ".join(str(x) for x in list_of_a)
# print(nan_expand(3))


def iterations_of_nan_expand(expanded):
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

#print(group([1, 2, 1, 2, 3, 3]))


def max_consecutive(items):
    list1_of_len = []
    for i in group(items):
            list1_of_len.append(len(i))
    return max(list1_of_len)

# print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))


def sum_of_numbers(str):
    suma = 0
    for i in re.findall('\d+', str):
        suma += int(i)
    return suma

# print(sum_of_numbers("ab"))


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

# print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))

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

# print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))
