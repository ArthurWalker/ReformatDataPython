import re
def replace(addrsess):
    new_address = addrsess
    new_address=re.sub(r"\bDN3\b",'DUBLIN 3',new_address)
    new_address=re.sub(r"\b\s305 ORWELL PARK GROVE DUBLIN 6W\b",'',new_address)
    new_address=re.sub(r"\bHTS\b",'HEIGHTS',new_address)
    new_address=re.sub(r"\bBANDOC\b",'BANDON',new_address)
    new_address=re.sub(r"\bCOLAGE\b",'COLLAGE',new_address)
    new_address=re.sub(r"\bTIPPEARARY\b",'TIPPERARY',new_address)
    new_address=re.sub(r"\bCRACAWEELCROSS\b",'CRAGAWEELCROSS',new_address)
    new_address=re.sub(r"\bCALRE\b",'CLARE',new_address)
    new_address=re.sub(r"\bCLAUIN\b",'CLUAIN',new_address)
    new_address=re.sub(r"\bCOMAYO\b",'MAYO',new_address)
    new_address=re.sub(r"\bWEXFOD\b",'WEXFORD',new_address)
    new_address=re.sub(r"\bWESFORD\b",'WEXFORD',new_address)
    new_address=re.sub(r"\bWICLOW\b",'WICKLOW',new_address)
    new_address=re.sub(r"\bKILCAVANCO\b",'KILCAVAN',new_address)
    return new_address