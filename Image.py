import requests
import time
import os
import aiohttp
import asyncio


class Image:
    """
    класс картинки
    """
    __slots__ = ('url', 'filename')

    def __init__(self, url):
        self.url = url
        self.filename = url.split("/")[-1]

    def download(self):
        start_time = time.time()

        response = requests.get(self.url)

        if response.status_code != 200:
            return f"Ошибка запроса {self.url}: Статус код {response.status_code}"

        if not os.path.exists('downloads'):
            os.makedirs('downloads')

        with open(os.path.join('downloads', self.filename), 'wb') as image:
            image.write(response.content)

        return f"время скачивания изображения {self.url} - {time.time() - start_time}"

    async def async_download(self):
        loop = asyncio.get_event_loop()
        start_time = loop.time()

        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                response.raise_for_status()
                image_data = await response.read()

                if not os.path.exists('downloads'):
                    os.makedirs('downloads')

                with open(os.path.join('downloads', self.filename), 'wb') as image:
                    image.write(image_data)

        end_time = loop.time()

        return f"время скачивания изображения {self.url} - {end_time - start_time}"

    def __str__(self):
        return f"изображение - {self.url}"
