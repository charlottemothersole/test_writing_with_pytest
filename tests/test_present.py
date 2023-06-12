# test init method returns None
# test wrap method adds contents
# test wrap raises exception when contents already full
# test unwrap method unwraps contents
# test unwrap method raises exception when nothing to unwrap
import pytest
from lib.present import *


def test_present_init_none() :
    present = Present()
    result = present.contents
    assert result == None


def test_present_wrap_adds() :
    present = Present()
    present.wrap(10)
    result = present.contents
    assert result == 10

def test_present_wrap_exception() :
    present = Present()
    present.wrap('Thing A')
    with pytest.raises(Exception) as e:
        present.wrap('Thing B')
    error_message = str(e.value)
    assert error_message == 'A contents has already been wrapped.'

def test_present_unwrap() :
    present = Present()
    present.wrap("Thing A")
    present.unwrap()
    result = present.contents
    assert result == "Thing A"

def test_present_unwrap_exception() :
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == 'No contents have been wrapped.'


