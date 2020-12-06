# Sum unique question answers


def input_to_list(txt):
    with open(txt) as f:
        txt = f.read()
    entries = [i for i in txt.split("\n\n")]
    return entries


def unique_letters_in_group(group):
    total = set(list(group))
    total.discard("\n")
    return len(total)


if __name__ == "__main__":
    groups = input_to_list("input.txt")
    print(sum([unique_letters_in_group(group) for group in groups]))
