from pytube import YouTube
import os

def cls():
	os.system("cls")
##----------------------------------------------------------------------------------------------------------------------------#

cls();
try :
	fo = open("location.txt", "r+")
	path = fo.read();
	fo.close()
	print(" Lokalizacja zapisu - ", path)
except (OSError, IOError) :
	print(" \n Brak lokalizacji zapisu plików. \n Ustal Lokalizację")
##----------------------------------------------------------------------------------------------------------------------------#
def download_video() :
	cls();
	try :
		fo = open("location.txt", "r+")
		destination = fo.read();
		fo.close()
	except (OSError, IOError) :	
		print(" \n Brak lokalizacji zapisu plików. \n Ustal Lokalizację")
		destination = None

	if destination  is None :
		print ("\n***************\n NO SAVE PATH\n***************")
	else :
		yt = YouTube(str(input(" Podaj link video: ")))
		videos = yt.streams.filter(progressive=True , file_extension='mp4').all()

		s = 1
		for v in videos:
			print(str(s)+". "+str(v))
			s += 1

		n = int(input(" Wybierz numer porządanego video: "))
		vid = videos[n-1]

		vid.download(destination)
		print(yt.title +"\nFile Has been successfully downloaded")
##----------------------------------------------------------------------------------------------------------------------------#	
def change_destination() :
	cls();
	fo = open("location.txt", "w")
	destination2 = str(input("Wprowadz ścieżkę: ")) 
	fo.write(destination2);
	fo.close()
	
##----------------------------------------------------------------------------------------------------------------------------#
def main():
	while True :
		
		print("\n MENU \n 1 - pobieranie video \n 2 - zmiana lokalizacji zapisu \n 0 - EXIT ")
		wybierz = int(input("Opcja : "))
		if wybierz == 1:
			download_video();
		if wybierz == 2:
			change_destination();
		if wybierz == 0:
			cls();
			break
##----------------------------------------------------------------------------------------------------------------------------#			
if __name__ == '__main__':
        main()
##----------------------------------------------------------------------------------------------------------------------------#