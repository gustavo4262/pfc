

def validateStringEssential(ide):
    if not ide:
        raise Exception("Bad Request")



def validateBooleanEssential(ide):
    if not (ide == "True" or ide == "False"):
        raise Exception("Bad Request")
