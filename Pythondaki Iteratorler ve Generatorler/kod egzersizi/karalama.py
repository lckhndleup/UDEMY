"""class Kumanda():
    def __init__(self,kanal_listesi):
        self.kanal_listesi=kanal_listesi
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1

        if self.index<len(self.kanal_listesi):
            return self.kanal_listesi[self.index]
        else:
            self.index=-1
            raise StopIteration

kumanda=Kumanda(["atv","kanald","trt","fox","bloomberg"])

iterator=iter(kumanda)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break"""

