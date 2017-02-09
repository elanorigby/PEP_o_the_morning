import re

def pep_num(pep):
    num = re.search(r'\d+', pep)
    return num.group(0)

# TODO: make sure you don't need this module and then delete it