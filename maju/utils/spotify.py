from maju.config import read_config
from werkzeug.exceptions import BadRequest, Unauthorized, UnprocessableEntity
import tekore as tk
import json

class SpotifySearch:
    
    def __init__(self):
        self._cfg = read_config()
        self._client_id = self._cfg.get("provider", 'sptf_id')
        self._client_secret = self._cfg.get("provider", 'sptf_secret')
    
    def auth(self):
        app_token = tk.request_client_token(self._client_id, self._client_secret)
        return tk.Spotify(app_token)

    def get_playlist(self, gender):
        playlist = []
        try:    
            spotfy_auth = self.auth()
            albuns = json.loads(spotfy_auth.category_playlists(gender).items.json())
            id_albuns = [alb['id'] for alb in albuns]
            for ids in id_albuns:
                tracks = spotfy_auth.playlist(ids)
                m = json.loads(tracks.tracks.items.json())
                for n in m:
                    info_track = n.get('track')
                    if info_track is not None:
                        track = n.get('track').get('name')
                        playlist.append(track)
                        
            return {'status': True, 'playlist': playlist}
        except Exception as e:
            print(f"Error in function get_playlist in class SpotifySearch - {str(e)}")
            
            return {'status': False, 'playlist': playlist, 'err': str(e)}
