from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Project

# Create your tests here.
# apis/tests.py

# class APITests(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.project = Project.objects.create(
#                                         name ="Django for APIs",
#                                         type ="Build web APIs with Python and Django",
#                                         user ="William S. Vincent",
#                                         isbn="9781735467221",
#                                         )
#     def test_api_listview(self):
#         response = self.client.get(reverse("project_list"))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Project.objects.count(), 1)
#         self.assertContains(response, self.book)