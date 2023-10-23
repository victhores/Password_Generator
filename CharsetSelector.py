import string

class CharsetSelector:
    def __init__(self, upper_letters: bool, lower_letters: bool, digits: bool, punctuation:bool, whitespace:bool):
        self.upper_letters = upper_letters
        self.lower_letters = lower_letters
        self.digits = digits
        self.punctuation = punctuation
        self.whitespace = whitespace
        self.charset = ''
        

    def include_characters(self, characters):
        if characters:
            self.charset += ''.join(characters)

    def configure_charset(self):
        self.include_characters(string.ascii_uppercase if self.upper_letters else '')
        self.include_characters(string.ascii_lowercase if self.lower_letters else '')
        self.include_characters(string.digits if self.digits else '')
        self.include_characters(string.punctuation if self.punctuation else '')
        self.include_characters(string.whitespace if self.whitespace else '')
        
        return self.charset


