# 1. Describe the Problem
# Put or write the user story here. Add any clarifying notes you might have.

# As a user
# So that I can record my experiences
# I want to keep a regular diary

# As a user
# So that I can reflect on my experiences
# I want to read my past diary entries

# As a user
# So that I can reflect on my experiences in my busy day
# I want to select diary entries to read based on how much time I have and my reading speed

# As a user
# So that I can keep track of my tasks
# I want to keep a todo list along with my diary

# As a user
# So that I can keep track of my contacts
# I want to see a list of all of the mobile phone numbers in all my diary entries

# ---------------------------------------

# 2. Design the Class System
# Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com

# Class DiaryTaskManager
#     __init__(self)
        # list = [entries]
#     add(self, entry)    
#         entry = formatted string
#         adds entry to diary_entries list
#         return nothing
#     read_all(self)
#         return all entries in diary_entries list
#     read_by_time_available(self, wpm, minutes)
#         wpm = int
#         minutes = int
#         calculate time available to read
#         return first entry that matches/closest less than match to time available
#     read_todo(self)
#         return todo list from Class Todo
#     view_mobile_numbers(self)
#         return list of mobile numbers from diary_entries list


# Class Todo
#     __init__(self)
#         task_list = list
#     add(self, task)
#         task = string
#         add task to task_list

# Class DiaryEntry
#     __init__(self, title, content)
#      sets title, content and word count
#      returns concatenated string title + content

# ----------------------------------------

# 3. Create Examples as Integration Tests
# Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

# Given a diary
# When we add two entries and call read_all
# We see those entries in the diary_entries list

# diary = DiaryTaskManager()
# entry_1 = DiaryEntry('A title', 'Some content here!')
# entry_2 = DiaryEntry('A second title', 'Some more content here with more words!')
# diary.add(entry_1)
# diary.add(entry_2)
# diary.read_all() => [entry_1, entry_2] 

# Given a diary
# When we add two entries and call read_by_time_available(2, 2)
# we are given the closest matching entry in time to read

# diary = DiaryTaskManager()
# entry_1 = DiaryEntry('A title', 'Some content here!')
# entry_2 = DiaryEntry('A second title', 'Some more content here with more words!')
# diary.add(entry_1)
# diary.add(entry_1)
# diary.read_by_time_available(2, 2) => [entry_1] 

# Given a diary 
# When we add a task to ToDo and call read_todo
# We are given the list of tasks

# diary = DiaryTaskManager()
# todo = ToDo()
# todo.add('cleaning!')
# diary.read_todo()

# Given a diary
# When we add multiple entries to Diary and call view_mobile_numbers()
# we are given a list of all mobile numbers in the entries

# diary = DiaryTaskManager()
# entry_1 = DiaryEntry('A title', 'A number 07123 456789!')
# entry_2 = DiaryEntry('A second title', 'Some more numbers here 07222 333444 with more words between 07333456789!')
# diary.add(entry_1)
# diary.add(entry_1)
# diary.view_mobile_numbers() => ['07123 456789','07222 333444','07333456789']

# -----------------------------------------------

# 4. Create Examples as Unit Tests


# When we are given a diary entry with correct title and content and instantiate DiaryEntry 
# we see the word count in self.word_count

# entry_1 = DiaryEntry('A title', 'Some content here!')
# entry_1.word_count => 3'

# When we are given a diary entry with a title and content == '' and instantiate DiaryEntry 

# entry_1 = DiaryEntry('A title', '') => raise error 'Empty field!' 

# When we are given a Todo 
# and we add a task
# we can see the task in task_list

# todo = Todo()
# todo.add('cleaning!')
# todo.task_list => ['cleaning']

# When we are given a Todo 
# and we add a task as an empty string
# we can see the task in task_list

# todo = Todo()
# todo.add('') => raise error 'No task given!'

# ---------------------------------------

# 5. Implement the Behaviour
# After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.