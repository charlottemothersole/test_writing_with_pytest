class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        # self.counter = 0
        self.num_of_words_already_read = 0

    def format(self):
        return f"{self.title}: {self.contents}" 

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        split_contents = self.contents.split()
        return len(split_contents)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        num_of_words = self.count_words()
        return num_of_words / wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        num_of_words = int(wpm * minutes)
        split_contents = self.contents.split()
        starting_point = self.num_of_words_already_read
        ending_point = num_of_words + starting_point
        chunk = split_contents[starting_point:ending_point]
        chunk_as_string = ' '.join(chunk)
        self.num_of_words_already_read += num_of_words
        return chunk_as_string
        
            