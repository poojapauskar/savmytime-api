from rest_framework import serializers
from user_data.models import User_data


class User_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_data
        fields = ('id', 'name', 'phone', 'email','city','service','category','sub_category')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """

        # sid = 'bitjini'
        # token = '85dbbbc18dfaf078290eeee3c185ac6dfd8a208f'

        # def send_message(sid, token, sms_from, sms_to, sms_body):
        #     return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
        #     auth=(sid, token),
        #     data={
        #         'From': sms_from,
        #         'To': sms_to,
        #         'Body': sms_body
        #     })


        # #if __name__ == '__main__':
        # # 'From' doesn't matter; For transactional, this will be replaced with your SenderId;
        # # For promotional, this will be ignored by the SMS gateway
        # # Incase you are wondering who Dr. Rajasekhar is http://en.wikipedia.org/wiki/Dr._Rajasekhar_(actor)
        # r = send_message(sid, token,
        #     sms_from='09243422233',  # sms_from='8808891988',
        #     sms_to=validated_data.get('phone'), # sms_to='9052161119',
        #     sms_body='SAVMYTIME Service Request: '+validated_data.get('name')+' has requested a service from SAVMYTIME. The email address provided is '+validated_data.get('email')+' and the mobile number is '+validated_data.get('phone')+'.')
        # print r.status_code
        # pprint(r.json())


        return User_data.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.city = validated_data.get('city', instance.city)
        instance.service = validated_data.get('service', instance.service)
        instance.category = validated_data.get('category', instance.category)
        instance.sub_category = validated_data.get('sub_category', instance.sub_category)
        instance.save()
        return instance