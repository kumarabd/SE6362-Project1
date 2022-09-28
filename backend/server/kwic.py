class KWIC:
    # track all characters
    chars = []
    char_counter = 0
    # Indices of each line starting character
    line_indices = []
    word_indices = [[]]
    word_counter = 0
    alpha_indices = [[]]

    def KWIC(self):
        self.line_indices = [-1]*10
        self.chars = ["-1"]*1000

    def input(self, data: str):
        line_iterator = 0
        new_line = True
        for char in data:
            if new_line:
                self.line_indices.extend([-1]*(line_iterator+1))
                self.line_indices[line_iterator] = self.char_counter
                line_iterator = line_iterator+1
                new_line = False
            if char == '\n':
                new_line = True
                char = ' '
            self.chars.extend(["-1"]*(self.char_counter+1))
            self.chars[self.char_counter] = char
            self.char_counter = self.char_counter+1
    def circular_shift(self):
        self.word_indices.append([[-1]*len(self.line_indices)]*30)
        # To be implemented
    def make_alpha(self):
        # To be implemented
        pass
    def output(self):
        # To be implemented
        return "sample"

