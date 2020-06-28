from maju.config import read_config
from werkzeug.exceptions import BadRequest, Unauthorized, UnprocessableEntity
import json, requests

class DeezerSearch:
    
    def __init__(self):
        self._cfg = read_config()
        self._url_deezer = self._cfg.get("provider", 'url_deezer')

    def gender_parser(self, gender):
        playlists = {
            'rock': '6046716724',
            'pop': '2021502402',
            'classic': '4590803744'
        }
        return playlists[gender]

    def get_playlist(self, gender):
        playlist = []
        try:
            request = requests.get(self._url_deezer + f'/{self.gender_parser(gender)}/tracks', timeout=5)
            response = request.json()
            playlist = [music['title'] for music in response['data']]
            
            return {'status': True, 'playlist': playlist}
        except Exception as e:
            print(f"Error in function get_playlist in class DeezerSearch - {str(e)}")
            
            return {'status': False, 'playlist': playlist, 'err': str(e)}