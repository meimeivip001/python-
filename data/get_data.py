#coding:utf-8
import sys
sys.path.append("D:/www/imooc")
from util.operation_excel import OperationExcel
import data.data_config
from util.operation_json import OperationJson
from util.operation_header import op_header_json
class GetData:
	def __init__(self):
		self.opera_excel = OperationExcel()
		self.opera_json = OperationJson()
		self.opera_header = op_header_json()
		self.data_config = data.data_config
		#self.data_config = self.data.data_config
	def get_case_lines(self):
		return self.opera_excel.get_lines()
	#获取是否执行
	def get_is_run(self,row):
		flag = None
		col = int(self.data_config.get_run())
		run_model = self.opera_excel.get_cell_value(row,col)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag
	#是否有header
	def is_header(self,row):
		col = int(self.data_config.get_header())
		header = self.opera_excel.get_cell_value(row,col)
		return header
	#根据获取到header值，获取json数据
	def get_header_json(self,row):
		header = self.is_header(row)
		if header != None:
			return self.opera_header.get_header_value(header)
		else:
			return None

	#获取请求方式
	def get_request_methon(self,row):
		col = int(self.data_config.get_run_way())
		request_method = self.opera_excel.get_cell_value(row,col)
		return request_method
	#获取url
	def get_url(self,row):
		col = int(self.data_config.get_url())
		url = self.opera_excel.get_cell_value(row,col)
		return url
	#获取请求数据
	def get_request_data(self,row):
		col = int(self.data_config.get_data())
		data = self.opera_excel.get_cell_value(row,col)
		if data != '':
			return data
		else:
			return None
	#通过关键字获取data数据
	def get_data_for_json(self,row):
		request_data = self.get_request_data(row)
		if request_data != None:
			data = self.opera_json.get_data(request_data)
		else:
			return None
		return data
	#获取预期结果
	def get_except_data(self,row):
		col = int(self.data_config.get_expect())
		request_data = self.opera_excel.get_cell_value(row,col)
		if request_data !='':
			return request_data
		else:
			return None
	def write_result(self,row,value):
		col = int(self.data_config.get_result())
		self.opera_excel.write_value(row,col,value)
# if __name__ == '__main__':
	# getdata=GetData()
	# print(getdata.get_header_json(1))
	# print(getdata.get_except_data(1))