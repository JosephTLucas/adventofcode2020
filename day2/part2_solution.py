# Count passwords that match their given rule


def txt_to_list(txt):
    with open(txt) as f:
        lines = f.read().splitlines()
    return lines


def check(line):
    rule, password = line.split(": ")
    range, target_letter = rule.split(" ")
    low, high = range.split("-")
    if (password[int(low) - 1] == target_letter) ^ (
        password[int(high) - 1] == target_letter
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    input_list = txt_to_list("input.txt")
    print(sum([1 for password in input_list if check(password)]))