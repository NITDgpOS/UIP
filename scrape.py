from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen
from urllib.request import urlretrieve
import os
def make_soup(url):
    req = request.Request(url=url,headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    response = request.urlopen(req)
    html=response.read()
    #print (html)

    return BeautifulSoup(html)

def get_images(url):
    soup = make_soup(url)
    #this makes a list of bs4 element tags

    thumbnails = soup.find_all("a",class_="thumbnail",href=True)
    image_links=[]
    if not thumbnails:
        print('No matching image found')
        return
    for link in thumbnails:
        if link['href'].endswith(('jpg','png','jpeg')):
            image_links.append( link['href'])
    print(image_links)
    for image in image_links:
        #filename.append(image.split('/')[-1])
        path=os.getcwd()+'/pics'
        print (path)
        urlretrieve(image,os.path.join(path,image.split('/')[-1]))
    

try:    
    get_images("https://www.reddit.com/r/wallpapers");
except ValueError as e: 
    print("File could not be retrieved.", e)
else:
    print("It worked!")