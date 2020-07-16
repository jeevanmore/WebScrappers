from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=J0ecdywyFWU&list=PLiqmorr0z7mUlZfWiXlRpdFO79PcNB0kl&index=19"
youtube = YouTube(video_url)
video = youtube.streams.first()
video.download('/home/jeevan/PycharmProjects/')

