from django.shortcuts import render
from django.http import HttpResponse
import task1
from django.urls import path
from django.http import JsonResponse

def index(request):
	return HttpResponse("hello, world.you're at the taskssss index.")
def adjs(request,n1,n2):
	ans=task1.adj(request,n1,n2)
	return HttpResponse(ans)

#	return render(request, 'task1.adj', n1,n2)
	#n1=int(input("enter starting number of range:"))
	#n2 =int(input("enter ending number of range:"))
#	n2=int(n2)
#	for i in range(n1,n2+1):
#		bin_num=bin(i).replace("0b","")
		#print(i,"is",bin_num)
#		for x in range(len(bin_num)-1):	
#			if bin_num[x] and bin_num[x+1]=="1":
#				q.update({i:"True"})
#			break;
#		if i not in q:
#			q.update({i:"False"})
#	return HttpResponse(q)
def add(request):
	#n1=int(request.GET["n1"])
	#n2=int(request.GET["n2"])
	return render(request, "trial/home.html")
def res(request):
	n1=int(request.POST["n1"])
	n2=int(request.POST["n2"])
	ans=n1+n2
	return render(request,"trial/result.html",{'ans':ans})	

