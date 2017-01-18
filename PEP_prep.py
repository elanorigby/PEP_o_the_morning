from PEPSoup import get_PEP_set
from pickle_town import pickle_it, read_pickle
import random


def get_push_pep():
    peps = get_PEP_set()
    ref_pickle = 'ref.pickle'
    use_pickle = 'use.pickle'

    # read ref and use pickles into vars ref and use
    ref_set = read_pickle(ref_pickle)
    use_set = read_pickle(use_pickle)

    if not use_set:
        pickle_it(use_pickle, peps)
        use_set = read_pickle(use_pickle)

    # compare against ref file
    if ref_set < peps:
        # if difference, add new items to ref and use files
        new_peps = peps.difference(ref_set)
        ref_set.update(new_peps)
        use_set.update(new_peps)

    # get random pep from use set
    pepo = random.choice(list(use_set))

    # remove that pep from use set
    use_set.remove(pepo)

    # attach pep to rest of url
    push_pep = 'https://www.python.org' + pepo
    return push_pep

