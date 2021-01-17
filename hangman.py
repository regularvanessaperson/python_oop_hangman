class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.characters = list(chosen_word)
        self.spaces = len(self.characters)
        initalState = [False for i in range(self.spaces)]
        iterator = iter(self.characters)
        self.guess_dictionary = dict(zip(iterator, initalState))
    def guess_attempt (self, characters):
        if characters in self.guess_dictionary and self.guess_dictionary[characters]== False:
            self.guess_dictionary[characters] = True
            return True
        else:
            print("This letter is not in the word or you have already guessed it.")
            return False
    
    def print_word(self):
        for characters in self.chosen_word:
            if self.guess_dictionary[characters] == False:
                print("_", end = ' ')
            else: 
                print(characters, end = ' ')
        print('')


new_word = Word("TREE")

new_word.print_word()