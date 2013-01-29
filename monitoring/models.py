from django.db import models
from django.utils import timezone
from datetime import datetime

class Sensor(models.Model):
	id_number = models.IntegerField()
	nickname = models.CharField(max_length=512)

	def __unicode__(self):
		return unicode(self.nickname)
	
class Data(models.Model):
	sensor = models.ForeignKey(Sensor)
	time = models.DateTimeField()
	temp = models.FloatField()
    
	def lastestData(self):
        	return self.data >= timezone.now() - datetime.timedelta(minutes=1)
	
	def __unicode__(self):
		return unicode('%s:%s:%f' % (self.sensor.nickname, self.time, self.temp))

