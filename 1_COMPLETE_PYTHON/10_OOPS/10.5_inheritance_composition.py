"""Inheritance means ek class dusri 
class ke features (methods & variables) use karti hai. 
Relation: IS-A

Composition means ek class ke andar dusri class ka object 
use karna.

➡️ Relation: HAS-A"""

class BaseChai:
    def __init__(self,type_):
        self.type=type_

    def prepare(self):
        print(f"preparing {self.type} chai___.....")


class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding Cardamom,ginger,cloves")

class Chaishop:
    chai_cls=BaseChai

    def __init__(self):
        self.chai=self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()



class FancyChaiShop(Chaishop):
    chai_cls=MasalaChai


shop=Chaishop()
fancy=FancyChaiShop()
shop.serve()
fancy.serve()
 