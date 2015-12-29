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

print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))
