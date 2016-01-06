from rest_framework import serializers
from upload_image.models import Upload_image
#from connect.models import Connect, LANGUAGE_CHOICES, STYLE_CHOICES

import random
from random import randint
import json


import cloudinary
import cloudinary.uploader
import cloudinary.api


cloudinary.config( 
  cloud_name = "htwoqvwuz", 
  api_key = "199369995891894", 
  api_secret = "186ob1Z_t3qOm5KfRHLrUwfkRmU" 
)



class Upload_imageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upload_image
        fields = ('photo','link')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        
        import sys
        link=''
       # image="image"+str(random.randint(100, 999))
        public_id='id'+str(random.randint(100000, 999999))

        

        if(bool(validated_data.get('photo')) == True):
         cloudinary.uploader.upload(validated_data.get('photo'),public_id ="savmytime/"+public_id)

        # if(bool(validated_data.get('photo')) == True):
        #  link="res.cloudinary.com/hffrh1pci/image/upload/vzcards/"+public_id+".pdf"

        if(bool(validated_data.get('photo')) == True):
         link=public_id+".jpg"

       

        
       
        #print >> sys.stderr, validated_data.get('photo')

        objects=Upload_image.objects.create(photo=link,link=link)
        # print >> sys.stderr, objects
        
        

        return objects




