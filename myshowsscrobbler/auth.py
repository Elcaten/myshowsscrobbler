import webbrowser
import time
import re
from requests_oauthlib import OAuth2Session
from urllib import parse
from exceptions import *
from settings import Settings

class Auth:
    '''Authorization moudule'''
    __client_id__ = 'myshows_lineyshikov'
    __client_secret__ = 'BpF6hZDja95Y65YXFem0Om05'
    __redirect_uri__ = 'myshows://oauth-callback/myshows'
    __authorization_base_url__ = 'https://myshows.me/oauth/authorize'
    __token_url__ = 'https://myshows.me/oauth/token'
    __settings__ = Settings()

    def gettoken(self):
        '''Gets authorization token'''
        token = self.__settings__.get("token")
        if token is not None:
            return token
        self.__login__()
        for i in range(0, 5):
            token = self.__settings__.get("token")
            if token is not None:
                return token
            time.sleep(i * 5)
        raise RetrieveTokenErrorException()

    def __init__(self):
        pass

    def __login__(self):
        '''Opens myshows authorization page'''
        session = OAuth2Session(self.__client_id__, redirect_uri=self.__redirect_uri__)
        authorization_url, state = session.authorization_url(self.__authorization_base_url__)
        self.__settings__.set("state", state)
        iexplore = webbrowser.get(webbrowser.iexplore)
        iexplore.open(authorization_url)

    def __extracttoken__(self, redirecturi):
        '''Gets authorization token'''
        state = self.__settings__.get("state")
        session = OAuth2Session(self.__client_id__, state=state, redirect_uri=self.__redirect_uri__)
        query = parse.urlsplit(redirecturi).query
        code = parse.parse_qs(query)['code'][0]
        token = session.fetch_token(self.__token_url__, code, client_secret=self.__client_secret__, verify=False)
        self.__settings__.set("token", token["access_token"])

#Handle browser authorization link click
if __name__ == '__main__':
    redirect_uri = sys.argv[1]
    Auth().__extracttoken__(redirect_uri)

