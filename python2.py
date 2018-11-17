#!/usr/bin/python2

import socket
import pickle
import datetime
import time


host = 'localhost'
port = 9999



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

time.sleep(0.5)

print(s.recv(1000))




############################################
s.send(("Ma\n"))
print("Ma\n")
print(s.recv(1000))

#############################################
s.send(("fe05150671053875b5aaf6a7a795c2df\n"))
print("fe05150671053875b5aaf6a7a795c2df\n")
print(s.recv(1000))

############################################
number = 5000
high_number = 10000
low_number = 0
b = True

while (b == True):
	
	number = (high_number + low_number) / 2

	s.send(str(number) + "\n")
	result_guess_number = s.recv(1000)
	list_result_guess_number = result_guess_number.split()

	if list_result_guess_number[0] != "nope.":
		b = False
	elif list_result_guess_number[3] == "bigger":
		low_number = number 
	elif list_result_guess_number[3] == "smaller":
		high_number = number	
		 
	

print(str(number) + "\n")
#print list_result_guess_number

############################################

#[' ##### ', '#     #', '      #', ' ##### ', '      #', '#     #', ' ##### '] 3
#['#      ', '#    # ', '#    # ', '#######', '     # ', '     # ', '     # '] 4
#['   #   ', '  ##   ', ' # #   ', '   #   ', '   #   ', '   #   ', ' ##### '] 1
#[' ##### ', '#     #', '#      ', '###### ', '#     #', '#     #', ' ##### '] 6
#['#######', '#      ', '#      ', ' ##### ', '      #', '#     #', ' ##### '] 5
#['#######', '#    # ', '    #  ', '   #   ', '  #    ', '  #    ', '  #    '] 7
#[' ##### ', '#     #', '#     #', ' ######', '      #', '#     #', ' ##### '] 9
#[' ##### ', '#     #', '      #', ' ##### ', '#      ', '#      ', '#######'] 2
#[' ##### ', '#     #', '#     #', ' ##### ', '#     #', '#     #', ' ##### '] 8
#['  ###  ', ' #   # ', '# #   #', '#  #  #', '#   # #', ' #   # ', '  ###  '] 0



result_dies_number  = s.recv(1000)
print(result_dies_number)

list_lines = result_dies_number.split("\n")[:-3]
#print list_lines 
#print '\n'

list_num_1 = []
list_num_2 = []
list_num_3 = []

for i in range(len(list_lines)):

	if len(list_lines[i]) != 39:
		diff = 39 - len(list_lines[i])
		for m in range(diff):
			list_lines[i] = list_lines[i] + ' '

	
	list_num_1.append(list_lines[i][0:7])
	list_num_2.append(list_lines[i][16:23])
	list_num_3.append(list_lines[i][32:39])


dictionary = dict()

dictionary = {"[' ##### ', '#     #', '      #', ' ##### ', '      #', '#     #', ' ##### ']": '3', "['#      ', '#    # ', '#    # ', '#######', '     # ', '     # ', '     # ']": '4', "['   #   ', '  ##   ', ' # #   ', '   #   ', '   #   ', '   #   ', ' ##### ']": '1', "[' ##### ', '#     #', '#      ', '###### ', '#     #', '#     #', ' ##### ']": '6', "['#######', '#      ', '#      ', ' ##### ', '      #', '#     #', ' ##### ']": '5', "['#######', '#    # ', '    #  ', '   #   ', '  #    ', '  #    ', '  #    ']": '7', "[' ##### ', '#     #', '#     #', ' ######', '      #', '#     #', ' ##### ']": '9', "[' ##### ', '#     #', '      #', ' ##### ', '#      ', '#      ', '#######']": '2', "[' ##### ', '#     #', '#     #', ' ##### ', '#     #', '#     #', ' ##### ']": '8', "['  ###  ', ' #   # ', '# #   #', '#  #  #', '#   # #', ' #   # ', '  ###  ']": '0'}

resultat = dictionary[str(list_num_1)] + dictionary[str(list_num_2)] + dictionary[str(list_num_3)]
print(resultat)
s.send( resultat + "\n" )
print(s.recv(1000))


############################################

pic_result = s.recv(1000)
print(pic_result)
list_pic_result = pic_result.split('\n')

pic_time = ''
for i in range(7):
	pic_time = pic_time + list_pic_result[(i + 1)] + '\n'

pic_time = pic_time + list_pic_result[8]

#print pic_time


atime = pickle.loads(pic_time)
microsec = atime.microsecond
print(microsec)


s.send( str(microsec) + '\n')

print(s.recv(1000))

############################################
write_mes = s.recv(1000)
print(write_mes)
list_write_mes = write_mes.split()



months = ['zero','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 


write_date = datetime.date( int('20' + list_write_mes[7][:-1]), months.index(list_write_mes[6]), int(list_write_mes[5])).weekday()


day = days[int(write_date)]

print(day)
s.send( str(day) + '\n')


############################################

time.sleep(0.5)
final_result = s.recv(500)



s.close()

print(final_result)

final_secret = final_result.split("\n")[2]

print('\n')

print(final_secret)


