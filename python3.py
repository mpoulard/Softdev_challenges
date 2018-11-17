#!/usr/bin/python2.7

import copy
import sys

#Read 7 files, return list of 7 strings
def read_files():
	my_blocks = []
	for i in range(7):
		my_file = open(sys.argv[i+1]).read(9)
		my_blocks.append(my_file)

	return my_blocks
 		
###

#Sort blocks by size (to optimize, unsed for the moment)
def sort_by_size(my_blocks):
	
	my_new_blocks = []
	double_new_blocks = []
	
	for i in range(7):
		double_new_blocks.append((block_size(my_blocks[i]),my_blocks[i]))
	
	double_new_blocks.sort(reverse = True)
	
	for i in range(7):
		my_new_blocks.append(double_new_blocks[i][1])

	return my_new_blocks

#Give size of the block
def block_size(block):
	counter = 0
	for i in range(len(block)):
		if block[i] != ' ' and block[i] != '\n':
			counter +=1
	return counter 

###

#Create matrice
def draw_matrix():
	#size 5*5?
	return [[ 0 for i in range(5) ] for i in range(5) ]

#Print the matrice with good format
def print_matrix(matrix):
	printed_matrix = ''
	for i in range(5):
		for j in range(5):
			printed_matrix = printed_matrix + str(matrix[i][j]) 
		if (i != 4):
			printed_matrix = printed_matrix + '\n'
		else: printed_matrix = printed_matrix
	return printed_matrix

#Removing the non used values of counter_loop and store_loop
def clear_list(counter_loop, index):
	for i in range(len(counter_loop)):
		if i > index:
			counter_loop[i] = 0
	return counter_loop


def clear_store(store_loop, index):
	for i in range(len(store_loop)):
		if i > index:
			store_loop[i] = []
	return store_loop

#Return True if an element e is in a list l
def el_in_list(e,l):
	for i in range(len(l)):
		if l[i] == e:
			return True
	return False 

#Find a non empty place for putting an element
def find_untaken_place(matrix):
	for i in range(5):
		for j in range(5):
			if (matrix[i][j] == 0):
				return [i,j]
	return 'no_place_avail'


#Put an element on a place
def put_element_on_place(element,matrix,posi):
	matrix[posi[0]][posi[1]] =  element
	return matrix

#Return the element of the block
def find_element_of_block(block):
	for char in block:
		if ( char != ' ') and ( char != '\n'):
			return char
	return 'no_good_block_format'
			
#Return True if an element is inserable
def check_element_inser(new_posi, matrix):
	if (new_posi[0] in range(5)) and (new_posi[1] in range(5)) and (matrix[new_posi[0]][new_posi[1]] == 0):
		return True
	else: return False

#Remove all the elements 'element' in matrice
def delete_element_from_matrix(matrix, element):
	for i in range(5):
		for j in range(5):
			if (matrix[i][j] == element):
				matrix[i][j] = 0
	return matrix

###

#Put a block in the matrice if possible (True, changed matrice) or (False, unchanged matrice)	
def put_block_from_posi(block,matrix,posi):
	
	new_posi = copy.copy(posi)
	new_block = copy.copy(block)
	#if the beggining of the block is a ' '
	if new_block[0] == ' ':
				posi[1] = posi[1] - 1
				new_posi[1] = new_posi[1] - 1
				if new_block[1] == ' ':
					posi[1] = posi[1] - 1
					new_posi[1] = new_posi[1] - 1
		


	
	for i in range(len(new_block)):


		if (new_block[i] == ' '):
			# decaler a droite
			new_posi[1] += 1
			
		elif new_block[i] == '\n': 
			#decaler en bas
			#revenir a la colone du debut
			new_posi[1] = posi[1]
			new_posi[0] += 1
		else: 
		#check if element inserable
		#put element
		#decaler a droite
			if check_element_inser(new_posi, matrix) == True :
				matrix = put_element_on_place(new_block[i],matrix,new_posi)
				new_posi[1] += 1
			else : 	
			#no insertion possible
				return False,delete_element_from_matrix(matrix, new_block[i])

         	
	return True,matrix


#Put a block in the whole matrice if possible (True, changed matrice) or (False, unchanged matrice)
def put_block_on_matrix(block, matrix):
	for i in range(5):
		for j in range(5):
			posi = [i,j]
			Flag,matrix = put_block_from_posi(block,matrix,posi)
			if (Flag == True): 
				return (Flag,matrix)
	return (Flag,matrix)

#Fill the matrix
#For each postion in added_block_list, I store the blocks that have been tried in store_loop, I store their quantity in counter_loop
def fill_matrix(matrix, my_blocks):

	added_block_list = []
	rest_block_list = copy.copy(my_blocks)
	counter_loop = [ 0 for i in range(7) ]
	store_loop = [[] for i in range(7)]
	
	i = 0

	while (find_untaken_place(matrix) != 'no_place_avail') :
		
		
		#If, for the position len(added_block_list), we ve already tried to put all the blocks, we won't repeat the try

		if ( counter_loop[len(added_block_list)] == (7 - len(added_block_list)) ):
				#print('CCCCCCCCCCCCCCCCCCCCCCCC')

				matrix = delete_element_from_matrix(matrix, find_element_of_block(added_block_list[-1]))
				rest_block_list.append(added_block_list[-1])
				del added_block_list[-1]

				store_loop[len(added_block_list)].append(rest_block_list[-1])
				clear_store(store_loop, (len(added_block_list)))

				counter_loop[len(added_block_list) ] += 1
				clear_list(counter_loop, (len(added_block_list)))
				
				

				#p
				#print(print_matrix(matrix))
				#print(rest_block_list)
				#print(added_block_list)

		

		else: 
			
			#If, for the position len(added_block_list), we ve already tried to put the block rest_block_list[0], we won't repeat the try
			if el_in_list(rest_block_list[0],store_loop[len(added_block_list)]) == True:
				rest_block_list.append(rest_block_list[0])
				del rest_block_list[0]
				continue
					

			Flag,matrix = put_block_on_matrix(rest_block_list[0], matrix)
			

			#If I can put the block, I add it
			if (Flag == True):
				added_block_list.append(rest_block_list[0]) 
				del rest_block_list[0]
				#p
				#print('a')
				#print(print_matrix(matrix))
				#print(rest_block_list)
				#print(added_block_list)

			else:	
				#If I cannot put the block, I remove the last one.
				#print('b')
				matrix = delete_element_from_matrix(matrix, find_element_of_block(added_block_list[-1]))
				rest_block_list.append(added_block_list[-1]) 
				del added_block_list[-1]

				store_loop[len(added_block_list)].append(rest_block_list[-1])
				clear_store(store_loop, (len(added_block_list)))

				counter_loop[len(added_block_list)] += 1
				clear_list(counter_loop, (len(added_block_list)))

				#p
				#print(print_matrix(matrix))
				#print(rest_block_list)
				#print(added_block_list)
				
		#print 
		#print
		#i += 1
		#print(i,'#####################################')
		
	return matrix





######################################

my_blocks = read_files()
#k = sort_by_size(my_blocks)  #if we want to optimize the algorithm
matrix = draw_matrix()
matrix = fill_matrix(matrix, my_blocks)
print(print_matrix(matrix))

