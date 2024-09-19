# TODO


def main():
    number = get_pos()
    unmultiplied = number
    multiplied = number

    # Check Card Lengh
    ccNUM3 = number
    count = 0
    while ccNUM3 >= 1:
        ccNUM3 = ccNUM3 / 10
        count += 1

    # Luna's Algorithm
    # second digits
    second = multiplied / 10
    total_multi = 0
    first_sec = int(second % 10) * 2

    while second >= 1:
        second = second / 100
        multi = int(second % 10) * 2
        if multi > 9:
            multi_digit_a = int(multi % 10)
            multi_digit_b = int(multi / 10)
            total_multi = total_multi + multi_digit_a + multi_digit_b
        else:
            total_multi = total_multi + multi
    if first_sec > 9:
        first_digit_a = int(first_sec % 10)
        first_digit_b = int(first_sec / 10)
        total_multi2 = total_multi + first_digit_a + first_digit_b
    else:
        total_multi2 = first_sec + total_multi

    # first digits
    first_digit = int(unmultiplied % 10)
    total_sum = 0

    while unmultiplied >= 1:
        unmultiplied = unmultiplied / 100
        sum = int(unmultiplied % 10)
        total_sum = total_sum + sum
    total_sum = total_sum + first_digit

    all = total_multi2 + total_sum

    if all % 10 == 0:
        if (
            count == 13
            or count == 16
            and int(number / (10**12)) == 4
            or int(number / (10**15)) == 4
        ):
            print("VISA")
        elif (
            count == 16
            and int(number / (10**14)) == 51
            or int(number / (10**14)) == 52
            or int(number / (10**14)) == 53
            or int(number / (10**14)) == 54
            or int(number / (10**14)) == 55
        ):
            print("MASTERCARD")
        elif (
            count == 15
            and int(number / (10**13)) == 34
            or int(number / (10**13)) == 37
        ):
            print("AMEX")
        else:
            print("INVALID")
    else:
        print("INVALID")


def get_pos():
    while True:
        try:
            n = int(input("Number: "))
            if n > 0:
                return n
        except ValueError:
            print("Not an intger.")


main()
