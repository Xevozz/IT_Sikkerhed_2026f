import pytest

# Test der er sande #

def test_pass():
    assert 1 + 1 == 2 # korrekt 1 + 1 = 2

def test_another_pass():
    assert "hello".upper() == "HELLO" # korrekt, skal være "HELLO"

def test_pass_with_calculation():
    result = sum([1, 2, 3, 4])
    assert result == 10 # korrekt, summen af angivet index-liste er 10



# Test der fejler #

def test_fail():
    assert 1 + 1 == 3 # forkert, skal være 2

def test_another_fail():
    assert "hello".lower() == "HELLO" # forkert, skal være "hello"

def test_fail_with_exception():
    raise ValueError("This is an intentional failure.") # forventet fejl



# Test som crasher #

def test_crash():
    raise Exception("This test crashes!") # En generel undtagelse

def test_another_crash():
    x = 1 / 0  # man kan ikke dividere med 0

def test_crash_with_index():
    lst = [1, 2, 3]
    _ = lst[5]  # 5 findes ikke i index-listen angivet.



# Test der skippes #
@pytest.mark.skip(reason="Skipping this test for demonstration purposes.")

def test_skip():
    assert 1 + 1 == 2 # testen bliver skippet

@pytest.mark.xfail(reason="This test is expected to fail.") # testen bliver skippet

def test_expected_fail():
    assert 1 + 1 == 3 # testen bliver skippet