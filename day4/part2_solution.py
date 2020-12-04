# Bulk passport validator w/ field validation

import attr


@attr.s
class Passport:
    byr = attr.ib()
    iyr = attr.ib()
    eyr = attr.ib()
    hgt = attr.ib()
    hcl = attr.ib()
    ecl = attr.ib()
    pid = attr.ib()
    cid = attr.ib(default=0)

    @byr.validator
    def valid_byr(self, attribute, value):
        if int(value) < 1920 or int(value) > 2002:
            raise ValueError("Birth Year must be between 1920 and 2002")

    @iyr.validator
    def valid_iyr(self, attribute, value):
        if int(value) < 2010 or int(value) > 2020:
            raise ValueError("Issue Year must be between 2010 and 2020")

    @eyr.validator
    def valid_eyr(self, attribute, value):
        if int(value) < 2020 or int(value) > 2030:
            raise ValueError("Expiration Year must be between 2020 and 2030")

    @hgt.validator
    def valid_hgt(self, attribute, value):
        number = value[:-2]
        unit = value[-2:]
        if unit not in ["cm", "in"]:
            raise ValueError("Height Unit must be cm or in")
        if unit == "cm":
            if int(number) < 150 or int(number) > 193:
                raise ValueError("CM height must be between 150 and 193")
        else:
            if int(number) < 59 or int(number) > 76:
                raise ValueError("IN height must be between 59 and 76")

    @hcl.validator
    def valid_hcl(self, attribute, value):
        if value[0] != "#":
            raise ValueError("Hair Color must start with #")
        if len(value[1:]) != 6:
            raise ValueError("Hair Color must have 6 chars after #")
        if value[1:].isalnum() is False:
            raise ValueError("Hair Color must have 6 alphanumeric chars after #")

    @ecl.validator
    def valid_ecl(self, attribute, value):
        if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            raise ValueError(
                "Eye  Color must be one of amb, blu, brn, gry, grn, hzl, oth"
            )

    @pid.validator
    def valid_pid(self, attribute, value):
        if len(value) != 9:
            raise ValueError("PID must be 9 digits")
        if value.isnumeric() is False:
            raise ValueError("PID must be all numeric")


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
        except (TypeError, ValueError):
            pass
    print(valid)