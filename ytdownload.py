from pytube import YouTube

fo = open("location.txt", "r+")
destination = fo.read();
print ("Lokalizacja zapisu : ", destination)
# Close opend file
fo.close()


def download_video() :
	yt = YouTube(str(input("Podaj link video: ")))
	videos = yt.streams.filter(progressive=True , file_extension='mp4').all()

	s = 1
	for v in videos:
		print(str(s)+". "+str(v))
		s += 1

	n = int(input("Wybierz numer porządanego video: "))
	vid = videos[n-1]

	vid.download(destination)
	print(yt.title +"\nFile Has been successfully downloaded")
	
def change_destination() :
	fo = open("location.txt", "w")
	destination2 = str(input("Wprowadz ścieżkę: ")) 
	fo.write(destination2);
	fo.close()
	fo = open("location.txt", "r+")
	destination = fo.read();
	print ("Lokalizacja zapisu : ", destination)
	fo.close()

def main():
	while True : 
		print(" Menu \n 1 - pobieranie video \n 2 - zmiana lokalizacji zapisu \n 0 - EXIT ")
		wybierz = int(input("Opcja : "))
		if wybierz == 1:
			download_video();
		if wybierz == 2:
			change_destination();
		if wybierz == 0:
			break
			
if __name__ == '__main__':
        main()