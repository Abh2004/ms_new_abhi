from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import blog,Hallpics, pics2019, pics2018, Champs2020to2021tech, Champs2011to2012sports, Champs2012to2013socult, Champs2016to2017sports, Champs2017to2018sports, Champs2018to2019sports, Champs2019to2020socult, Champs2019to2020tech, ugd, phdd, alumnid,hallnotices
from django.contrib.auth.models import auth, User
from django.contrib import messages

# Create your views here.

def home(request) :
    return render(request, 'msh/home/index.html')

def gallery(request) :
    pics1 = Hallpics.objects.all()
    pics2 = pics2019.objects.all()
    pics3 = pics2018.objects.all()
    print("!")
    return render(request, 'msh/gallery/index1.html', {'pics1': pics1, 'pics2': pics2, 'pics3': pics3})

def hof(request) :
    champs20t = Champs2020to2021tech.objects.all()
    champs11s = Champs2011to2012sports.objects.all()
    champs12c = Champs2012to2013socult.objects.all()
    champs16s = Champs2016to2017sports.objects.all()
    champs17s = Champs2017to2018sports.objects.all()
    champs18s = Champs2018to2019sports.objects.all()
    champs19c = Champs2019to2020socult.objects.all()
    champs19t = Champs2019to2020tech.objects.all()
    return render(request, 'msh/hall of fame/index3.html', {'champs20t': champs20t, 'champs11s': champs11s, 'champs12c': champs12c, 'champs16s': champs16s, 'champs17s': champs17s, 'champs18s': champs18s, 'champs19c': champs19c, 'champs19t': champs19t})

def halln(request) :
    obj=hallnotices.objects.all()
    context={
        "notices":obj
    }
    return render(request, 'msh/notice/index3.html',context)

def gcn(request) :
    return render(request, 'msh/notice/index4.html')

def messn(request) :
    return render(request, 'msh/notice/index5.html')

def dat(request) :
    return render(request, 'msh/database/database.html')

def genn(request) :
    return render(request, 'msh/notice/index6.html')

def datug(request) :
    dept = request.POST.get('dept')
    year = request.POST.get('year')
    data = ugd.objects.all().filter(dept = dept)
    data = data.filter(year = year)
    return render(request, 'msh/database/form_ug.html', {'datas': data})

def datphd(request) :
    dept = request.POST.get('dept')
    year = request.POST.get('year')
    data = phdd.objects.all().filter(dept = dept)
    data = data.filter(year = year)
    return render(request, 'msh/database/form_phd.html', {'datas': data})

def datalumni(request) :
    year = request.POST.get('year')
    data = alumnid.objects.all().filter(year = year)
    return render(request, 'msh/database/form_alumni.html', {'datas': data})

def login(request) :
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']
        user=auth.authenticate(username=username, password=password1)
        print(user)
        if user is not None:
            print("user logged in")
            auth.login(request, user)
            if alumnid.objects.all().filter(Roll=username).exists():
                pres = alumnid.objects.all().filter(Roll=username).values_list('Name', flat=True)
            elif phdd.objects.all().filter(Roll=username).exists():
                pres = phdd.objects.all().filter(Roll=username).values_list('Name', flat=True)
            else:
                pres = ugd.objects.all().filter(Roll=username).values_list('Name', flat=True)
            messages.info(request, 'Please refresh the page')
            return render(request,'msh/home/logged.html', {'name':pres[0]})
        else :
            print("no user")
            return render(request, 'msh/home/wrong.html')
    else:
        print("called")
        return render(request, 'msh/home/login.html')

def logged(request) :
    pres =User.objects.all().filter(username=request.user.username).values_list('first_name', flat=True)
    name = pres[0]
    return render(request, 'msh/home/logged.html', {'name': name})

def logout(request) :
    auth.logout(request)
    return redirect('../../../')

def change(request) :
    if request.method == 'POST':
        username = request.POST['roll']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        u = User.objects.get(username=username)
        if u is not None:
            if password1 == password2 :
                u.set_password(password1)
                u.save();
                user=auth.authenticate(username=username, password=password1)
                auth.login(request, user)
                return redirect('../../../')
            else :
                messages.info(request, 'Passwords do not match')
                return redirect('change')
        else :
            messages.info(request, "Please check your Roll number, you've typed an incorrect one!")
            return redirect('change')
    else :
        return render(request, 'msh/home/forgot.html')

def signup(request) :
    if request.method == 'POST':
        if 'signup' in request.POST :
            username = request.POST['roll']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            ans = request.POST['security'].lower()
            if alumnid.objects.all().filter(Roll=username).exists() | phdd.objects.all().filter(Roll=username).exists() | ugd.objects.all().filter(Roll=username).exists():
                if alumnid.objects.all().filter(Roll=username).exists():
                    pres = alumnid.objects.all().filter(Roll=username).values_list('Name', flat=True)
                elif phdd.objects.all().filter(Roll=username).exists():
                    pres = phdd.objects.all().filter(Roll=username).values_list('Name', flat=True)
                else:
                    pres = ugd.objects.all().filter(Roll=username).values_list('Name', flat=True)
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Is there a typo in your roll number? If not, Contact us stating this error.")
                    return redirect('signup')
                elif password1!=password2 :
                    messages.info(request, 'Passwords do not match')
                    return redirect('signup')
                else :
                    user = User.objects.create_user(username=username, password = password1, first_name=pres[0], last_name=ans)
                    user.save();
                    print('user created')
                    auth.login(request, user)
                    return redirect('../')
            else :
                messages.info(request, "Sign up is permitted only for MSH boarders, you can go through the guest version of our website! Contact us if you're a MS Hall boarder and getting this error")
                return redirect('signup')
        else :
            username = request.POST['roll']
            security = request.POST['security'].lower()
            user=auth.authenticate(username=username, last_name=security)
            pres = User.objects.all().filter(username=username).values_list('last_name', flat=True)
            if pres[0]==security :
                return redirect('../change/')
            else :
                messages.info(request, 'Incorrect Roll Number or Security answer')
                return redirect('signup')

    else :
        return render(request, 'msh/home/signup.html')

def hcm(request) :
    return render(request, 'msh/hmc/index7.html')

def blogs(request):
    obj=blog.objects.all()
    for ob in obj:
        print(ob.Title)
    # print(obj.length())
    context={
        "blogs":obj
    }
    return render(request,'msh/blogs/index.html',context)

def blog_Desc(request,id):
    obj=blog.objects.get(id=id)

    context={
        "blog":obj
    }
    return render(request,'msh/blogs/new.html',context)
def gallery_new(request):
    return render(request,'msh/amweb-main/Gallery.html')

