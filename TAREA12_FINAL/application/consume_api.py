import requests

# ___________Red Light Camera Violations___________

if __name__ == '__main__':
    url = 'https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vision-Zero-Chicago-Traffic-Fatali/gzaz-isa6/data'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.content
        file = open('TAREA12_FINAL/data/Traffic_Fatalities.html', 'wb')
        file.write(content)
        file.close()



# _________________TrafficTracker_________________

if __name__ == '__main__':
    url = 'https://data.cityofchicago.org/resource/kf7e-cur8.json'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.content
        file = open('TAREA12_FINAL/data/Traffic_Tracker.json', 'wb')
        file.write(content)
        file.close()



    #     data = response.json()
    #     for item in data[:5]:
    #         print(item)
    # else:
    #     print("Error al obtener los datos. Código de estado:", response.status_code)



if __name__ == '__main__':
    url = 'https://data.cityofchicago.org/resource/7mgr-iety.json'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.content
        file = open('TAREA12_FINAL/data/Map_Red_Light_Camera_Locations.json', 'wb')
        file.write(content)
        file.close()
