from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import LongtoShort

def hello_world(request):
	return HttpResponse("Hello world!")


def home_page(request):
	context = {
		"submitted": False
		"error":False
	}

	if request.method == 'POST':
		context["submitted"] = True

		data = request.POST 				# dict
		long_url = data['longurl']
		custom_name = data['custom_name']

		print(long_url)
		print(custom_name)
		
		try:
			obj = LongtoShort(long_url=long_url,short_url = custom_name)
		    obj.save()

			date = obj.date
			clicks=obj.clicks

			context["long_url"] = long_url
			context["short_url"] = request.build_absolute_uri() + custom_name
			context["date"] = date
			context["clicks"] = clicks
			context["submitted"]=True
		
		except:
			context["error"]=True

	else:
		print("User not sending anything")

def redirect_url(request,short_url):
	row=LongtoShort.objects.filter(short_url = short_url)

	if len(row)==0:
		return HttpResponse("no such url exist")

	obj=row[0]
	long_url = obj.long_url
	obj.clicks=obj.clicks+1
	obj.save()


	return redirect(long_url)

def all_analytics(request):
	rows = LongtoShort.objects.all()

	context={
	       "rows": rows

	}
	return render(request,"all-analytics.html", context)




	return render(request, "index.html", context)




