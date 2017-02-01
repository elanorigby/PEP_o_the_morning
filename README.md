# PEP_o_the_morning
Feed for a Pushbullet channel that sends a random Python PEP to you every morning

####Uses

[**BeautifulSoup4**](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

to scrape PEPs from https://www.python.org/dev/peps/

and

[**Pushbullet.py**](https://github.com/randomchars/pushbullet.py) to push the PEPs to a pushbullet channel

*TODO*
* put this jazz on pythonanywhere and set it to run once a day
* link pushbullet channel



#### How to Run
* Make a virtualenv (or whatever)
* Install requirements
* get youself an api key from Pushbullet
* Run `python3 pusher.py` from within project folder