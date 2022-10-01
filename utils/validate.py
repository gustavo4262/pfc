

def validateStringEssential(ide):
    if not ide:
        raise Exception("Bad Request")



def validateBooleanEssential(ide):
    if not (ide == "1" or ide == "0"):
        raise Exception("Bad Request")
