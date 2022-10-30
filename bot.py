import pywhatkit
import time

group_id = 'you group ID' #if you want group message
# or 
#mob = '+380967258867' #if you want private message

mes = 'you message text'

def send_message():

	mobile = group_id 
	# mobile = mob
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


	minute_a = minute+3

	pywhatkit.sendwhatmsg_to_group(group_id=mobile, message=message, time_hour=hour, time_min=minute_a)
	# pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message, time_hour=hour, time_min=minute_a)
	

starttime=time.time()

def main():
	send_message()
	time.sleep(20)

while True:
	main()

if __name__ == '__main__':
	main()


