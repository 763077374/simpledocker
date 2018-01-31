import smtplib
sender = '763077374@qq.com'

passWord = '985528'
mail_host = 'smtp.qq.com'
s = smtplib.SMTP("smtp.qq.com", 465)
s.set_debuglevel(1)
s.login(sender,passWord)	
print("success")
