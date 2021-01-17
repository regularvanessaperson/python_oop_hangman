class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.characters = list(chosen_word)
        self.spaces = len(self.characters)
        self.turns = 10
        self.failed = 0
        initalState = [False for i in range(self.spaces)]
        iterator = iter(self.characters)
        self.guess_dictionary = dict(zip(iterator, initalState))
    def guess_attempt (self, characters):
        if characters in self.guess_dictionary and self.guess_dictionary[characters]== False:
            self.guess_dictionary[characters] = True
            return True
        elif characters not in self.guess_dictionary:
            self.turns -= 1
            self.failed += 1
            print(f"This letter is not in the word you have {self.turns} turns left")
            return False
        else: 
            print("Looks like you already got this one, try again")
    
    def print_word(self):
        for characters in self.chosen_word:
            if self.guess_dictionary[characters] == False:
                print("_", end = ' ')
            else: 
                print(characters, end = ' ')
                # if False not in self.guess_dictionary.values():
                #     print(characters, end = ' ')
                #     print("You're a winner!")
                #     break
        print('')
 

new_word = Word("TREE")

guess = input("Guess a character:")
new_word.guess_attempt(guess)

while new_word.turns > 0: 

    if new_word.guess_attempt(guess) == True:
        if False not in new_word.guess_dictionary.values():
            new_word.print_word()
            print("You're a winner!")
            break
        else:
            new_word.print_word()
            guess = input("Guess a character:")
    else:
        if new_word.turns == 0:
            print("You have no more turns left :(")
            break
        else:
            new_word.print_word()
            guess = input("Guess a character:")


