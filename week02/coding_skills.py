import json
import sys


def main():
    with open(sys.argv[1], 'r') as json_file:
        data = json.load(json_file)
    i = 0
    state_level = 0
    dictionary = {'C++': '', 'PHP': '', 'Python': '', 'C#': '', 'Haskell': '','Java': '', 'JavaScript': '', 'Ruby': '', 'CSS': '', 'C': ''}

    for i in range(0, len(data['people'])):
        for j in range(0, len(data['people'][i]['skills'])):
            language = data['people'][i]['skills'][j]['name']
            level = data['people'][i]['skills'][j]['level']
            if dictionary[language] != '':
                state_level = level
                if dictionary[language] < state_level:
                    dictionary[language] = level
            else:
                dictionary[language] = level

    for i in range(0, len(data['people'])):
        for j in range(0, len(data['people'][i]['skills'])):
            language_name = data['people'][i]['skills'][j]['name']
            person = data['people'][i]['first_name'] + ' '\
                + data['people'][i]['last_name']
            if language_name in dictionary:
                if data['people'][i]['skills'][j]['level'] \
                        in dictionary.values():
                    dictionary[language_name] = person

    return dictionary

if __name__ == '__main__':
    main()
