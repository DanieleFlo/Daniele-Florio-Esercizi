import requests as rq
import json
import matplotlib.pyplot as plt

link = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,precipitation_probability,wind_speed_10m&timezone=auto'
res = rq.get(link)

if res.status_code == 200:
    data = res.json()
    print(data)
    
# Oppure

data = res.text
data = json.loads(data)
x = list(data['hourly']['temperature_2m'])[:10]
y = list(data['hourly']['time'])[:10]

plt.figure(figsize=(10,10))
plt.plot(y,x)
plt.show()