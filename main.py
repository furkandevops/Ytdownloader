import pytube

url = input("enter video url: ")

savePath = ""

pytube.YouTube(url).streams.get_highest_resolution().download(savePath)