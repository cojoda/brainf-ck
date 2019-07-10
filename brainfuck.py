class Brainfuck:

    def __init__(self, code, stdin=''):
        self.code = code
        if type(self.code) is str:
            self.code = list(self.code)
        self.code_ptr = 0
        self.data = [0]
        self.data_ptr = 0
        self.stdin = stdin
        if type(self.stdin) is str:
            self.stdin = list(self.stdin)
        self.stdin_ptr = 0
        self.stdout = []
        self.depth = 0

    # finds index of matching bracket ']'
    def match(self):
        left_count = 1
        for position in range(self.code_ptr + 1, len(self.code)):
            if self.code[position] is '[':
                left_count += 1
            elif self.code[position] is ']':
                left_count -= 1
                if left_count is 0:
                    return position

    def run(self):
        while self.code_ptr < len(self.code):
            instruction = self.code[self.code_ptr]
            if instruction is '+':
                self.data[self.data_ptr] += 1
            elif instruction is '-':
                self.data[self.data_ptr] -= 1
            elif instruction is '>':
                self.data_ptr += 1
                if self.data_ptr >= len(self.data):
                    self.data.append(0)
            elif instruction is '<':
                self.data_ptr -= 1
                if self.data_ptr < 0:
                    print('data_ptr out of bounds')
                    exit(-1)
            elif instruction is ',':
                if self.stdin_ptr >= len(self.stdin):
                    print('stdin_ptr out of bounds')
                    exit(-1)
                self.data[self.data_ptr] = ord(self.stdin[self.stdin_ptr])
                self.stdin_ptr += 1
            elif instruction is '.':
                self.stdout.append(self.data[self.data_ptr])
            elif instruction is '[':
                code_start = self.code_ptr + 1
                code_end = self.match()
                frame = Brainfuck(self.code[code_start:code_end], self.stdin)
                frame.data = self.data
                frame.data_ptr = self.data_ptr
                frame.stdin_ptr = self.stdin_ptr
                frame.stdout = self.stdout
                while self.data[self.data_ptr] != 0:
                    frame.code_ptr = 0
                    frame.depth = self.depth + 1
                    frame.run()
                    self.data_ptr = frame.data_ptr
                self.code_ptr = code_end
            self.code_ptr += 1
        # if frame stack depth = 0 (at head) convert to ascii string with overflow support
        if self.depth == 0:
            for stdout_ptr in range(len(self.stdout)):
                self.stdout[stdout_ptr] = chr(self.stdout[stdout_ptr] % 255)
            self.stdout = ''.join(self.stdout)
            