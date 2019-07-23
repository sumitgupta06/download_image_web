#program to download an image from the we
'''random is required as the image downloaded needs to be given a random name
so that it wont clash with any image having similar names'''

import random
import urllib.request #package allows to get data from websites
#file>settings>project iterpreter>'+' allows to download different modules> search and install package


def download_image(url):
    name=random.randrange(1,1000) #randrange(i,j) selects a random no, from i to j
    fullname= str(name) + ".jpg" #str would convert no. to string
    urllib.request.urlretrieve(url, fullname) #urlretrieve retrieves the url from object passed
    #image retrieved is stored in the project directory

download_image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Vinnymarch2012c.jpg/220px-Vinnymarch2012c.jpg")
