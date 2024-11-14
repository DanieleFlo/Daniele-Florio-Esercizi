import requests as rq
import json
import matplotlib.pyplot as plt

# link_meteo = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,precipitation_probability,wind_speed_10m&forecast_days=1'
# link_pos = 'https://geocoding-api.open-meteo.com/v1/search?name=Berlin&count=1&language=it&format=json'

# Create un programma python che permette tramite le api
# https://open-meteo.com/en/docs (per le previsioni metereologiche) e
# (per l’ottenimento in automatico della propria
# langitudine e latitudine tramite l’indirizzo ip), di vedere le previsione
# metereologiche.
# L’utente potrà scegliere se visionarle dei prossimi 1, 3 o 7 giorni e se
# visionare oltre che le temperature anche la velocità del vento e le
# probabili precipitazioni.
    
class Meteo():
    def __init__(self):
        self.__link_meteo = 'https://api.open-meteo.com/v1/forecast?'
        self.__link_pos_1 = 'https://geocoding-api.open-meteo.com/v1/search?name='
        self.__link_pos_2 = '&count=1&language=it&format=json'
        
    def get_position(self, citta):
            if len(citta)>0:
                try:
                    link = self.__link_pos_1 + citta + self.__link_pos_2
                    res = rq.get(link)
                    
                    if res.status_code == 200:
                        data = res.json()
                        latitudine = str(data['results'][0]['latitude'])
                        longitudine = str(data['results'][0]['longitude'])
                        return latitudine, longitudine
                    else:
                        print('Errore nel recupero della posizione.')
                        return None
                except:
                    print('Errore imprevisto.')
                    return None
            print('Nome città non valida!')
            return None
    
    def get_previsioni(self, link):
        try:
            res = rq.get(link)
            
            if res.status_code == 200:
                all_data = res.json()
                data = all_data['hourly']
                time = data['time']
                temperature = data.get('temperature_2m')
                prec_prob = data.get('precipitation_probability')
                wind_s = data.get('wind_speed_10m')
                
                for i in range(len(time)):
                    print('Data: ', time[i], end='; ')
                    if temperature!=None:
                        print('Temperatura: ', temperature[i], end='; ')
                    if prec_prob!=None:
                        print('Probabilità di precipitazione: ', prec_prob[i], end='; ')
                    if wind_s!=None:
                        print('Velocità del vento: ', wind_s[i], end='; ')
                    print()
                
                day = [t[-8:-3] for t in time]
                plt.figure(figsize=(10,10))
                if temperature!=None:
                    plt.plot(day, temperature, label='Temperatura')
                if prec_prob!=None:
                    plt.plot(day, prec_prob, label='% prec')
                if wind_s!=None:
                    plt.plot(day, wind_s, label='Wind Speed')
                plt.legend()
                plt.show()
            else:
                print('Errore connessione!')
        except:
            print('Errore imprevisto!')
    
    def start(self):
        citta = input('Inserisci il nome della città: ').lower()
        periodo = ''
        while True:
            periodo = input('Di quanti giorni vuoi le previsioni (1,3, 7): ')
            if periodo in ['1','3','7']:
                break
            else:
                print('Inserimento periodo non valido!')
        nav_vento = input('Velocità del vento: (y/n): ')
        nav_prec = input('Percentuale di precipitazioni: (y/n): ')
        res_pos =  self.get_position(citta)
        if res_pos !=None:
            latitudine, longitudine = res_pos
            link_meteo_tot = self.__link_meteo+'latitude='+latitudine+'&longitude='+longitudine+'&hourly=temperature_2m'
            if nav_prec == 'y':
                link_meteo_tot +=',precipitation_probability'
            if nav_vento == 'y':
                link_meteo_tot +=',wind_speed_10m'
            link_meteo_tot +='&forecast_days='+periodo
            print('Link API:', link_meteo_tot)
            self.get_previsioni(link_meteo_tot)
        else:
            print('Errore nella determionazione della posizione!')


meteo = Meteo()
meteo.start()
    
    
        