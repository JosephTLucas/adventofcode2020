# Number of same anwers in group

from collections import Counter


def input_to_list(txt):
    with open(txt) as f:
        txt = f.read()
    entries = [i for i in txt.split("\n\n")]
    return entries


def agreed_letters_in_group(group):
    c = Counter(group)
    del c["\n"]
    return len([k for k in c if c[k] == len(group.split("\n"))])


if __name__ == "__main__":
    groups = input_to_list("input.txt")
    print(sum([agreed_letters_in_group(group) for group in groups]))
