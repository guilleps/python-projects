import pandas as pd
import requests

if __name__ == '__main__':
    url = 'https://data.cityofchicago.org/resource/gzaz-isa6.json?$query=SELECT%0A%20%20%60person_id%60%2C%0A%20%20%60rd_no%60%2C%0A%20%20%60crash_date%60%2C%0A%20%20%60crash_location%60%2C%0A%20%20%60victim%60%2C%0A%20%20%60longitude%60%2C%0A%20%20%60latitude%60%2C%0A%20%20%60geocoded_column%60%2C%0A%20%20%60%3A%40computed_region_vrxf_vc4k%60%2C%0A%20%20%60%3A%40computed_region_6mkv_f3dw%60%2C%0A%20%20%60%3A%40computed_region_bdys_3d7i%60%2C%0A%20%20%60%3A%40computed_region_43wa_7qmu%60%2C%0A%20%20%60%3A%40computed_region_rpca_8um6%60%0AORDER%20BY%20%60crash_date%60%20DESC%20NULL%20FIRST'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data_endpoint = response.json()  # Convierte la respuesta JSON en un diccionario de Python
        data_fatalities = pd.DataFrame(data_endpoint)
        # print(data_fatalities.head())
        # print(data_fatalities.describe())
        # print(data_fatalities.info())
        # print(data_fatalities.isnull())
        # print(data_fatalities.duplicated())
        
        columnas_a_eliminar = [':@computed_region_bdys_3d7i', ':@computed_region_43wa_7qmu', ':@computed_region_rpca_8um6',
                               ':@computed_region_vrxf_vc4k', ':@computed_region_6mkv_f3dw', 'geocoded_column',
                               'person_id', 'rd_no']
        data_fatalities.drop(columns=columnas_a_eliminar, inplace=True)
        print(data_fatalities)

        
        data_fatalities['latitude'] = pd.to_numeric(data_fatalities['latitude'], errors='coerce')
        data_fatalities['longitude'] = pd.to_numeric(data_fatalities['longitude'], errors='coerce')

        data_fatalities['victim'] = data_fatalities['victim'].astype('string')
        data_fatalities['crash_location'] = data_fatalities['crash_location'].astype('string')

        data_fatalities['latitude'] = data_fatalities['latitude'].round(4)
        data_fatalities['longitude'] = data_fatalities['longitude'].round(4)

        data_fatalities['crash_date'] = pd.to_datetime(data_fatalities['crash_date'])

        data_fatalities['crash_date'] = data_fatalities['crash_date'].dt.strftime('%Y-%m-%d')


        # print(data_fatalities.info())
        print(data_fatalities.head())


