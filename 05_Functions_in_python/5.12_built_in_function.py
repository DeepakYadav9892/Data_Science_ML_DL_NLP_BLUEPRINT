

def chai_flavor(flavour="masala"):
    """Return the flavour of chai. """
    return flavour

print(chai_flavor.__doc__)
print(chai_flavor.__name__)
help(len)

def generate_bill(chai=0,samosa=0):
    """
    Docstring for generate_bill
    
    :param chai: Description
    :param samosa: Description
    Calculate the total bill for chai and samosa 
    :Param chai : Number of chai cups (10 rupees each )
    :param samosa:Number fo samosa (15 rupess each )
    :return : (total amount , thank you message)
    """

    total=chai*10+samosa*15
    return total,"Thank you for visiting chaicode.com"