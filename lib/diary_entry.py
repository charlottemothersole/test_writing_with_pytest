from math import ceil

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self.stop_point = 0

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        readable_chunk_length = wpm * minutes
        words = self.contents.split()
        if self.stop_point >= len(words):
            self.stop_point = 0

        start_point = self.stop_point
        end_point = self.stop_point + readable_chunk_length
        readable_chunk = " ".join(words[start_point:end_point])
        self.stop_point += readable_chunk_length
        return readable_chunk