#coding:utf-8
import requests
import json
class RunMethod():
	def post_main(self,url,data=None,headers=None):
		if headers !=None:
			res = requests.post(url=url,data=data,headers=headers).text
		else:
			res = requests.post(url=url,data=data).text
		return res
	def get_main(self,url,params=None,headers=None):
		if params == None:
			res = requests.get(url=url,params=None,headers=headers).text
		else:
			res = requests.get(url=url,params=data,headers=headers).text
		return res
	def run_main(self,method,url,data=None,headers=None):
		if method =='post':
			res = self.post_main(url,data,headers)
		else:
			res = self.get_main(url,data,headers)
		return res
		#json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
# if __name__ == '__main__':
# 	run = RunMethod()
# 	url = 'http://47.93.16.173:10010/home/login'
# 	method = 'post'
# 	data = {"name":"teacher","password":"123123"}
# 	header = {"Content-Length": "28",
# 	"Cookie": "PHPSESSID=m3dofibuj2ije3irj2mtrknfmd; laravel_session=miR3En3TzXG2V3s8MhYTSMGyodyAXB5bs1rAPTwP; io=1pAVHUXSJGxHVKGyAAid",
# 	"Host": "47.93.16.173:10010",
# 	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
# 	print(run.run_main(method,url,data,header))

