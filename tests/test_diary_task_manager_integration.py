from lib.diary_task_manager import *
from lib.diary_entry_for_manager import *
from lib.todo import *

def test_read_all():
    diary = DiaryTaskManager()
    entry_1 = DiaryEntry('A title', 'Some content here!')
    entry_2 = DiaryEntry('A second title', 'Some more content here with more words!')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.read_all() == ['A title: Some content here!','A second title: Some more content here with more words!']

# Given a diary
# When we add two entries and call read_by_time_available(2, 2)
# we are given the closest matching entry in time to read

def test_read_by_time_available():
    diary = DiaryTaskManager()
    entry_1 = DiaryEntry('A title', 'Some content here!')
    entry_2 = DiaryEntry('A second title', 'Some more content here with more words!')
    entry_3 = DiaryEntry('A third title', 'Three!')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.read_by_time_available(2, 2) == entry_1

# Given a diary 
# When we add a task to ToDo and call read_todo
# We are given the list of tasks

# diary = DiaryTaskManager()
# todo = ToDo()
# todo.add('cleaning!')
# diary.read_todo()

def test_read_todo():
    diary = DiaryTaskManager()
    todo = ToDo()
    todo.add('cleaning')
    assert diary.read_todo(todo) == ['cleaning']

# Given a diary
# When we add multiple entries to Diary and call view_mobile_numbers()
# we are given a list of all mobile numbers in the entries

def test_view_mobile_numbers():
    diary = DiaryTaskManager()
    entry_1 = DiaryEntry('A title', 'A number 07123 456789!')
    entry_2 = DiaryEntry('A second title', 'Some more numbers here 07222 333444 with more words between 07333456789!')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.view_mobile_numbers() == ['07123 456789','07222 333444','07333456789']