from pytube import YouTube
from pytube.cli import on_progress
from moviepy.editor import *
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
		yt = YouTube(str(input(" Podaj link video: ")),use_oauth=True , allow_oauth_cache=True,on_progress_callback=on_progress)
		videos = yt.streams.filter(progressive=True)

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
def converter():
	cls();
	#audioconvert convert input/ output/ --output-format .mp3
	name = str(input("wprowadź nazwę pliku "))
	source_video = name + ".mp4"
	video=VideoFileClip(source_video)
	video.audio.write_audiofile(name+".mp3")
	
##----------------------------------------------------------------------------------------------------------------------------#
def main():
	while True :
		
		print("\n MENU \n 1 - pobieranie video \n 2 - zmiana lokalizacji zapisu \n 3 - converter\n 0 - EXIT ")
		wybierz = int(input("Opcja : "))
		if wybierz == 1:
			download_video();
		if wybierz == 2:
			change_destination();
		if wybierz == 3 :
			converter();
		if wybierz == 0:
			cls();
			break
##----------------------------------------------------------------------------------------------------------------------------#			
if __name__ == '__main__':
        main()
##----------------------------------------------------------------------------------------------------------------------------#