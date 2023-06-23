class DiaryEntry():
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.word_count = len(content.split())
        if(title == '' or content == ''):
            raise Exception('Empty field!')