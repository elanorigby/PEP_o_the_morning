from pushbullet import Pushbullet
from main import get_push_pep
import APIkeys

#TODO check for pusbullet.py upgrade

pb = Pushbullet(APIkeys.pushbullet)

pepo_chan = pb.channels[0]

push_pep = get_push_pep()
# print(type(push_pep))
# print(push_pep)

push = pepo_chan.push_link("PEP o' the morning to ya!", push_pep)
