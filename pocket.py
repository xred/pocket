import time
import json

def getNowTime(formate):
	if formate == "date":
		formate = "%Y-%m-%d"
	elif formate == "time":
		formate = "%H:%M:%S"
	elif formate == "datetime":
		formate = "%Y-%m-%d %H:%M:%S"
	theTime = time.strftime(formate,time.localtime(time.time()))
	return theTime

def timestampToDatetime(timestamp):
	formate = "%Y-%m-%d %H:%M:%S"
	dateTime = time.strftime(formate,time.localtime(timestamp))
	return dateTime

def datetimeToTimestamp(datetime):
	formate = "%Y-%m-%d %H:%M:%S"
	timestamp = time.mktime(time.strptime(datetime,formate))
	timestamp = int(timestamp)
	return timestamp

def xmlToDict(xml):
 	try:
 		import xmltodict
 	except Exception, e:
 		print e
 	theDict = xmltodict.parse(xml)
 	return theDict

def jsonToDict(json):
	theDict = json.loads(json)
	return theDict

def dictToJson(dict):
	theJson = json.dumps(dict)
	return theJson

def postJson(url,json):
	try:
		import requests
	except Exception, e:
		print e
	r = requests.post(url,data=json)
	return r

def postFile(url,name,filePath):
	try:
		import requests
	except Exception, e:
		print e
	files = {name:open(filePath,"rb")}
	r = requests.post(url,files=files)
	return r

def simplePost(url,dict):
	try:
		import requests
	except Exception, e:
		print e
	r = requests.post(url,data=dict)
	return r

class mailRose(object):
	"""simple mail class"""
	def __init__(self):
		try:
			import smtplib,mimetypes
	   		from email.mime.text import MIMEText
			from email.mime.multipart import MIMEMultipart
			from email.mime.image import MIMEImage
		except Exception, e:
			print e
		self.msg = MIMEMultipart()
		self.smtp = smtplib.SMTP_SSL()
	def setInfo(self,to,fromWho,subject,content):
		from email.mime.text import MIMEText
		self.to = to
		self.fromWho = fromWho
		self.subject = subject
		self.content = content
		self.txt = MIMEText(content.encode("utf-8"))
		self.msg['From'] = self.fromWho
		self.msg['To'] = self.to
		self.msg['Subject'] = self.subject
		self.msg.attach(self.txt)
	def serverLogin(self,server,port,account,password):
		self.smtp.connect(server,port)
		self.smtp.login(account,password)
		self.account = account
	def send(self):
		self.smtp.sendmail(self.account,self.to,self.msg.as_string())

class simpleHTTPServerPocket(object):
	staticServer = None
	def __init__(self):
		try:
			import tornado
			import tornado.ioloop
			import tornado.web
			import tornado.autoreload
			import os.path
		except Exception, e:
			print e
		def createStaticServer(a1):
			print a1
			settings = {
				"debug": True,
				"static_path":os.path.join(os.path.dirname(os.path.abspath(__file__)),"./"),
	   			"template_path":os.path.join(os.path.dirname(os.path.abspath(__file__)),"./"),
	    		"cookie_secret":"61oETzkk111aYdkL5gEmGeJJFuYjjjQnp2XdTP1o/Vo="
			}
			class mainHandler(tornado.web.RequestHandler):
				def get(self):
					self.render("index.html")
			handlers = [
				(r"/",mainHandler),
				(r"/(.*)",tornado.web.StaticFileHandler,dict(path=settings['static_path']))
			]
			application = tornado.web.Application(handlers,**settings)
			application.listen(8080)
			instance = tornado.ioloop.IOLoop.instance()
			tornado.autoreload.start(instance)
			instance.start()
		self.createStaticServer = createStaticServer

sp = simpleHTTPServerPocket()
sp.createStaticServer('fuck')
