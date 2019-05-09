#coding:utf-8
import json
class op_header_json:
	def read_header(self):
		with open('../dataconfig/headers.json') as fp:
			data = json.load(fp)
			return data
	def get_header_value(self,id):
		header_data = self.read_header()
		if id !=None:
			return header_data[id]
		else:
			return None
# if __name__ == '__main__':
# 	op = op_header_json()
# 	print(op.get_header_value(login))