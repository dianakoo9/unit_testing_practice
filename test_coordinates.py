
def test_on_line():
    from coordinates import on_line

    result = on_line((0,0),(5,5),1)

    assert result == 1

def test_find_slope():
    from coordinates import find_slope

    result = find_slope((-1,0),(3,4))

    assert result == 1

def test_find_yintercept():
    from coordinates import find_yintercept

    result = find_yintercept((2,5),2)

    assert result == 1
