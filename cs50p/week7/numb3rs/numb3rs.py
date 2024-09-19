import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        if (
            0 <= int(matches.group(1)) <= 255
            and 0 <= int(matches.group(2)) <= 255
            and 0 <= int(matches.group(3)) <= 255
            and 0 <= int(matches.group(4)) <= 255
        ):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()


# if re.search(r"^(([1][0-9][0-9])|([2][0-5][0-5])|[1-9]?[0-9])\.(([1][0-9][0-9])|([2][0-5][0-5])|[1-9]?[0-9])\.(([1][0-9][0-9])|([2][0-5][0-5])|[1-9]?[0-9])\.(([1][0-9][0-9])|([2][0-5][0-5])|[1-9]?[0-9])$", ip):
