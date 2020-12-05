# What is the highest ID on a boarding pass


def txt_to_list(txt):
    with open(txt) as f:
        lines = f.read().splitlines()
    return lines


def get_seat(seat_string, plane_dim):
    seats = [i for i in range(plane_dim)]
    for letter in seat_string:
        divider = len(seats) // 2
        if letter in ["F", "L"]:
            seats = seats[:divider]
        else:
            seats = seats[divider:]
    return seats[0]


def get_seat_id(seat_string):
    return get_seat(seat_string[:7], 128) * 8 + get_seat(seat_string[7:], 8)


if __name__ == "__main__":
    seats = txt_to_list("input.txt")
    print(max([get_seat_id(seat) for seat in seats]))
