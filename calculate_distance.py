import math
import datetime
from datetime import date

with open("gps.txt", "r") as f:
   data = f.read().split()
   lat1 = []
   lat1 = data[1]
   lat1 = data[1].replace('>','')
   lat1 = lat1.replace('lat="','')
   lat1 = lat1.replace('"','')
   lat1 = float(lat1)
   #print(lat1)
   long1 = []
   long1 = data[2].replace('>','')
   long1 = long1.replace('lon="','')
   long1 = long1.replace('"','')
   long1 = float(long1)
   #print (long1)
   # print(data)
   fmt = "%Y-%m-%dT%H:%M:%SZ"
   t1 = (data[4].replace('<time>','').replace('</time>',''))
   t2 = (data[17].replace('<time>','').replace('</time>',''))
   
   t1 =  datetime.datetime.strptime(t1,fmt)
   t2 = datetime.datetime.strptime(t2,fmt)
   t = (t2 - t1).total_seconds()
   # print (t)
   # ttb = t2 - t1
   # print (ttb)
   
   lat2 = []
   lat2 = data[14]
   lat2 = data[14].replace('>','')
   lat2 = lat2.replace('lat="','').replace('"','')
   lat2 = float(lat2)
   #print(lat2)
   long2 = []
   long2 = data[15].replace('>','')
   long2 = long2.replace('lon="','').replace('"','')
   long2 = float(long2)
   def degreesToRadians(degrees):
      return degrees * math.pi / 180
   def distanceInKmBetweenEarthCoordinates(lat1, long1, lat2, long2):
      earthRadiusKm = 6371
      dLat = degreesToRadians(lat2-lat1)
      dLon = degreesToRadians(long2-long1)
      lat1 = degreesToRadians(lat1)
      lat2 = degreesToRadians(lat2)
      a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
      c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
      return (earthRadiusKm * c *1000)
print(distanceInKmBetweenEarthCoordinates(lat1, long1, lat2, long2))
print(distanceInKmBetweenEarthCoordinates(lat1, long1, lat2, long2)/t)