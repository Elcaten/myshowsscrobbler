import webbrowser
from requests_oauthlib import OAuth2Session

class MyshowsVlcScrobbler:
    '''MyShows scrobbler for VLC'''
    client_id = 'myshows_lineyshikov'
    redirect_uri = 'myshows://oauth-callback/myshows'
    authorization_base_url = 'https://myshows.me/oauth/authorize'
    token_url = 'https://myshows.me/oauth/token'
    token = None

    def __init__(self):
        self.state = None

    def login(self):
        '''Opens myshows authorization page'''
        session = OAuth2Session(self.client_id, scope='basic', redirect_uri=self.redirect_uri)
        authorization_url, state = session.authorization_url(self.authorization_base_url)
        self.state = state
        iexplore = webbrowser.get(webbrowser.iexplore)
        iexplore.open(authorization_url)

    def retrievetoken(self, authresponse):
        '''Retrieves authorization token from browser redirect
           TODO: handle invalid state exception'''
        session = OAuth2Session(self.client_id, state=self.state)
        self.token = session.token_from_fragment(authresponse)
