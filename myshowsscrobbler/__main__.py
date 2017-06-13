import logging
from time import sleep
from myshowsscrobbler.scrobbler import Scrobbler
from myshowsscrobbler.filenameparser import parse_tv
from myshowsscrobbler.config import *

logging.basicConfig(filename=LOG_FILE)
scrobbler = Scrobbler()
lastscrobbled = None

while True:
    sleep(60)
    status = scrobbler.getvlcstatus()
    if status["position"] > 0.85 and status["filename"] != lastscrobbled:
        series = parse_tv(status["filename"])
        if not series:
            logging.error(f'{status["filename"]} failed to scrobble')
            continue
        succesfullyscrobbled = scrobbler.checkepisode(series["show"], series["season"], series["episodes"])
        if succesfullyscrobbled:
            lastscrobbled = status["filename"]
            logging.info(f'{status["filename"]} successfully scrobbled')
        else:
            logging.error(f'{status["filename"]} failed to scrobble')
