from data import Data

class Brainf_ck:
    """Return the results of Brainf*ck code."""

    def __init__(self, code, stdin=''):

        self.code = Data(code)
        self.data = Data([0])
        self.stdin = Data()
        self.stdout = Data()

        self.depth = 0
    

    def __add(self):
        self.data[self.data.ptr] += 1


    def __sub(self):
        self.data[self.data.ptr] -= 1


    def __inc_ptr(self):
        self.data.ptr += 1
        if self.data.ptr >= len(self.data):
            self.data.append(0)


    def __dec_ptr(self):
        self.data.ptr -= 1
        if self.data.ptr < 0:
            print('data.ptr out of bounds')
            exit(-1)


    def __read_stdin(self):
        if self.stdin.ptr >= len(self.stdin):
            print('stdin_ptr out of bounds')
            exit(-1)
        self.data[self.data.ptr] = ord(self.stdin[self.stdin.ptr])
        self.stdin.ptr += 1


    def __write_stdout(self):
        self.stdout.append(self.data[self.data.ptr])


    def __match_bracket(self):
        """Return matching end bracket."""
        left_count = 1
        for position in range(self.code.ptr + 1, len(self.code)):
            if self.code[position] == '[':
                left_count += 1
            elif self.code[position] == ']':
                left_count -= 1
                if left_count == 0:
                    return position


    def __bracket(self):
        """Return the results of code inside two matching brackets."""
        code_start = self.code.ptr + 1
        code_end = self.__match_bracket()
        frame = Brainf_ck(self.code[code_start:code_end], self.stdin)
        frame.data = self.data
        frame.data.ptr = self.data.ptr
        frame.stdin.ptr = self.stdin.ptr
        frame.stdout = self.stdout
        while self.data[self.data.ptr] != 0:
            frame.code.ptr = 0
            frame.depth = self.depth + 1
            frame.run()
            self.data.ptr = frame.data.ptr
        self.code.ptr = code_end


    def __str__(self):
        """Convert stdout to ascii character string"""
        txt = []
        for i in range(len(self.stdout)):
            txt.append(chr(self.stdout[i] % 255))
        return ''.join(txt)


    def run(self):
        while self.code.ptr < len(self.code):
            instruction = self.code[self.code.ptr]
            if instruction == '+':
                self.__add()
            elif instruction == '-':
                self.__sub()
            elif instruction == '>':
                self.__inc_ptr()
            elif instruction == '<':
                self.__dec_ptr()
            elif instruction == ',':
                self.__read_stdin()
            elif instruction == '.':
                self.__write_stdout()
            elif instruction == '[':
                self.__bracket()
            self.code.ptr += 1
