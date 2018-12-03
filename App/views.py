import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
from .models import *
from AXF.settings import MEDIA_ROOT
import hashlib
import uuid


# Create your views here.
def user_index(request):
    return render(request, 'App/index.html')


def user_home(request):
    image = MainWheel.objects.all()
    navs = MainNav.objects.all()
    mustbuy = MainMustBuy.objects.all()
    shop = MainShop.objects.all()
    shop0 = shop[0]
    shop1_2 = shop[1:3]
    shop3_6 = shop[3:7]
    shop7_10 = shop[7:]

    shows = MainShow.objects.all()

    data = {
        'image': image,
        'navs': navs,
        'mustbuys': mustbuy,
        'shop0': shop0,
        'shop1_2': shop1_2,
        'shop3_6': shop3_6,
        'shop7_11': shop7_10,
        'shows': shows,

    }
    return render(request, 'home/home.html', data)


def user_market(request, typeid, childid, sortid):
    types = MainFoodtypes.objects.all()

    foodtypes = MainFoodtypes.objects.get(typeid=typeid)  # one type data
    childTypes = foodtypes.childtypenames  # child type
    childTypesList = childTypes.split('#')
    childs = []
    for childType in childTypesList:
        childList = childType.split(':')
        childs.append(childList)
    print(childs)
    # goods = MainGoods.objects.all()
    goods = MainGoods.objects.filter(categoryid=typeid)
    if childid != '0':
        goods = goods.filter(childcid=childid)
    if sortid == '0':
        pass
    elif sortid == '1':
        goods = goods.order_by('productnum')
    elif sortid == '2':
        goods = goods.order_by('-price')
    elif sortid == '3':
        goods = goods.order_by('price')
    data = {
        'types': types,
        'goods': goods,
        'foodtype': typeid,
        'childs': childs,
        'childid': childid,
    }
    return render(request, 'market/market.html', data)


def user_cart(request):
    username = request.session.get('username')
    userid = request.session.get('userid')
    carts = Cart.objects.filter(user_id=userid)
    data = {
        'username': username,
        'carts': carts
    }
    return render(request, 'cart/cart.html', data)


def cartadd(request):
    userid = request.session.get('userid')
    if userid:
        if request.method == 'GET':
            goodid = request.GET.get('goodid')
            num = request.GET.get('num')
            carts = Cart.objects.filter(user_id=userid, goods_id=goodid)

            if carts.exists():
                cart = carts.first()
                cart.num += int(num)
                cart.save()
            else:
                cart = Cart()
                cart.user_id = userid
                cart.goods_id = goodid
                cart.num = num
                cart.save()
            return JsonResponse({'status': 1, 'msg': '加入购物车成功!'})
        else:
            return JsonResponse({'status': -1, 'msg': 'request wrong!'})
    else:
        return JsonResponse({'status': 0, 'msg': '您尚未登录，是否前往登录'})


def cartNumAdd(request):
    data = {
        'status': 1,
        'msg': '加入成功'
    }

    if request.method == 'GET':
        cartid = request.GET.get('cartid')
        carts = Cart.objects.filter(id=cartid)
        if carts.exists():
            cart = carts.first()
            cart.num += 1
            cart.save()

            # new num into cart page
            data['num'] = cart.num
        else:
            data['status'] = -1
            data['msg'] = 'your cart not have this one'
    else:
        data['status'] = -2
        data['msg'] = 'request is wrong'
    return JsonResponse(data)


def cartNumReduce(request):
    data = {
        'status': 1,
        'msg': 'reduce成功'
    }

    if request.method == 'POST':
        cartid = request.POST.get('cartid')
        carts = Cart.objects.filter(id=cartid)
        if carts.exists():
            cart = carts.first()
            if cart.num > 1:
                cart.num -= 1
            cart.save()

            # new num into cart page
            data['num'] = cart.num
        else:
            data['status'] = -1
            data['msg'] = 'your cart not have this one'
    else:
        data['status'] = -2
        data['msg'] = 'request is wrong'
    return JsonResponse(data)


def cartDel(request):
    data = {
        'status': 1,
        'msg': 'delete成功'
    }

    if request.method == 'POST':
        cartid = request.POST.get('cartid')
        Cart.objects.filter(id=cartid).delete()
    else:
        data['status'] = -2
        data['msg'] = 'request is wrong'
    return JsonResponse(data)


def cartSelect(request):
    data = {
        'status': 1,
        'msg': 'select成功'
    }

    if request.method == 'POST':
        cartid = request.POST.get('cartid')
        carts = Cart.objects.filter(id=cartid)
        if carts.exists():
            cart = carts.first()
            cart.selected = not cart.selected
            cart.save()

            # new num into cart page
            data['selected'] = cart.selected
        else:
            data['status'] = -1
            data['msg'] = 'your cart not have this one'
    else:
        data['status'] = -2
        data['msg'] = 'request is wrong'
    return JsonResponse(data)


