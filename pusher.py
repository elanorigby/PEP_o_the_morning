from pushbullet import Pushbullet

from secrets import APIkeys
from PEP_prep import make_push_pep

def push_it_real():
    # identify self to pushbullet api
    pb = Pushbullet(APIkeys.pushapikey)

    # set channel to push to
    pepo_chan = pb.channels[0]

    # grab a pep to push out
    push_pep = make_push_pep()

    # push it out
    push = pepo_chan.push_link("PEP o' the morning to ya!", push_pep)

    return push_pep



# TODO check for pusbullet.py upgrade
