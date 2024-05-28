import argparse
from Image import Image
import asyncio
import time

URL_LIST = [
    'https://legendvalley.net/wp-content/uploads/2021/03/Slots-Reload-Bonuses-Explained.jpg',
    'https://moidachi.ru/wp-content/uploads/2021/12/sa2-4.jpg',
    'https://mir-s3-cdn-cf.behance.net/project_modules/1400_opt_1/433d4747359645.5877cb1da3dfa.jpg',
    'https://krovlyakryshi.ru/wp-content/uploads/sa-445.jpg',
    ]

images = [Image(url) for url in URL_LIST]


async def download(img_list):
    tasks = [asyncio.create_task(img.async_download()) for img in img_list]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


if __name__ == '__main__':
    # start_time = time.time()
    # asyncio.run(main())
    # print(f"суммарное время на выполнение - {time.time() - start_time}")

    parser = argparse.ArgumentParser(description="Скачать картинки по указанным URL")
    parser.add_argument('urls', nargs='*', help="Список URL-адресов картинок для скачивания")
    args = parser.parse_args()
    asyncio.run(download(Image(url) for url in args.urls))
