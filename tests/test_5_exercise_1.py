# # When an order is created with an address
# # The address is reflected in the address attribute
# order = Order("123 Fake Street")
# assert order.address == "123 Fake Street"

# # When we add two valid items to the order
# # And we format the order note
# # It returns a string with the address and the items
# order = Order("123 Fake Street")
# order.add_item("Chair")
# order.add_item("Moisturiser")
# assert order.format_note() == "Order for 123 Fake Street: Chair, Moisturiser"

from lib.chapter_5_exercise_1 import *
import pytest

# test format
def test_format_with_title_contents() :
    new_entry = DiaryEntry('The title', 'this is the diary entry')
    result = new_entry.format()
    assert result == 'The title: this is the diary entry'

# test count_words returns num of words

def test_count_words() :
    new_entry = DiaryEntry('The title', 'this is the diary entry')
    result = new_entry.count_words()
    assert result == 5

# test reading time returns int of estimated reading time based on wpm given

def test_reading_time() :
    new_entry = DiaryEntry('The title', 'this is the diary entry')
    result = new_entry.reading_time(5)
    assert result == 1

# test reading chunk returns string that user could read in num of minutes. 
# start at beginning and if called again return subsequent chunk.
def test_reading_chunk() :
    new_entry = DiaryEntry('The title', 'this is the diary entry that is over 5 words and should be split into multiple chunks')
    result = new_entry.reading_chunk(5, 1)
    assert result == 'this is the diary entry'

def test_reading_chunk_again() :
    new_entry = DiaryEntry('The title', 'this is the diary entry that is over 5 words and should be split into multiple chunks')
    new_entry.reading_chunk(5, 2)
    result = new_entry.reading_chunk(5, 1)
    assert result == 'and should be split into'

def test_reading_chunk_third() :
    new_entry = DiaryEntry('The title', 'this is the diary entry that is over 5 words and should be split into multiple chunks')
    new_entry.reading_chunk(5, 2)
    new_entry.reading_chunk(5, 1)
    result = new_entry.reading_chunk(5,1)
    assert result == 'multiple chunks'


