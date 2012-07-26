try:
	import urllib2 #urllib is in python 2.7 and later standard libraries 
except:
	print('You need to install the URLLIB2')

#Download web files. Takes a url and writes the file into the specified folder. 

url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip' #URL to download data from

def Json_Query(url):
	print('downloading with urllib2')
	File = urllib2.urlopen(url) #Open the Webpage
	data = File.read() #Read data from webpage.
	with open("Json_File.zip", "wb") as Json_file: #Write data into the selected folder.
		Json_file.write(data)
	print(data) #You can also print the data on the command line. 
