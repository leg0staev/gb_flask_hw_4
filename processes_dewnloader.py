from multiprocessing import Process
import argparse
from Image import Image

URL_LIST = [
    'https://legendvalley.net/wp-content/uploads/2021/03/Slots-Reload-Bonuses-Explained.jpg',
    'https://moidachi.ru/wp-content/uploads/2021/12/sa2-4.jpg',
    'https://mir-s3-cdn-cf.behance.net/project_modules/1400_opt_1/433d4747359645.5877cb1da3dfa.jpg',
    'https://krovlyakryshi.ru/wp-content/uploads/sa-445.jpg',
]

images = [Image(url) for url in URL_LIST]


def callback(string):
    print(string)


def download(image_list):
    processes = []
    for img in image_list:
        process = Process(target=lambda: callback(img.download()))
        processes.append(process)
        process.start()

    for p in processes:
        p.join()


if __name__ == '__main__':
    # download(images)

    parser = argparse.ArgumentParser(description="Скачать картинки по указанным URL")
    parser.add_argument('urls', nargs='*', help="Список URL-адресов картинок для скачивания")
    args = parser.parse_args()
    download(Image(url) for url in args.urls)
