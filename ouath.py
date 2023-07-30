import requests

CLIENT_ID = "198f75998f7dc4f1198f75970400f56"
CLIENT_SECRET = "3pdc4f1198f759Ey4yFPR24198f759ZzO"
REDIRECT_URI = "http://localhost:5000/oauth"

class Oauth:
    
    def __init__(self):
        self.auth_server = "https://kauth.kakao.com%s"
        self.api_server = "https://kapi.kakao.com%s"
        self.default_header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache",
        }

    def auth(self, code):
        return requests.post(
            url=self.auth_server % "/oauth/token", 
            headers=self.default_header,
            data={
                "grant_type": "authorization_code",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uri": REDIRECT_URI,
                "code": code,
            }, 
        ).json()


    def refresh(self, refresh_token):
        return requests.post(
            url=self.auth_server % "/oauth/token", 
            headers=self.default_header,
            data={
                "grant_type": "refresh_token",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "refresh_token": refresh_token,
            }, 
        ).json()


    def userinfo(self, bearer_token):
        return requests.post(
            url=self.api_server % "/v2/user/me", 
            headers={
                **self.default_header,
                **{"Authorization": bearer_token}
            },
            #"property_keys":'["kakao_account.profile_image_url"]'
            data={}
        ).json()