from rest_framework import serializers
from services.models import Services
from category.models import Category
from sub_category.models import Sub_category



class Get_detailsSerializer(serializers.ModelSerializer):
    class Meta:

        # model = Friends
        # fields = ('vz_id','friends_vz_id',)
        # model = Register
        # fields = ('',)
        

    	model = Category
    	fields = ('category','description')
        
        # model = Ticket
        # fields = ('user_details','question', 'item', 'description','date_created','date_validity','ticket_id','vz_id')
        
 

