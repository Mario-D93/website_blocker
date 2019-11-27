import time
from datetime import datetime as dt

#path to the hosts file on my ubuntu os
host_path = '/etc/hosts'

#websites I'd like to block
websites=['www.facebook.com']
redirect='172.0.0.1'

while True:

	#work hours set between 6am - 15pm
	if dt(dt.now().year,dt.now().month,dt.now().day,6) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,15):
		#print('Working hours')
		
		with open(host_path,'r+') as file:
			content = file.read()
			for site in websites:
				if site in content:
					pass
				else:
					file.write(redirect + '  ' + site + '\n')

	else:
		#print('Free time')
		
		with open(host_path,'r+') as file:
			content = file.readlines()
			file.seek(0)
			
			for line in content:
				if not any(web in line for web in websites):
					file.write(line)
			file.truncate()
	
	#program will be executed in 10s intervals
	time.sleep(10)