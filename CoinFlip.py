from random import randrange
results = []

def flip_coin():
    if randrange(0, 2) < 0.55555:
        return "Heads"
    else:
        return "Tails"


def count_history(results):
    heads = results.count("Heads")
    tails = results.count("Tails")
    return "Heads: {0}\nTails: {1}".format(heads, tails)


state = True
start_phrase = "input 'f' to flip and q to exit:\n"

while state:
    n = input(start_phrase)
    if n == "f":
        result = flip_coin()
        results.append(result)
        print(result)
    elif n == "q":
        print(count_history(results))
        state = False
