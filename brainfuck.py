class Brainfuck:

    def __init__(self, code, stream_in=''):
        self.code = code
        self.code_ptr = 0
        self.data = [0]
        self.data_ptr = 0
        self.stream_in = stream_in
        self.stream_in_ptr = 0
        self.stream_out = []
        self.stream_out_ptr = 0

    def match(self):
        left_count = 1
        for position in range(self.code_ptr + 1, len(self.code)):
            if self.code[position] is '[':
                left_count += 1
            elif self.code[position] is ']':
                left_count -= 1
                if left_count is 0:
                    return position
        return -1

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
                code_start = self.code_ptr + 1
                code_end = self.match()
                frame = Brainfuck(self.code[code_start:code_end], self.stream_in)
                frame.data = self.data
                frame.data_ptr = self.data_ptr
                frame.stream_in_ptr = self.stream_in_ptr
                frame.stream_out = self.stream_out
                frame.stream_out_ptr = self.stream_out_ptr
                while self.data[self.data_ptr] != 0:
                    frame.code_ptr = 0
                    frame.run()
                    self.data_ptr = frame.data_ptr
                    self.stream_out_ptr = frame.stream_out_ptr
                self.code_ptr = code_end
            self.code_ptr += 1



code = '++++++++[>++++++++<-]>[<++++>-]+<[>-<[>++++<-]>[<++++++++>-]<[>++++++++<-]+>[>++++++++++[>+++++<-]>+.-.[-]<<[-]<->] <[>>+++++++[>+++++++<-]>.+++++.[-]<<<-]] >[>++++++++[>+++++++<-]>.[-]<<-]<+++++++++++[>+++>+++++++++>+++++++++>+<<<<-]>-.>-.+++++++.+++++++++++.<.>>.++.+++++++..<-.>>-[[-]<]'
test = Brainfuck(code)
test.run()
print(''.join(test.stream_out))