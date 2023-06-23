import re
class DiaryTaskManager():
    def __init__(self):
        self.list = []
    
    def add(self, entry):
        self.list.append(entry)

    def read_all(self):
        all_entries_formatted = []
        for entry in self.list:
            all_entries_formatted.append(f'{entry.title}: {entry.content}')

        return all_entries_formatted
    
    def read_by_time_available(self, wpm, minutes):
        words_can_read = wpm * minutes
        possible_entries = {}
        for entry in self.list:
            if(words_can_read == entry.word_count):
                return entry
            elif(words_can_read >= entry.word_count):
                possible_entries[entry] = entry.word_count
        if(possible_entries == {}):
            return None
        else:
            list_of_possible_entries = list(possible_entries.items())
            sorted_list = sorted(list_of_possible_entries, key= lambda entry: entry[1])
            return sorted_list[-1][0]
        
    def read_todo(self, todo_list_name):
        return todo_list_name.task_list
    
    def view_mobile_numbers(self):
        phone_numbers = []
        for entry in self.list:
            matches = (re.findall(r"\d{5}\s\d{6}|\d{11}", entry.content))
            for item in matches:
                phone_numbers.append(item)
        return phone_numbers