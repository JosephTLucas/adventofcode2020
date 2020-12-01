# Find two numbers that sum to 2020, return their product


def txt_to_list(txt):
    with open(txt) as f:
        lines = f.read().splitlines()
    return lines


def find_sum(input_list, target):
    input_list = list(map(int, input_list))
    for item in input_list:
        if target - item in input_list:
            return item, target - item
    return None, None


if __name__ == "__main__":
    input_list = txt_to_list("input.txt")
    first, second = find_sum(input_list, 2020)
    try:
        print(first, second, first * second)
    except TypeError:
        print("No pairs sum to target")
