import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Do you mean %s instead? If yes type Y , or else N for no : " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            user_ip = input("The word does not exist, please type again: ")
            w1 = user_ip.lower()
            if w1 in data:
                return data[w1]
            elif w1.title() in data:
                return data[w1.title()]
            elif w1.upper() in data:
                return data[w1.upper()]


word = input("Enter a word of your choice: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print("We dnt understand your entry :(")
    word = input("Type again: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)

