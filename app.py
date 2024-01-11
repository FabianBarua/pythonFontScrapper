from download import download_fonts
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url_page = 'https://www.linotype.com/es/5621276/internacional-familia.html'
folder_name="internacional"

urls = []
response = requests.get(url_page)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    div_list = soup.find('div', class_='list')

    if div_list:
        divs_inside_list = div_list.find_all('div', class_='itemline_details')  # Obtener todos los divs con la clase 'itemline_details'

        for div in divs_inside_list:
            # Extraer la URL y el nombre
            relative_url = div.find('h4').find('a')['href']
            full_url = urljoin(url_page, relative_url)
            name = div.find('h4').find('a').text.strip().replace(' ', '-')

            # Agregar el objeto a la lista
            urls.append({'url': full_url, 'name': name})

    else:
        print('No se encontró el div con la clase "list".')
else:
    print(f'Error al hacer la petición. Código de estado: {response.status_code}')

download_fonts(urls=urls, folder=folder_name)