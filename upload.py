# upload the video to relvant platforms as given by the parameters


import datetime
import time
from googleapiclient.http import MediaFileUpload
import pandas as pd
from google_apis import create_service

def video_categories():
    video_categories = service.videoCategories().list(part='snippet', regionCode='US').execute()
    df = pd.DataFrame(video_categories.get('items'))
    return pd.concat([df['id'], df['snippet'].apply(pd.Series)[['title']]], axis=1)

API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube']
# SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
client_file = 'act1_edigen.json'
service = create_service(client_file, API_NAME, API_VERSION, SCOPES)

print(video_categories())

"""
Step 1. Uplaod Video
"""
upload_time = (datetime.datetime.now() + datetime.timedelta(days=10)).isoformat() + '.000Z'
request_body = {
    'snippet': {
        'title': '<video title>',
        'description': '<video description>',
        'categoryId': '<category id>',
        'tags': ['tags']
    },
    'status': {
        'privacyStatus': 'private',
        'publishedAt': upload_time,
        'selfDeclaredMadeForKids': False
    },
    'notifySubscribers': False
}

video_file = 'demo video.mp4'
media_file = MediaFileUpload(video_file)
# print(media_file.size() / pow(1024, 2), 'mb')
# print(media_file.to_json())
# print(media_file.mimetype())

response_video_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=media_file
).execute()
uploaded_video_id = response_video_upload.get('id')



'''
class Upload:
    def __innit__(self):
        pass
'''