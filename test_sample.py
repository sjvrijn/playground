def test_1():
    assert 1024 is (1023+1)
    
def test_2():
    assert 1+1 == 2

def test_3():
    assert (1 == 2) is False

def test_4():
    assert len([]) == 0

def test_5():
    assert False is False
