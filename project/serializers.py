from rest_framework import serializers
from .models import Project, Review

# class ProjectSerializer(serializers.ModelSerializer):

#     reviews = serializers.SerializerMethodField(method_name='get_reviews',read_only = True)
#     def get_reviews(self,obj):
#         reviews = obj.reviews.all()
#         serializer = ReviewSerializer(reviews , many=True)
#         return serializer.data

#     class Meta:
#         model = Project
#         fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

        
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Review
        fields = "__all__"
