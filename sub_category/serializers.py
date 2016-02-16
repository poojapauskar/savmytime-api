from rest_framework import serializers
from sub_category.models import Sub_category


class Sub_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_category
        fields = ('id', 'sub_category', 'category_id','price','description','payment')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        # return Sub_category.objects.create(**validated_data)

        # Sub_category.objects.filter(id=47)52 57 58 59 65 72 73 78 89 90 91 92 93 94 95 102 103 104 105 106 107 108 109 110 111 145 146 147 148 149 150 151 152 153 154 155 262 268 269 270 271 272 273 274 275 276 278 288 289 290 291 292 300 301 302 303 304 305 312.update(payment=0)
        # Sub_category.objects.filter(id=47).filter(id=52).filter(id=57).filter(id=58).filter(id=59).filter(id=65).filter(id=72).filter(id=73).filter(id=78).filter(id=89).filter(id=90).filter(id=91).filter(id=92).filter(id=93).filter(id=94).filter(id=95).filter(id=102).filter(id=103).filter(id=104).filter(id=105).filter(id=106).filter(id=107).filter(id=108).filter(id=109).filter(id=110).filter(id=111).update(payment="0")
        # Sub_category.objects.filter(id=145).filter(id=146).filter(id=147).filter(id=148).filter(id=149).filter(id=150).filter(id=151).filter(id=152).filter(id=153).filter(id=154).filter(id=155).filter(id=262).filter(id=268).filter(id=269).filter(id=270).filter(id=271).filter(id=272).filter(id=273).filter(id=274).filter(id=275).filter(id=276).filter(id=277).filter(id=278).filter(id=288).filter(id=289).filter(id=290).update(payment="0")
        # Sub_category.objects.filter(id=291).filter(id=292).filter(id=300).filter(id=301).filter(id=302).filter(id=303).filter(id=304).filter(id=305).filter(id=312).update(payment=0)

        # Sub_category.objects.all().update(payment="0")

        return Sub_category.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.sub_category = validated_data.get('sub_category', instance.sub_category)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance