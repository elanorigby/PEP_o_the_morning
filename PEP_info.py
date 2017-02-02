import re

def pep_num(pep):
    num = re.search(r'\d+', pep)
    return num.group(0)

