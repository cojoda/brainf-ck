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