def cartSelectAll(request):
    data = {
        'status': 1,
        'msg': 'selectall成功'
    }

    if request.method == 'POST':
        isall = request.POST.get('isAllSelect')
        carts = Cart.objects.all()
        if int(isall) == 1:
            data['selectall'] = 0
            for cart in carts:
                cart.selected = False
                cart.save()
        else:
            data['selectall'] = 1
            for cart in carts:
                cart.selected = True
                cart.save()
    else:
        data['status'] = -2
        data['msg'] = 'request is wrong'
    return JsonResponse(data)


def order(request, oid):
    order = Order.objects.get(id=oid)
    return render(request, 'App/order.html', {'order': order})


def changeOrderStatus(request):
    data = {
        'status': 1,
        'msg': '成功'
    }

    if request.method == 'POST':
        orderid = request.POST.get('orderid')
        status = request.POST.get('status')
        print(status)
        Order.objects.filter(id=orderid).update(status=status)
    else:
        data['status'] = -1
        data['msg'] = 'request is wrong'
    return JsonResponse(data)


def orderAdd(request):
    data = {
        'status': 1,
        'msg': 'product成功'
    }

    if request.method == 'POST':
        order = Order()
        userid = request.session.get('userid')
        order.orderid = randomGenerator()
        order.user_id = userid
        order.save()

        carts = Cart.objects.filter(user_id=userid, selected=True)

        total = 0
        for cart in carts:
            orderGoods = OrderGoods()
            orderGoods.order_id = order.id
            orderGoods.goods_id = cart.goods_id
            orderGoods.num = cart.num
            orderGoods.price = cart.goods.price

            orderGoods.save()

            total += orderGoods.num * orderGoods.price

        order.price = total
        data['orderid'] = order.id

        # clear cart
        carts.delete()
        order.save()
    else:
        data['status'] = -1
        data['msg'] = 'request is wrong'

    return JsonResponse(data)


def orderunreceive(request):
    userid = request.session.get('userid')

    if not userid:
        return redirect(reverse('App:login'))
    else:
        orders = Order.objects.filter(status=1,user_id=userid)
        return render(request, 'App/order_unreceive.html', {'orders': orders})


def orderget(request):
    data = {
        'status': 1,
        'msg': 'get成功',
    }
    userid = request.session.get('userid')
    ordersid = request.POST.get('ordersid')
    if request.method == "POST":
        Order.objects.filter(status=1,id=ordersid,user_id=userid).delete()
    else:
        data['status'] = -1
        data['msg'] = 'request is wrong'
    return JsonResponse(data)

def user_mine(request):
    username = request.session.get('username')
    icon = request.COOKIES.get('icon')

    data = {
        'username': username,
        'icon': icon,
    }
    return render(request, 'mine/mine.html', data)


def user_login(request):
    return render(request, 'App/login.html')


def user_register(request):
    return render(request, 'App/register.html')


def myMd5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()


def randomGenerator():
    uid = str(uuid.uuid4())
    return myMd5(uid)


def loginHandle(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=myMd5(password))
        if user.exists():
            iconimg = user.get(username=username).icon
            userid = user.get(username=username).id
            response = redirect(reverse('App:mine'))
            request.session['username'] = username
            request.session['userid'] = userid
            # request.session['icon'] = iconimg
            response.set_cookie('icon', iconimg)
            print(request.session.get('username'))
        else:
            return HttpResponse('username or password is wrong')
    else:
        return HttpResponse('request is wrong')
    return response


def checkUserName(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        if User.objects.filter(username=username):
            return JsonResponse({'status': 0, 'msg': 'username is exists'})
        else:
            return JsonResponse({'status': 1, 'msg': 'username is useable'})
    else:
        return JsonResponse({'status': -1, 'msg': 'request is wrong'})


def registerHandle(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('files')

        user = User()
        user.username = username
        user.password = myMd5(password)
        user.email = email

        # random file name
        iconRandomName = randomGenerator() + os.path.splitext(icon.name)[1]
        iconFile = MEDIA_ROOT + iconRandomName

        if not icon:
            return HttpResponse('you have not update image')
        with open(iconFile, 'ab') as f:
            for part in icon.chunks():
                f.write(part)
                f.flush()
        user.icon = '/uploads/' + iconRandomName
        response = redirect(reverse('App:login'))
        # return HttpResponse('Success')
        user.save()
    else:
        return HttpResponse('is a wrong request')

    return response


def login_out(request):
    response = redirect(reverse('App:mine'))
    del request.session['username']
    request.session.flush()
    # del request.session['userid']
    # request.session.flush()
    # del request.session['icon']
    # request.session.flush()
    response.delete_cookie('icon')
    return response
