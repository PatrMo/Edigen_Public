# upload the video to relvant platforms as given by the parameters


import datetime
from googleapiclient.http import MediaFileUpload
import pandas as pd
from google_apis import create_service


class upload:
    # class for uploading shorts ---> change id in request_body for different format

    def __init__(self):
        API_NAME = 'youtube'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/youtube']
        client_file = 'act1_edigen.json'

        self.service = create_service(client_file, API_NAME, API_VERSION, SCOPES)

        self.title = ''
        self.description = ''
        self.uploadTime = ''
        self.tags = []
        self.priv_status = ''
        self.media_file = ''

    def setVideoFile(self,video_file):
        self.media_file = MediaFileUpload(video_file)
        # print(media_file.size() / pow(1024, 2), 'mb')
        # print(media_file.to_json())
        # print(media_file.mimetype())
        self.setRequestBody()

    def setTitle(self, given_title):
        self.title = given_title
        self.setRequestBody()

    #uploads an inputted number of hours from current time.
    def setUploadTime(self, added_time):
        # must be in ISO 8601 time format, example: '2020-07-10 15:00:00.000'
        self.uploadTime = (datetime.datetime.now() + datetime.timedelta(hours=added_time)).isoformat() + '.000Z'
        self.setRequestBody()
    
    def setDescription(self,desc):
        self.description = desc
        self.setRequestBody()

    # string list input type for tags
    def setTags(self,tag_list):
        self.tags = tag_list
        self.setRequestBody()

    def setPrivStatus(self,priv):
        self.priv_status = priv
        self.setRequestBody()

    def setRequestBody(self):
        #all of the video info is set here
        self.request_body = {
            'snippet': {
                'title': self.title,
                'description': self.description,
                'categoryId': 29,
                'tags': self.tags
            },
            'status': {
                'privacyStatus': self.priv_status,
                'publishedAt': self.uploadTime,
                'selfDeclaredMadeForKids': False
            },
            'notifySubscribers': False
        }

    def uploadVideo(self):
        self.service.videos().insert(
            part='snippet,status',
            body=self.request_body,
            media_body=self.media_file
        ).execute()
        print('Video Uploaded with ', self.request_body)


def upload_main():
    vid = upload()
    vid.setVideoFile('test.mp4')
    vid.setTitle('Title')
    vid.setDescription('Test Description') #long string
    vid.setTags(['shorts', 'informational', 'subwaysurfers']) #insert a list of string representing tags ---> may use same list for all vidoes in future
    vid.setPrivStatus('private') #changfe to public when youtube account gets authorized
    vid.setUploadTime(1) 
    vid.uploadVideo()
