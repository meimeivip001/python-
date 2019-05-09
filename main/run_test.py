#coding:utf-8
import time
import sys
import json
sys.path.append("D:/www/imooc")
from base.run_methon import RunMethod
from data.get_data import GetData
from util.equeal_util import equeal
from util.send_email import SendEmail
class RunTest:
	
	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()
		self.equeal = equeal()
		self.sendmail = SendEmail()
	#程序执行
	def go_on_run(self):
		pass_list = []
		fail_list = []
		res = None
		rows_count = self.data.get_case_lines()
		for i in range(1,rows_count):
			url = self.data.get_url(i)
			method = self.data.get_request_methon(i)
			is_run = self.data.get_is_run(i)
			data = self.data.get_data_for_json(i)
			headers = self.data.get_header_json(i)
			expect = self.data.get_except_data(i)
			print(expect)
			if is_run:
				res = self.run_method.run_main(method,url,data,headers)
				if self.equeal.is_contain(expect,res):
					self.data.write_result(i,'pass')
					pass_list.append(i)
				else:
					print("测试失败")
					self.data.write_result(i,res)
					fail_list.append(i)
		self.sendmail.send_content(pass_list,fail_list)
if __name__ == '__main__':
	run = RunTest()
	run.go_on_run()


