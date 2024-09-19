from numb3rs import validate

def main():
    test_validate()

def test_validate():
    assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('cat') == False
    assert validate('pre.season') == False
    assert validate('2001:0db8:85a3:0000:0000:8a2e:0370:7334') == False
    assert validate("1.2.3.1000") == False
    assert validate("1.2.1000.4") == False
    assert validate("1.1000.3.4") == False
    assert validate("1000.2.3.4") == False
    assert validate("1.") == False
    assert validate("256.0.0.0") == False  # Out of range octet
    assert validate("192.168.0.256") == False  # Out of range octet
    assert validate("192.168..1") == False  # Missing octet
    assert validate("192.168.0.1.2") == False  # Extra octet
    assert validate("10.10.10.10.10") == False  # Five octets
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False  # An IPv6 address


if __name__ == "__main__":
    main()