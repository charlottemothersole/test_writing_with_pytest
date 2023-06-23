from lib.diary_entry import *

class Diary:
    def __init__(self):
        self.entries_list = []

    def add(self, entry):
        self.entries_list.append(entry)

    def all(self):
        return self.entries_list

    def count_words(self):
        word_count = 0
        for entry in self.entries_list:
            word_count += entry.count_words()
        return word_count

    def reading_time(self, wpm):
        reading_time = 0

        if self.entries_list == []:
            raise Exception("No entries added!")
        for entry in self.entries_list:
            reading_time += entry.reading_time(wpm)
        return reading_time

    def find_best_entry_for_reading_time(self, wpm, minutes):

#         var = we need to calculate how many words we can read
# for loop - look at stored entries list and run count_words
#     if entry word count == var return entry
#     elif entry word count < var
#     store entry and word count in dict
# if dict == {} return None 
# else sort dict
# return highest
        words_can_read = wpm * minutes
        possible_entries = {}
        for entry in self.entries_list:
            words_in_entry = entry.count_words()
            if words_in_entry == words_can_read:
                return entry
            elif words_in_entry < words_can_read:
                possible_entries[entry] = words_in_entry
        if possible_entries == {}:
            return None
        else:
            list_of_possible_entries = list(possible_entries.items())
            sorted_list = sorted(list_of_possible_entries,key = lambda item: item[-1] )
            print(sorted_list[-1][0].title)
            return sorted_list[-1][0]


        # best_entry = None
        # min_reading_time = 9999999
        # for entry in self.entries_list :
        #     entry_word_count = entry.count_words()
        #     entry_reading_time = entry_word_count / wpm
            

        #     if entry_reading_time <= minutes and minutes - entry_reading_time < min_reading_time :
        #         best_entry = entry
        #         min_reading_time = minutes - entry_reading_time
        # return best_entry

a = Diary()
entry_1 = DiaryEntry("Title 1", "Contents one")
entry_2 = DiaryEntry("Title 2", "This is contents two")
entry_3 = DiaryEntry("Title 3", "three")
entry_4 = DiaryEntry("Title 4", "two words")
a.add(entry_1)
a.add(entry_2)
a.add(entry_3)
a.add(entry_4)
print(a.find_best_entry_for_reading_time(1, 3))