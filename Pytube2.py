from pytube import YouTube

link=input("inserte el enlace del video: ")
yt=YouTube(link)
lista= yt.streams.all()
for st in lista:
    print(st)

codigo=int(input("digite el itag de la calidad de video que desea: "))

st=yt.streams.get_by_itag(codigo)
st.download()
