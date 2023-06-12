# test that init method sets blank list
# test that the gratitude is appending to blank list
# test that the formatted var is returned after multiple adds with correct string and syntax

from lib.gratitudes import *

def test_gratitudes_init_empty_list() :
    gratitudes = Gratitudes()
    result = gratitudes.gratitudes
    assert result == []

def test_gratitudes_add_appending() :
    gratitudes = Gratitudes()
    gratitudes.add('giving thanks!')
    result = gratitudes.gratitudes
    assert result == ['giving thanks!']

def test_gratitudes_formatted_var() :
    gratitudes = Gratitudes()
    gratitudes.add('This')
    gratitudes.add('Is')
    gratitudes.add('Adding')
    result = gratitudes.format()
    assert result == "Be grateful for: This, Is, Adding"