from newpackage import myModule

def test_fibonacci():
    """making sure the code works correctly"""
    
    assert fibonacci(1) == 1, "incorrect"
    assert fibonacci(2) == 1, "incorrect"
    assert fibonacci(3) == 2, "incorrect"
    