#coding:utf-8
import json
class OperationJson():
	def __init__(self):
		self.data = self.read_json()
	#读取json数据
	def read_json(self):
		with open('../dataconfig/login.json') as fp:
			data = json.load(fp)
			return data
	#根据关键字获取数据
	def get_data(self,id):
		if id != None:
			return self.data[id]
		else:
			return None
# if __name__ == '__main__':
# 	opjson = OperationJson()
	# print (type(opjson.get_data("login")))