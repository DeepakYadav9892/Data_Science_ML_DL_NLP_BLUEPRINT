##Accessing Base class
##Code Duplication 
##Explicit call , super()

class Chai:
    def __init__(self,type_,strength):
        self.type=type_
        self.strength=strength

class GingerChai(Chai):
    def __init__(self, type_, strength,spice_level):
        super().__init__(type_, strength)


