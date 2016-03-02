from os import listdir,rename,remove
from os.path import isdir,isfile,join,splitext,getsize
from click import echo,secho
import click

@click.command()
@click.option('-f',type=click.STRING, help="Folder path")
@click.option('-nm',type=click.STRING, help="Name")
def sync(f,nm):

	"""Synchronizes the names of the folder and its subcontents to the given name"""

	if isdir(f):
		for file in listFilesInDescBySize(f):
			split = splitext(file);
			if split[1] in ('.jpg','.txt','.nfo','.com'):
				remove(file)
				echo('Removed Junk File %s' %file)
			else:
				newName = join(f,nm+split[1])
				echo('Renaming %s to %s' % (file,newName))
				try:
					rename(file,newName)
				except FileExistsError:
					secho('File %s reported to be existing. So removing %s' % (newName,file),blink=True, bold=True, fg='red', bg='white')
					remove(file)
		echo('Renaming folder %s to %s' %(f,nm))
		rename(f,nm)
	else:
		raise ValueError('This command works only for directorys.')

def listFilesInDescBySize(path):
	files = []
	for file in listdir(path):
		fileName = join(path,file)
		if isfile(fileName):
			files.append(fileName)
		else:
			echo('Ignoring %s' %fileName)

	for i in range(len(files)):
		files[i] = (files[i], getsize(files[i]))

	files.sort(key=lambda fileName:fileName[1], reverse=True)
	for i in range(len(files)):
		files[i] = files[i][0]
	return files