class Brainfuck:

    def __init__(self, code, stream_in):
        self.code = code
        self.code_ptr = 0
        self.data = [0]
        self.data_ptr = 0
        self.stream_in = stream_in
        self.stream_in_ptr = 0
        self.stream_out = []
        self.stream_out_ptr = 0

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
            elif instruction is ',':
                self.data[self.data_ptr] = ord(self.stream_in[self.stream_in_ptr])
                self.stream_in_ptr += 1
            elif instruction is '.':
                self.stream_out.append(chr(self.data[self.data_ptr]))
            elif instruction is '[':
                pass
            self.code_ptr += 1
        print(self.data)
        print(self.stream_out)


code = ',+.'
test = Brainfuck(code, '1')
test.run()