import requests
from flask import Flask , request ,jsonify
app=Flask(__name__)
@app.route("/")
def f():
	return "<h1> السلام عليكم ورحمة الله وبركاته </h1>"
@app.route("/api/check/")
def f6():
	number = request.args.get("number")
	code = request.args.get("code")
	if '011' in number:
	    na = replace('0', '')
	url = 'https://mab.etisalat.com.eg:11003/Saytar/rest/quickAccess/verifyCodeQuickAccess'
	headers = {"applicationVersion": "2",
    "applicationName": "MAB",
    "Accept": "text/xml",
    "applicationPassword": "ZFZyqUpqeO9TMhXg4R/9qs0Igwg\u003d",
    "APP-BuildNumber": "547",
    "APP-Version": "22.13.0",
    "OS-Type": "Android",
    "OS-Version": "10",
    "APP-STORE": "Huawei",
    "Is-Corporate": "false",
    "Content-Type": "text/xml; charset\u003dUTF-8",
    "Content-Length": "214",
    "Host": "mab.etisalat.com.eg:11003",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.12.8",
    "ADRUM_1": "isMobile:true",
    "ADRUM": "isAjax:true"}
	data = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><verifyCodeQuickAccessRequest><dial>%s</dial><udid>5245f6e7-8f3d-41cc-8bb4-ee83392bed4b</udid><verCode>%s</verCode></verifyCodeQuickAccessRequest>" %(na,code)
	a = requests.post(url,headers=headers,data=data)
	if 'true' in a.text:
		c = a.headers["Set-Cookie"]
		token = c[:-117]		
		return jsonify(result="good",token=token) 	
	else:
		return jsonify(result="Try Again")				

app.run(host='0.0.0.0', port=8080)
