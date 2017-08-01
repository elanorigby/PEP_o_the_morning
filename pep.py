# external
import random

# internal
import scrape
import pickler


def pick(fresh, used):
    pepo = random.choice(fresh)
    if pepo in used:
        pick(fresh, used)
    else:
        used.append(pepo)
        return pepo
    return pepo


def prep(debug=True):
    # scrape for current peps
    fresh = scrape.peps()

    # get used peps list (from pickle)
    used = pickler.read('used.p')

    # make sure that there are some unused peps, if not reset used list to empty
    if used == fresh:
        used = []

    pep = pick(fresh, used)

    # put away new list of used peps
    pickler.pickleit('used.p', used)

    # add rest of url to pep
    pepo = 'https://www.python.org' + pep

    if debug:
        print('got the pep! {}'.format(pepo))
    return pepo

prep()
