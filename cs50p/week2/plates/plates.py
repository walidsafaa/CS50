def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    digits = 0
    letters = 0
    if 2 <= len(s) <= 6:
        # Check all letters are non-special characters
        for c in s:
            if c.isdigit():
                digits += 1
            if c.isalpha():
                letters += 1

        if letters + digits == len(s) and letters >= 2:
            if digits >= 1:
                # Check the last character is a number
                if s[len(s) - 1].isdigit():
                    for i in range(len(s)):
                        # Check the first digit is not 0
                        if s[i].isdigit():
                            if s[i] != "0":
                                if s[i:].isdigit():
                                    return True
                                else:
                                    False
                            else:
                                return False
                else:
                    return False
            else:
                return True
        else:
            return False

    else:
        False


main()
