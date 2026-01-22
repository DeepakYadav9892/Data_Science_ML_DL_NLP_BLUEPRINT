class TeaLeaf:
    def __init__(self):
        self._age=age
@property
def age():
    return self._age +2

@age.setter
def age(self,age):
    if 1 <=age <=5:
        self._age=age
    else:
        raise ValueError("Tea leaf age must be between 1 annd 5 years ")

        