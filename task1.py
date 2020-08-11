def adj (): 
	n1=int(input("enter starting number of range:"))
	n2 =int(input("enter ending number of range:"))
	dict={}
	for i in range(n1,n2+1):
		bin_num=bin(i).replace("0b","")
#		rem=0 lst=[]
#		while int(i)>1:
#			rem=i%2
#			i=i/2
#			a=int(rem)
#			lst.append(str(a))
#			c="".join(lst)
#			bin_num = c[::-1]
		print(i,"is",bin_num)	
		for x in range(len(bin_num)-1):
			if bin_num[x] and bin_num[x+1]=="1":
				dict.update({i:"True"})
			break;
		if i not in dict:
			dict.update({i:"False"})
	print(dict)
adj()	