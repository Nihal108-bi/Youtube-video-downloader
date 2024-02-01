from pytube import YouTube

link= input("Enter the youtube link: ")

print(str(link))
youtube_1=YouTube(link)

print("Video title: ")
print(youtube_1.title)
#print(youtube_1.thumbnail_url)
videos=youtube_1.streams.all()                     #all format
#video=youtube_1.streams.filter(only_audio=True)    #only audio
vid=list(enumerate(videos))
for i in vid:
    print(i)

print()
strm=int(input("Enter: "))
videos[strm].download()
print("Successfully")


#*******playlist list Download******

# from pytube import Playlist
# py=Playlist("https://youtube.com/playlist?list=PLfIsZ7BXA3FxtVxiihzBD7Wm1b5Q1lkTh&si=jcg0kO0EhMGdT2n1")

# print(f'Downloading : {py.title}')

# for video in py.videos:
#     video.streams.first().download()
