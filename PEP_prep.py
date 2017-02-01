from PEPSoup import get_fresh_peps
from pickle_town import pickle_it, read_pickle
import random


def make_push_pep(debug=True):
    # scrape for current peps
    fresh_peps = get_fresh_peps()

    # get used_peps list (from pickle)
    used_peps = read_pickle('used.p')

    # make sure that there are some unused peps, if not reset used list to empty
    if used_peps == fresh_peps:
        used_peps = []

    def get_pepo():
        pepo = random.choice(fresh_peps)
        if pepo in used_peps:
            get_pepo()
        else:
            used_peps.append(pepo)
            return pepo

    pepo = get_pepo()

    pickle_it('used.p', used_peps)

    push_pep = 'https://www.python.org' + pepo

    if debug:
        print('got the pep! {}'.format(push_pep))

    return push_pep

