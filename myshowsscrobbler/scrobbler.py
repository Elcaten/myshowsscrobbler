import requests
import myshows
import logging
from myshowsscrobbler.config import *

class Scrobbler:
    def __init__(self):
        self._api = myshows.apiv2()
        self._api.login('myshows_lineyshikov', 'BpF6hZDja95Y65YXFem0Om05')
        logging.basicConfig(filename=LOG_FILE)

    def _getshowid(self, show):
        response = self._api.shows.Search(query=show)
        return response[0]["id"]

    def checkepisode(self, show, season, episodenumbers):
        '''Checks episode as watched'''

        results = {}
        try:
            if not isinstance(episodenumbers, list):
                episodenumbers = [episodenumbers]
            showid = self._getshowid(show)
            self._api.manage.SetShowStatus(showId=showid, status="watching")
            showepisodes = self._api.shows.GetById(showId=showid)["episodes"]
            episodeids = [episode["id"] for episode in showepisodes
                          if episode["seasonNumber"] == season
                          and episode["episodeNumber"] in episodenumbers]
            for episodeid in episodeids:
                results[episodeid] = self._api.manage.CheckEpisode(id=episodeid)
        except Exception as e:
            logging.error(f'failed to scrobble {show} | {season} | {episodenumbers}')
            logging.error(f'error: {e}')
            return False
        finally:
            return False not in results

    def getvlcstatus(self):
        status = {
            "filename": None,
            "position": 0
        }
        try:
            url = f'http://{VLC_LOGIN}:{VLC_PASSWORD}@127.0.0.1:8080/requests/status.json'
            response = requests.get(url).json()
            status["position"] = response["position"]
            meta = response["information"]["category"]["meta"]
            status["filename"] = meta["filename"]
        except Exception:
            pass
        return status
