from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.Serializer):
    names= serializers.CharField()
    email= serializers.EmailField()
    address= serializers.CharField()
    phone= serializers.CharField()
    age= serializers.CharField()

    def validate(self,attrs):
        names= attrs.get('names')
        email= attrs.get('email')
        # address= attrs.get('address')
        # phone= attrs.get('phone')
        # age= attrs.get('age')

        errors = {}

        # Validate name
        if len(names) <= 4:
            # raise serializers.ValidationError("please name must not be less than 4 characters")
            errors['name'] = ["please name must not be less than 4 characters"]
       

        # Validate email (optional: add email format validation if needed)
        if not email:
            errors['email'] = ["Email is required"]

        
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
        
        return validated_data
    
    def update(self, instance, validated_data):
        #print(validated_data, "validated data")
        print(vars(instance), "instance __dict__") # only works for instances with a __dict__ attribute
        print(dir(instance), "instance dir()") # Lists all attributes and methods 


        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("name", instance.email)
        instance.address = validated_data.get("name", instance.address)
        instance.phone = validated_data.get("name", instance.phone)
        instance.age = validated_data.get("name", instance.age)
        instance.save()
        return instance