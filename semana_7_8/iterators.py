class RemoteControl:
    def __init__(self):
        self.channels = ["HBO", "cnn", "abc", "ESPN"]
        self.index = -1 

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1 

        if (self.index == len(self.channels)):
            raise StopIteration
        
        return self.channels[self.index]
    
r = RemoteControl()
iter = iter(r)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

    

