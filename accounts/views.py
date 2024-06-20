from django.shortcuts import render, get_object_or_404 ,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.contrib.auth import authenticate , login

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from datetime import datetime, timedelta

from .serializers import SingUpSerializer, UserSerializer
from .forms import SignupForm ,UserForm ,ProfileForm
from .models import Profile

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username ,password=password)
            login(request,user)
            return redirect('/accounts/profile')        
    else:
        form = SignupForm()
    return render(request , 'registration/signup.html',{'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request , 'profile/profile.html',{'profile':profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,instance=profile)
        if userform.is_valid() and profile_form.is_valid():
            userform.save()
            myform = profile_form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('/accounts/profile')
    else:
        userform = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)


    return render(request , 'profile/profile_edit.html',{
        'userform' : userform ,
        'profileform' : profile_form,
    })



@api_view(["POST"])
def register(request):
    data = request.data
    user = SingUpSerializer(data=data)

    if user.is_valid():
        if not User.objects.filter(username=data["email"]).exists():
            user = User.objects.create(
                username=data["email"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                password=make_password(data["password"]),
            )
            return Response(
                {"details": "Your account registered successfully !"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"error": "This email already exists!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    else:
        return Response(user.errors)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserSerializer(request.user, many=False)
    return Response(user.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    data = request.data

    user.first_name = data["first_name"]
    user.username = data["email"]
    user.last_name = data["last_name"]
    user.email = data["email"]

    if data["password"] != "":
        user.password = make_password(data["password"])

    user.save()
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


def get_current_host(request):
    protocol = request.is_secure() and "https" or "http"
    host = request.get_host()
    return "{protocol}://{host}/".format(protocol=protocol, host=host)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_review(request, pk):
    user = request.user
    project = get_object_or_404(Project, id=pk)

    review = project.reviews.filter(user=user)

    if review.exists():
        review.delete()
        rating = project.reviews.aggregate(avg_ratings=Avg("rating"))
        if rating["avg_ratings"] is None:
            rating["avg_ratings"] = 0
            project.ratings = rating["avg_ratings"]
            project.save()
            return Response({"details": "Project review Deleted !!!"})
    else:
        return Response(
            {"error": "Review NOT found!!"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["POST"])
def forgot_password(request):
    data = request.data
    user = get_object_or_404(User, email=data["email"])
    token = get_random_string(40)
    expire_date = datetime.now() + timedelta(minutes=30)
    user.profile.reset_password_token = token
    user.profile.reset_password_expire = expire_date
    user.profile.save()
    host = get_current_host(request)

    # http://localhost:8000/ or {host}
    link = "http://localhost:8000/api/reset_password/{token}".format(token=token)
    body = "Your password reset link is : {link}".format(link=link)
    send_mail(
        "password reset from eProject", body, "eProject@gmail.com", [data["email"]]
    )
    return Response(
        {"details": "password reset sent to {email}".format(email=data["email"])}
    )


@api_view(["POST"])
def reset_password(request, token):
    data = request.data
    user = get_object_or_404(User, profile__reset_password_token=token)

    if user.profile.reset_password_expire.replace(tzinfo=None) < datetime.now():
        return Response(
            {"error": "Token is expired"}, status=status.HTTP_400_BAD_REQUEST
        )

    if data["password"] != data["confirmPassword"]:
        return Response(
            {"error": "password are not same"}, status=status.HTTP_400_BAD_REQUEST
        )

    user.password = make_password(data["password"])
    user.profile.reset_password_token = ""
    user.profile.reset_password_expire = None
    user.profile.save()
    user.save()

    return Response({"details": "password reset done"})
