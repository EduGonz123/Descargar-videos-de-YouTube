import pytube
import os

while True:
	os.system("clear")
	
	print("\t\tDescargar videos de YouTube")
	print("By: Charly_GM")
	url = input("Inserte el link del video: ")
	
	youtube = pytube.YouTube(url)
	
	print("\nEl video ", youtube.title, ", ha sido descargado exitosamente")
	
	video = youtube.streams.first()
	
	video.download("sdcard/WhatsApp")
	
	pregunta = input("\n¿Desea descargar otro video? (sí = s o no = n): ")
	
	if pregunta == 's' or pregunta == 'S':
		break;