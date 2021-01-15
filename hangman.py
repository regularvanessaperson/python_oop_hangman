class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.characters = list(chosen_word)
        self.spaces = len(self.characters)
        
    # def guess(self, characters):
    #     if characters in 
        


new_word = Word("CHILI")

print(new_word.characters)