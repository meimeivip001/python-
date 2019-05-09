#coding:utf-8
class equeal:
	def is_contain(self,str_one,str_two):
		flag = None
		# if isinstance(str_one,str):
		# 	str_one = str_one.encode(str).decode('string_escape')
		if str_one in str_two:
			flag = True
		else:
			flag = False
		return flag
# if __name__ == '__main__':
# 	eq = equeal()
# 	str_one ='login'
# 	str_two = {1,2,3,"login":"测试通过"}
# 	print(eq.is_contain(str_one,str_two))
