import pytest
from lib.password_checker import *

# test to check if statement correctly calculates 
# length of password if length = 9
# test to check if statement as above if length = 20
# test to check else statement raises exception if len of password < 8

def test_if_len_is_9() :
    checker = PasswordChecker()
    result = checker.check('Password1')
    assert result == True


def test_if_len_is_20() :
    checker = PasswordChecker()
    result = checker.check('Passwordpassword1111')
    assert result == True

def test_else_raises_exception() :
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check('short')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
