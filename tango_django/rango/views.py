from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category,Car
from rango.forms import CategoryForm,CarForm,UserForm,UserProfileForm

# rendering and responding to reqs
def index(req):
    category_list = Category.objects.order_by('-likes')[:5]
    cars_list = Car.objects.order_by("-views")[:3]
    context_dict = {'categories':category_list,"cars":cars_list}
    return render(req,'rango/index.html',context=context_dict)
    req.session.set_test_cookie()
    request.session.set_test_cookie() 
def show_category(req,category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        cars = Car.objects.filter(category=category)
        context_dict['cars'] = cars
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['cars'] = None
        context_dict['category'] = None
    return render(req,'rango/categories.html',context_dict)
def carName(req,car_name):
    return HttpResponse(f'your looking for {car_name}')

def about(req):
    if req.session.test_cookie_worked():
        print("cookie worked !")
        req.session.delete_test_cookie()
    return render(req,'rango/about.html')
def login(req):
    return render(req,'rango/login.html')

# forms handling

def add_category(req):
    form = CategoryForm()
    # HTTP POST 
    if req.method == 'POST':
        form = CategoryForm(req.POST)
        #checking values
        if form.is_valid():
            print('form is valid')
            form.save(commit=True)
            return index(req)
        else:
            print('form not valid')
            print(form.errors)
    return render(req,'rango/add_cat.html',{'form':form})
    
def add_car(req,category_name_slug):
    try:
        category =Category.objects.get(slug= category_name_slug)
    except Category.DoesNotExist:
        
        category = None

    form = CarForm()
    if req.method == 'POST':
        form = CarForm(req.POST)
        if form.is_valid():
            if category:
                car = form.save(commit=False)
                car.category = category
                car.views= 0
                car.save()
                return show_category(req,category_name_slug)
            form.save(commit=True)
            return render(req,f'rango/{Category.slug}/{Car.name}')
        else :
            print(form.errors)
    context_dict = {'form':form,'category':category}
    return render(req,'rango/add_cat.html',context_dict)
def register(req):
    registered = False
    if req.method == 'POST ':
        user_form = UserForm(data=req.POST)
        profile_form = UserProfileForm(data=req.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save()
            profile.user = user
            if 'picture' in req.FILES :
                profile.picture = req.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors) 
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    context_dict = {'user_form':user_form,'profile_form':profile_form,'registered':registered}
    return render(req,'rango/register.html',context_dict)
