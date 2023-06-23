class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        # new_text = self.text
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                # print('self.text[i]',self.text[i])
                # 'ab'
                # 'aeiou'
                # self.text = self.text[:i] + self.text[i+1:]
                self.text.replace(self.text[i], '')
                print(self.text)
                # aeiou = 0:0 + 1:end = iou
                # 
                # print('i',i)
                # print('self.text[:i]', self.text[:i])
                # print('self.text[i:]', self.text[i+1:])
                # print('self.text[:i] + self.text[i:]', self.text[:i] + self.text[i+1:])
                # print('self.text',self.text)
                # b, a,
                # eiou, eou, eo
                if self.text[i].lower() not in self.vowels:
                    i += 1
        
        return self.text

new = VowelRemover('aeiou')
print(new.remove_vowels())
