# a file to download videos and caption from youtube / gain relvenat inforamion on that video
from pytube import YouTube, Caption
import json

class Download:
    '''Class for downloading youtube scripts'''
    yt : YouTube
    captions : Caption

    def __init__(self, url) -> None:
        '''Creates a new youtube link object from youtube library'''
        self.yt = YouTube(f'https://www.youtube.com/watch?v={url}')

    def download(self):
        '''Downloads highest quality video available'''
        self.yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download()

    def len_video(self):
        '''Returns length of video'''
        return self.yt.length

    def cap(self):
        '''Returns caption of vidoe in json object'''
        self.yt.streams.first()
        captions = self.yt.captions['a.en']
        return captions.json_captions


if __name__ == '__main__':
    # donwload Video
    video = Download('LrIRuqr_Ozg')
    video.download()

    with open('output.json', "w") as json_file:
        json.dump(video.cap(), json_file, indent=1)