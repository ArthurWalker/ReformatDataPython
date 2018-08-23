import re
def replace(addrses):
    new_address = addrses
    new_address=re.sub(r"\bDN3\b",' DUBLIN 3',new_address)
    new_address=re.sub(r"\b\s305 ORWELL PARK GROVE DUBLIN 6W\b",'',new_address)
    new_address=re.sub(r"\bHTS\b",' HEIGHTS',new_address)
    new_address=re.sub(r"\bBANDOC\b",' BANDON',new_address)
    new_address=re.sub(r"\bCOLAGE\b",'COLLAGE',new_address)
    new_address=re.sub(r"\bTIPPEARARY\b",'TIPPERARY',new_address)
    new_address=re.sub(r"\bCRACAWEELCROSS\b",'CRAGAWEELCROSS',new_address)
    new_address=re.sub(r"\bCALRE\b",'CLARE',new_address)
    return new_address