from pytube import YouTube

link = input("Link: ")                   # Here, the link is taken from the user

yt = YouTube(link)
ys = yt.streams.get_highest_resolution() # Video resolution is set here.

print("Downloading...")
ys.download()                            # Downloading takes place here.
print("Downloaded.")
