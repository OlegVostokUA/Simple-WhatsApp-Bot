import pywhatkit
import time

group_id = 'JGQwzfeGh7z3sIIfYBk0JH' #https://chat.whatsapp.com/JGQwzfeGh7z3sIIfYBk0JH
mes = 'pft,e'

def send_message():

	mobile = group_id
	message = mes
	
	def generate_time():
		a = list(time.ctime())
		h = a[11:13]
		hv = str(''.join(h))
		b = a[14:16]
		c = str(''.join(b))
		c = int(c)
		if c >= 55:
			c = 5
		else:
			c = c
		return int (hv), int(c)+1

	hour, minute = generate_time()

	print(hour)
	print(minute)

	minute_a = minute+3

	pywhatkit.sendwhatmsg_to_group(group_id=mobile, message=message, time_hour=hour, time_min=minute_a)

starttime=time.time()

def main():
	send_message()
	time.sleep(20)

while True:
	main()

if __name__ == '__main__':
	main()

























'''
import pywhatkit

mobn = ['+380969413176', '+380937205205']
#mob = '+380967258867'
mes = 'test'




def send_message():
	for i in mobn:
		mob = i
	mobile = mob
	message = mes

	pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)

def main():
	send_message()


if __name__ == '__main__':
	main()

'''
