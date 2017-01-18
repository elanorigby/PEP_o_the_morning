from pushbullet import Pushbullet
from PEP_prep import get_push_pep
import APIkeys

#TODO check for pusbullet.py upgrade

# identify self to ppushbullet api
pb = Pushbullet(APIkeys.pushbullet)

# set channel to push to
pepo_chan = pb.channels[0]

# grab a pep to push out
push_pep = get_push_pep()

# make push
push = pepo_chan.push_link("PEP o' the morning to ya!", push_pep)
