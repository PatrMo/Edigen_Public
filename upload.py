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
client_file = 'act1_edigen.json'
service = create_service(client_file, API_NAME, API_VERSION, SCOPES)

print(video_categories())



class upload:
    # class for uploading videos

    def __init__(self, video_file):
        self.title = ''
        self.description = ''
        self.uploadTime = ''
        self.tags = []

        self.media_file = MediaFileUpload(video_file)
        # print(media_file.size() / pow(1024, 2), 'mb')
        # print(media_file.to_json())
        # print(media_file.mimetype())
        pass

    def setTitle(self, given_title):
        self.title = given_title

    #uploads an inputted number of hours from current time.
    def setUploadTime(self, added_time):
        # must be in ISO 8601 time format, example: '2020-07-10 15:00:00.000'
        self.uploadTime = (datetime.datetime.now() + datetime.timedelta(hours=added_time)).isoformat() + '.000Z'
    
    def setDescription(self,desc):
        self.description = desc

    # string list input type for tags
    def setTags(self,tag_list):
        self.tags = tag_list

    def setPrivStatus(self,privStatus):
        self.priv = privStatus

    def video_upload(self):
        service.videos().insert(
            part='snippet,status',
            body=self.request_body,
            media_body=self.media_file
        ).execute()


    def request_body(self):
        self.request_body = {
            'snippet': {
                'title': self.title,
                'description': self.description,
                'categoryId': 42,
                'tags': ['tags']
            },
            'status': {
                'privacyStatus': self.priv,
                'publishedAt': self.time,
                'selfDeclaredMadeForKids': False
            },
            'notifySubscribers': False
        }
      


'''
request_body = {
    'snippet': {
        'title': '<video title>',
        'description': '<video description>',
        'categoryId': 42,
        'tags': ['tags']
    },
    'status': {
        'privacyStatus': 'private',
        'publishedAt': upload.time(hours=1),
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


'''


'''
class Upload:
    def __innit__(self):
        pass
'''
