#coding:utf-8
import smtplib
from email.mime.text import MIMEText
class SendEmail:
	global send_user
	global send_host
	global password
	password = "wssnlvvqiutpbfih"
	send_user = "837512134@qq.com"
	send_host = "smtp.qq.com"
	def send_email(self,user_list,sub,content):
		user = "837512134"+"<"+send_user+">"
		message = MIMEText(content,_subtype='plain',_charset='utf-8')
		message['Subject'] = sub
		message['From'] = user
		message['To'] = ";".join(user_list)
		server = smtplib.SMTP()
		server.connect(send_host)
		server.login(send_user,password)
		server.sendmail(user,user_list,message.as_string())
		server.close()

	def send_content(self,pass_list,fail_list):
		pass_num = float(len(pass_list))
		fail_num = float(len(fail_list))
		count_num = pass_num+fail_num
		pass_result = "%.2f%%" %(pass_num/count_num*100)
		fail_result = "%.2f%%" %(fail_num/count_num*100)
		user_list = ['meizile@huatangjt.com']
		sub = "这个是测试邮件"
		content = "此次一共运行接口个数为%s个,通过个数为%s个,失败个数为%s个,通过率为%s个,失败率为%s个" %(count_num,pass_num,fail_num,pass_result,fail_result)
		self.send_email(user_list,sub,content)
# if __name__ == '__main__':
# 	sen = SendEmail()
	# sen.send_content([1,2,3,4],[3,4,5,6,7,6])