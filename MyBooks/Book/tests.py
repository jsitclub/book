from django.test import TestCase

# Create your tests here.


from django.core.files import File
from urllib import request
import os

# class Item(models.Model):
#     image_file = models.ImageField(upload_to='images')
#     image_url = models.URLField()

# ...

# def get_remote_image(self):
#     if self.image_url and not self.image_file:
#         result = request.urlretrieve(self.image_url)
#         self.image_file.save(
#                 os.path.basename(self.image_url),
#                 File(open(result[0], 'rb'))
#                 )
#         self.save()
        
url="https://bookthumb-phinf.pstatic.net/cover/163/897/16389774.jpg?type=m140&udate=20200627" 
        
        
def get_remote_image():

    result = request.urlretrieve(url)
    print(result)
    # self.image_file.save(
    #         os.path.basename(url),
    #         File(open(result[0], 'rb'))
    #         )
    # self.save()
get_remote_image()