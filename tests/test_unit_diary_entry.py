from lib.diary_entry import *

# test instantiation
def test_diary_entry_instantiation():
    diary_entry = DiaryEntry("Title 1", "Contents one")
    assert diary_entry.title == "Title 1"
    assert diary_entry.contents == "Contents one"

def test_single_entry_count_words():
    diary_entry = DiaryEntry("Title 1", "Contents one")
    assert diary_entry.count_words() == 2

def test_reading_time_for_2wpm():
        diary_entry = DiaryEntry("Title 1", "Contents one")
        assert diary_entry.reading_time(2) == 1

def test_initialize_2_words_first_chunk():
    diary_entry = DiaryEntry("Title 1", "Contents one")
    assert diary_entry.reading_chunk(1,1) == "Contents"