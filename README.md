# syncnames
Synchronizes the names of the folder and its sub contents to the given name


This is a small utiltiy that I have creted for my self.

Basically, my requirement was to synchronise the names of the files and folder with a single name for my Samsung television to pick up subtitles.

My scenario is that to get all the .srt (Subtitiles extension) files and .WHATEVER_MOVIE_FILE_FORMAT (ex: *.mp4,*.mkv,*.avi) to a single name for my televesiont
to be abel to honor the subtitiles files in the folder.

For example:

If older structure is as below-

Folder1/
		abc_1234567889.avi
		qwerty.srt
		something.jpg
		sample.avi

"syncnames -f Folder1 -nm NewName" wil make the above folder as below

NewName/
		NewName.avi
		NewName.srt

This utility deletes few temporary files like .JPG, .TXT and aslo removes the sample files (finding files based on size of file, assuming the biggest is always tehr eal movie and small ones are samples sort off)
