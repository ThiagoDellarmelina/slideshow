from selenium import webdriver
from bs4 import BeautifulSoup
import time

# URL do álbum compartilhado no Google Fotos
album_url = "https://photos.app.goo.gl/3DJWVTYpptLo5e9b9"

# Configurar o driver do Chrome
driver = webdriver.Chrome()  # Certifique-se de que o ChromeDriver está no PATH

try:
    # Acessar o link do álbum
    driver.get(album_url)
    time.sleep(5)  # Aguarde para garantir que as imagens carreguem

    # Obter o HTML da página
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Procurar por URLs de imagens maiores
    image_urls = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and 'googleusercontent' in src and not 's32-p' in src:
            # Altere o parâmetro do tamanho para obter uma versão maior da imagem, se disponível
            high_res_src = src.replace('=s32-p', '=s1200')  # Exemplo para 1200px
            image_urls.append(high_res_src)

    # Exibir as URLs encontradas
    print("URLs das imagens encontradas:")
    for url in image_urls:
        print(url)

finally:
    driver.quit()  # Fechar o navegador
