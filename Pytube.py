import pytube
import os

while True:
	os.system("clear")
	
	print("\t Descargar videos de YouTube")
	print(" By: Charly GM")
	url = input("\n Pegue el link del video que desea descargar: ")
	
	carpetaAndroid = "mkdir /sdcard/Descargas CharlyTube"
	
	youtube = pytube.YouTube(url)
	
	video = youtube.streams.first()
	
	video.download(carpetaAndroid)
	
	print("\n El video ", youtube.title, ", ha sido descargado exitosamente")
	
	pregunta = int(input("\n ¿Desea descargar otro video? (sí = 1 o no = 2): "))
	
	if pregunta == 2:
		break;
