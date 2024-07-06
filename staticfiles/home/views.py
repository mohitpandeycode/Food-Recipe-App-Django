from django.shortcuts import render,redirect
from home.models import Recipe
from django.contrib.auth.models import User  # use this for Creating User
from django.contrib.auth import authenticate, login,logout  # use this for login and logout the user 
from django.contrib import messages   #use this for Get maasage when signin login go to singnup function..

# Create your views here.
def index(request):
   recp = Recipe.objects.all()

#serch functionality.....
   if request.method == "GET":
      search = request.GET.get('search')
      if search != None:
         recp = Recipe.objects.filter(recipe_name__icontains=search)

#normal page functionality.....
   if request.method == "POST":
     recipe_name = request.POST.get('recipe_name')
     Description = request.POST.get('Description')
     image = request.FILES.get('image')
     recipe = Recipe(recipe_name = recipe_name,Description = Description,image = image )
     recipe.save()
     return redirect('/')  
   data = {'items':recp}
   return render(request,'index.html',data)

# for Delete items
def delete_items(request,id):
   item = Recipe.objects.get(id=id)
   item.delete()
   return redirect('/')


# for Update items.....
def update_item(request,id):
   item = Recipe.objects.get(id=id)
   data ={'recipe':item}
   if request.method=="POST":
      recipe_name = request.POST.get('recipe_name')
      Description = request.POST.get('Description')
      image = request.FILES.get('image')

      item.recipe_name = recipe_name
      item.Description = Description
      if image:
         item.image = image
      item.save()
      done = True
      return render(request,'update.html',{'Done':done,'recipe':item})

   return render(request,'update.html',data)

# for view the perticuler recipe...
def viewRecipe(request,id):
   view = Recipe.objects.get(id = id)
   item = {'view':view}
   return render(request,'viewRecipe.html',item)

# for signup page......
def signup(request):
   if request.method =="POST":
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      username = request.POST.get('username')
      password = request.POST.get('password')
      cpassword = request.POST.get('cpassword')
      if password != cpassword:
          messages.error(request, "Please check the Password and Confirm Password must be same! ")
          return redirect("/signup/")
      user = User.objects.filter(username = username)
      if user.exists():
         messages.error(request, "Username Already taken!")
         return redirect("/signup/")
   
      user = User.objects.create_user(username,None,password)
      user.first_name = first_name
      user.last_name = last_name
      user.save()
      messages.success(request, "Account Created Succcesfully!")
      return redirect("/signup/")
   return render(request,'signup.html')

# for login the user....
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('loginusername')
        password = request.POST.get('pass')

        # check the username...
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username!')
            return redirect("/login/")

        # authenticate the user....
        user = authenticate(request, username=username, password=password)

        # login the user.....
        if user is None:
            messages.error(request, 'Invalid Password!')
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/")

    return render(request, 'login.html')

# for logout the user....
def user_logout(request):
   logout(request)
   return redirect("/")