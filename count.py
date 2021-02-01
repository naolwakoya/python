def countsort(list):
	list1 = [0,0,0,0,0,0]
	list2 =  [list[0]]
	final_List = []
	#part1
	for value in list:
		if value == 'A' or value == 0:
			list1[0] += 1
		elif value == 'B'  or value  == 1:
			list1[1] += 1 
		elif value == 'C' or value == 2:
			list1 [2] += 1
		elif value == 'D' or value == 3:
			list1[3] += 1
		elif value =='E' or value == 4:
			list1[4] +=1
		elif value == 'F' or value == 5:
			list1[5] +=1
	#part2		
	for value1 in list:
		for value2 in range(0,len(list)):
			if list2[value2]==value1:
				break
			elif value2 == len(list2)-1 and not list2[value2] == value1:
				list2.append(value1)
	
	list2.sort()
	#part3		
	j = 0
	k = 0
	for i in range (0,len(list1)):
		while (list1[i] > 0):
			final_List.append(list2[j])
			list1[i] -= 1
			k += 1
		if k>0:
			j += 1
		
		k = 0
	
	return final_List