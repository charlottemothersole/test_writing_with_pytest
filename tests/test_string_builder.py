from lib.string_builder import *

def test_string_builder_size_with_this() :
    new_class = StringBuilder()
    new_class.add('this')
    size_result = new_class.size()
    assert size_result == 4

def test_string_builder_output_with_this_thing() :
    new_class = StringBuilder()
    new_class.add('This')
    new_class.add(' thing')
    output_result = new_class.output()
    assert output_result == 'This thing'

# testing to check that init method sets an empty string
# test for add method in isolation

def test_string_builder_init_method_empty_string() : 
    new_class = StringBuilder()
    result = new_class.str
    assert result == ""

def test_string_builder_add_string() :
    new_class = StringBuilder()
    new_class.add('A string')
    result = new_class.str
    assert result == 'A string'