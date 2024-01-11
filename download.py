import os
import requests
from bs4 import BeautifulSoup

def download_fonts(urls, folder='fonts'):
    if not os.path.exists(folder):
        os.makedirs(folder)

    for url_info in urls:
        url_pagina = url_info['url']
        font_name = url_info['name']

        response = requests.get(url_pagina)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            font_description = soup.find('div', class_='font-description')
            comment = str(font_description).split("<!--")[1].split("-->")[0]
            url_fuente = "https://" + comment.split('url("//')[1].split('")')[0]
            font_type = comment.split('format("')[1].split('")')[0]

            response_fuente = requests.get(url_fuente)

            if response_fuente.status_code == 200:
                with open(os.path.join(folder, f'{font_name}.{font_type}'), 'wb') as f:
                    f.write(response_fuente.content)
                print(f'Fuente "{font_name}" descargada exitosamente.')
            else:
                print(f'Error al descargar la fuente "{font_name}". Código de estado: {response_fuente.status_code}')

        else:
            print(f'Error al hacer la petición para "{font_name}". Código de estado: {response.status_code}')
