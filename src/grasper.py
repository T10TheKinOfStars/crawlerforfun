import os
import datetime
import urllib
import urllib2
import cookielib


def GetDateStr():
    from datetime import date
    dateStr = date.today().strftime("%Y_%m_%d")
    return dateStr

def MkNewDir(newDir=None):
	if newDir is None:
		newDirCreated = "./" + GetDateStr()
	else:
		newDirCreated = "./" + newDir
	os.mkdir(newDirCreated)
	return newDirCreated

def graspurl(targetUrl, targetDir=None):
	ck = cookielib.LWPCookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ck))
	urllib2.install_opener(opener)
	
	req = urllib2.Request(targetUrl)
	operate = opener.open(req)
	msg = operate.read()

	if targetDir and os.path.isdir("./"+targetDir):
		print(targetDir," Exists already ")
		fullpath = os.getcwd() + "/" + targetDir
	else:
		fullpath = os.getcwd() + MkNewDir(targetDir)

	filename = targetUrl.replace('/','_')
	filename = filename.replace(':','.')
	filename = fullpath + "/" + filename + '.html'
	
	file_obj = open(filename, 'w')
	file_obj.write(msg)
	file_obj.close()
	
	return filename
