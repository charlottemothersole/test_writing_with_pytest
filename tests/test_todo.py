from lib.todo import *
import pytest 

# When we are given a Todo 
# and we add a task
# we can see the task in task_list

def test_todo_add():
    todo = ToDo()
    todo.add('cleaning!')
    assert todo.task_list == ['cleaning!']

# When we are given a Todo 
# and we add a task as an empty string
# we can see the task in task_list

def test_todo_empty_string():
    todo = ToDo()
    with pytest.raises(Exception) as e:
        todo.add('')
    str(e.value) == 'No task given!'