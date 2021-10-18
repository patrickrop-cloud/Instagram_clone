from django.test import TestCase

from instagram.views import profile
from .models import Image, Profile

# Create your tests here.
class ImageTestclass(TestCase):
    #setup method
    def setUp(self):
        self.myimage=Image(image='image',name='Patrick',caption='Nice',comments='nice pic')

     #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.myimage,Image))
    
    #save method
    def test_save_images(self):
        self.myimage.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    
    def test_update_caption(self):
        new_caption=Image.update_caption()
        expected_caption=f'{new_caption}'
        self.assertTrue(expected_caption,'new_image')

    #delete method
    def test_delete_images(self):
        self.myimage.save_image()
        images_record=Image.objects.all()
        self.myimage.delete_image()
        self.assertTrue(len(images_record)==0)

class ProfileTestclass(TestCase):
    #setUp method
    def setUp(self):
        self.profile=Profile(profile_pic='image',bio='Software developer')

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    #Save method
    def test_save_profile(self):
        self.profile.save_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>0)

    #Delete method
    def test_delete_profile(self):
        self.profile.save_profile()
        profile_record = Profile.objects.all()
        self.profile.delete_profile()
        self.assertTrue(len(profile_record)==0)



    