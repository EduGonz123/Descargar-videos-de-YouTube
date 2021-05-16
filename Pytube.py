import pytube
import os

//Hacer, hasta que
while True:
	os.system("clear")
	
	print("\tDescargar videos de YouTube")
	print("By: Charly GM")
	url = input("\nInserte el link del video: ")
	
	youtube = pytube.YouTube(url)
	
	video = youtube.streams.first()
	
	video.download()
	
	print("\nEl video ", youtube.title, ", ha sido descargado exitosamente")
	
	pregunta = input("\n¿Desea descargar otro video? (sí = s o no = n): ")
	
	//Hasta que
	if pregunta != "s" or pregunta != "S":
		break;