from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import revenue
import json
from django.core.serializers.json import DjangoJSONEncoder

def home(request):

	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request,('Item has been added to the list!'))
			return render(request,'home.html',{'all_items': all_items})			

	else:		
		all_items = List.objects.all
		return render(request,'home.html',{'all_items': all_items})	

def about(request):
	context = {'name': 'Snigdha'}
	return render(request,'about.html',context)

def delete(request,list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request,('Item has been deleted!'))
	return redirect('home')

def cross_off(request,list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home')

def uncross(request,list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home')

def dash(request):
	# Region = revenue.objects.all().values_list('Region')
	# Region = revenue.objects.all().values_list('Region')
	# print(Region)
	# context = {"Region":Region}
	c = revenue.objects.all().values()
	print("******************************  c is ****************************************")
	print(c)
	#context = json.dumps(list(c), cls=DjangoJSONEncoder)
	context = c[0]
	print("****************************** context is ****************************************")
	print(context)
	return render(request, 'dashboard.html', context)




