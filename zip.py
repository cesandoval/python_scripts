import zipfile
import os

#Extracts files on a zip file into a given directory, if no directory is given, 
#it extracts the files into the zip file directory.
def unzip_file(zip_file, my_path=None):
	zip_file = zipfile.ZipFile(zip_file) #open the zip file
	
	if my_path != None: #if directory is given, and doesn't exist, create directory.
		if not os.path.isdir(my_path):
			try:
				os.makedirs(my_path)
			except OSError:
				pass
					
		for f in zip_file.namelist(): #extract all the files into the given directory
			zip_file.extract(f, my_path=None)
	
	else: #if no directory is given, extract the files into the zipfiles's directory.
		for f in zip_file.namelist():
			zip_file.extract(f)


zip_file = 'C:\Users\carlos\Desktop\python\Json_File.zip' #set the zipfile's directory.
#my_path = 'C:\Users\carlos\Desktop\python\Json_File' #set the directory to extract files.

unzip_file(zip_file)

#testing git

