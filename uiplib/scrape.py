from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
import os
import sys
import json

def make_soup(url):
    '''
    makes soup, that is basically parsing the html document
    '''
    response = requests.get(url, headers = {'User-agent': 'UIP'})
    html = response.content
    return BeautifulSoup(html, "html.parser")

def make_json(url):
    response = requests.get(url + '/.json', headers = {'User-agent': 'UIP'})
    json_file = response.text
    data = json.loads(json_file)
    return data['data']


def dlProgress(count, blockSize, totalSize):
    '''
    Show Progress bar
    '''
    percent = int(count*blockSize*100/totalSize)/2
    sys.stdout.write("\r[%s%s]" % ('='*int(percent), ' '*(50-int(percent))))
    sys.stdout.flush()

def get_images(url, directory, count):
    '''
    scrape images from /r/wallpapers
    '''
    image_links = []
    no_of_images = int(count)
    page = make_json(url)
    for sub in page['children']:
        for image in sub['data']['preview']['images']:
            if(len(image_links)<no_of_images):
                image_links.append(image['source']['url'])

    for image in image_links:
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = image.split('/')[-1]
        filename = filename[: filename.find('?')]
        page = requests.get(image, stream = True)
        try:
            urlretrieve(image,
                        os.path.join(directory,filename),
                        reporthook = dlProgress)
        except Exception as e:
            print("Image cannot be downloaded: ",str(e))
