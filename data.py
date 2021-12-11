class Data():

    def __init__(self, body=[]):

        if type(body) == str:
            self.body = list(body)
        elif type(body) == list:
            self.body = body

        self.ptr = 0


    def __len__(self):
        return len(self.body)


    def __getitem__(self, key):
        return self.body[key]


    def __setitem__(self, key, value):
        self.body[key] = value
    

    def __str__(self):
        return f'{self.body}'


    def append(self, value):
        self.body.append(value)
  