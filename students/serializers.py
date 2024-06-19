from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.ModelSerializer):

#     # reviews = serializers.SerializerMethodField(method_name='get_reviews',read_only = True)
#     # def get_reviews(self,obj):
#     #     reviews = obj.reviews.all()
#     #     serializer = ReviewSerializer(reviews , many=True)
#     #     return serializer.data

#     class Meta:
#         model = Student
#         fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

