from django.shortcuts import render_to_response
from monitoring.models import *

def index(request):
	sensor_list = Sensor.objects.all().order_by('-id_number')[:4]
	data_list_list = list()
	
	for sensor in sensor_list:
		data_list = Data.objects.filter(sensor__pk = sensor.pk).order_by('time')
		data_list_list.append(data_list)	

	return render_to_response('monitoring/index.html',{'sensor_list': sensor_list, 'data_list_list':data_list_list})
