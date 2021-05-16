import pytube

print("\t\tDescargar videos de YouTube")
print("By: Charly_GM")

url = input("Ingrese el link del video que desea descargar: ")
youtube = pytube.YouTube(url)

video = youtube.streams.first()

video.download()