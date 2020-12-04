# Bulk passport validator

from dataclasses import dataclass


@dataclass
class Passport:
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: str = 0


def entry_to_passport(entry):
    entry = entry.replace(" ", "\n")
    field_list = entry.split("\n")
    init_dict = dict()
    for field in field_list:
        key, value = field.split(":")
        init_dict[key] = value
    p = Passport(**init_dict)
    return p


def input_to_dict(txt):
    with open(txt) as f:
        txt = f.read()
    entries = [i for i in txt.split("\n\n")]
    return entries


if __name__ == "__main__":
    entries = input_to_dict("input.txt")
    valid = 0
    for entry in entries:
        try:
            entry_to_passport(entry)
            valid += 1
        except TypeError:
            pass
    print(valid)