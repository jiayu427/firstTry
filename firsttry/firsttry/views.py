from django.http import HttpResponse
from datetime import datetime
from firsttry.models import Counter
from django.db.models import F
from django.shortcuts import render

def index(request):
	try:
		c = Counter.objects.get(pk=1)
	except:
		c = Counter(number=0)
		c.save()
		pass
			
	c = Counter.objects.filter(pk=1)
	c.update(number=F('number')+1)
	c = Counter.objects.get(pk=1)
	return render(request, 'index.html', {
	   'number': c.number,
	   'time' : str(datetime.now())})

