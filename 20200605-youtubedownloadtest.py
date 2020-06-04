import pytube

url = 'https://www.youtube.com/watch?v=AN0rQR0RlOM'
pytube.YouTube(url).streams.first().download()
pytube.YouTube(url).streams.get_high_resolution().download()
