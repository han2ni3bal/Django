from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from users.models import UserProfile, Article
from django.contrib import auth
from .forms import RegistrationFrom,LoginForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method=='POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email=form.cleaned_data['email']
            password = form.cleaned_data['password2']

            user = User.objects.create_user(username=username,password=password,email=email)

            user_profile = UserProfile(user=user)
            user_profile.save()
            #return HttpResponseRedirect("/accouts/login/")
            return HttpResponseRedirect("/login/")
    else:
        form = RegistrationFrom()
    return render(request,'users/registration.html',{'form':form})

@csrf_exempt
def login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username,password=password)

            if user is not None and user.is_active:
                auth.login(request,user)
                #return redirect('/', {'user': user})
                return HttpResponseRedirect("/article/",{'user':user})
               # return HttpResponseRedirect(reverse('users:profile',args=[user.id]))
            else:
                return render(request,'users/login.html',{'form': form,'message':'Wrong password. Please try again.'})
    else :
        form = LoginForm()
    #return render(request, 'users/login.html', {'form': form})
    return render(request,'users/login.html')


def logout(request):
    auth.logout(request)
    return render(request,'users/index.html')

def article(request):
    article_list = Article.objects.all()
    # print article_list
    # print type(article_list)
    #QuerySet是一个可遍历结构，包含一个或多个元素，每个元素都是一个Model实例
    #QuerySet类似于Python中的list，list的一些方法QuerySet也有，比如切片，遍历。
    #每个Model都有一个默认的manager实例，名为objects，QuerySet有两种来源：通过manager的方法得到、通过QuerySet的方法得到。mananger的方法和QuerySet的方法大部分同名，同意思，如filter(),update()等，但也有些不同，如manager有create()、get_or_create()，而QuerySet有delete()等
    return render(request, 'users/article.html',{'article_list': article_list})

def detail(request,id):
    # print id
    try:
        article = Article.objects.get(id=id)
        # print type(article)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'users/detail.html',locals())
    #return render(request,'users/detail.html',{'article':article})

def profile(request,pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/profile.html', {'user': user})