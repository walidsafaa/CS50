while True:
    try:
        fraction = input("Fraction: ").strip().split("/")
        x = int(fraction[0])
        y = int(fraction[1])
        if x <= y:
            percentage = round(x / y * 100)
            if 1 < percentage < 99:
                print(f"{percentage}%")
                break
            elif percentage <= 1:
                print("E")
                break
            elif percentage >= 99:
                print("F")
                break
    except (ValueError, ZeroDivisionError):
        pass