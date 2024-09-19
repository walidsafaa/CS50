from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten('word') == 'wrd'
    assert shorten('max') == 'mx'
    assert shorten('m1x') == 'm1x'
    assert shorten('m.x') == 'm.x'
    assert shorten('Omega') == 'mg'


if __name__ == "__main__":
    main()