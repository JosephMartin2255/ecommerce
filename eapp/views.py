from django.shortcuts import render,redirect
from eapp.models import Category
from eapp.models import Products
from eapp.models import userdetails
from eapp.models import Cart
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')
def loginpage(request):
    return render(request,'loginpage.html')
def logincreate(request):
    if request.method=='POST':
        Username=request.POST['Uname']
        Password=request.POST['Pwd']
        user=auth.authenticate(username=Username, password=Password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('adminhome')
            else:
                auth.login(request, user)
                messages.info(request,f'welcome {Username}')
                return redirect('userhomepage')
        else:
            messages.info(request, 'Invalid USERNAME or PASSWORD')
            return redirect('loginpage')
    else:
        return redirect('loginpage')
def logout(request):
        auth.logout(request)
        return redirect('homepage')



def adminhome(request):
    return render(request,'adminhome.html')
def addcategory(request):
    return render(request,'addcategory.html')
def addcategory1(request):
    if request.method=="POST":
        categoryname=request.POST['nm'] 
        ctg=Category(category_name=categoryname)
        ctg.save()
        return redirect('addcategory')
def addproducts(request):
    categories = Category.objects.all()
    return render(request,'addproducts.html',{'categories': categories})
def addproducts1(request):
    if request.method=="POST":
        productname=request.POST['name']
        productdescription=request.POST['description']
        productprice=request.POST['price']
        productimage=request.FILES['file']
        categorynm=request.POST['nm']
        category1=Category.objects.get(id=categorynm)
        pt=Products(product_name=productname,product_description=productdescription,product_price=productprice,product_image=productimage,category=category1)
        pt.save()
        return redirect('viewproducts')
def viewproducts(request):
    product1=Products.objects.all()
    return render(request,'viewproducts.html',{'products':product1})
def deleteproducts(request,id):
    product=Products.objects.get(id=id)
    product.delete()
    return redirect('viewproducts')
def viewusers(request):
    users = userdetails.objects.all()
    return render(request,'viewusers.html',{'user':users})
def deleteusers(request,id):
    user1=userdetails.objects.get(user=id)
    user1.delete()
    user2=User.objects.get(id=id)
    user2.delete()
    return redirect('viewusers')
   


def usersignup(request):
    return render(request,'usersignup.html')
def usersignup1(request):
    if request.method=="POST":
        user_fname=request.POST['fname']
        user_lname=request.POST['lname']
        user_uname=request.POST['uname']
        user_pwd=request.POST['pwd']
        user_email=request.POST['email']
        user = User.objects.create_user(
            first_name=user_fname,
            last_name=user_lname,
            username=user_uname,
            password=user_pwd,
            email=user_email)
        user.save()

        user_address = request.POST['address']
        user_contact = request.POST['contact']
        user_img = request.FILES['file']
        
        user1 = userdetails(
        user=user, address=user_address,number=user_contact, img=user_img)
        user1.save()
        return redirect('loginpage')  
    return render(request,'usersignup1.html')
def userhomepage(request):
    categories1 = Category.objects.all()
    print("hai")
    return render(request, 'userhomepage.html', {'categories': categories1})
def aboutpage(request):
    categories2 = Category.objects.all()
    return render(request,'about.html', {'categories': categories2})
def categorypage(request, id):
    category = Category.objects.get(id=id)
    products = Products.objects.filter(category=category)
    categories = Category.objects.all() 
    return render(request, 'categorypage.html', {'category': category, 'products': products, 'categories': categories})




def cart(request, product_id):
    pr=Products.objects.get(id=product_id)
    cart_item, created=Cart.objects.get_or_create(user=request.user,prod=pr)
    if not created:
        cart_item.quantity +=1
        cart_item.save()
    return redirect('cartde')
def cartde(request):
    cart_items=Cart.objects.filter(user=request.user).select_related('prod')
    total_pr=sum(item.total_price() for item in cart_items)
    coun=Cart.objects.values_list('quantity',flat=True).count()
    return render(request,'cartpage.html',{'caite':cart_items,'totalpr':total_pr,'cou':coun})
def increase(request,k):
    cart_item=Cart.objects.get(prod_id=k,user=request.user)
    cart_item.quantity +=1
    cart_item.save()
    return redirect('cartde')
def decrease(request,k):
    cart_item=Cart.objects.get(prod_id=k,user=request.user)
    cart_item.quantity -=1
    cart_item.save()
    return redirect('cartde')
def remove(request,k):
    cart_item=Cart.objects.filter(user=request.user).first()
    if cart_item:
        cart_item.delete()
    return redirect('cartde')


  





        
def checkoutpage(request):
    return render(request,'checkoutpage.html')


        