from pushbullet import Pushbullet

from secrets import APIkeys
from prepare import make_push_pep
import flaskapp


# identify self to pushbullet api
pb = Pushbullet(APIkeys.pushapikey)

# set channel to push to
channel = pb.channels[0]

# grab a pep to push out
push_pep = make_push_pep()

# push it out
push = channel.push_link("PEP o' the morning to ya!", push_pep)

# update flask app with current pep
flaskapp.update(push_pep)



# TODO check for pusbullet.py upgrade
