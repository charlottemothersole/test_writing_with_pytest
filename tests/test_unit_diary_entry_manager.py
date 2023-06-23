from lib.diary_entry_for_manager import *
import pytest

# When we are given a diary entry with correct title and content and instantiate DiaryEntry 
# we see the word count in self.word_count

# entry_1 = DiaryEntry('A title', 'Some content here!')
# entry_1.word_count => 3'
def test_word_count():
    entry_1 = DiaryEntry('A title', 'Some content here!')
    assert entry_1.word_count == 3

# When we are given a diary entry with a title and content == '' and instantiate DiaryEntry 

def test_no_content():
    with pytest.raises(Exception) as e:
        entry_1 = DiaryEntry('A title', '')
    assert str(e.value) == 'Empty field!' 

