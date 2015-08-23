import urllib
import urllib2
import cookielib

def graspurl(targetUrl):
	ck = cookielib.LWPCookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ck))
	urllib2.install_opener(opener)
	
	req = urllib2.Request(targetUrl)
	operate = opener.open(req)
	msg = operate.read()
	
	fullpath = "D://"
	filename = targetUrl.replace('/','_')
	filename = filename.replace(':','.')
	filename = fullpath + filename + '.html'
	
	file_obj = open(filename, 'w')
	file_obj.write(msg)
	file_obj.close()
	
	return filename
