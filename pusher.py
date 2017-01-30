from pushbullet import Pushbullet
from PEP_prep import make_push_pep
from secrets import APIkeys

#TODO check for pusbullet.py upgrade

# identify self to pushbullet api
pb = Pushbullet(APIkeys.pushapikey)

# set channel to push to
pepo_chan = pb.channels[0]

# grab a pep to push out
push_pep = make_push_pep()

# make push
push = pepo_chan.push_link("PEP o' the morning to ya!", push_pep)
