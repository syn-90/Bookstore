from django.http import JsonResponse
from django.shortcuts import render
from .models import BasketOrderModel, OrderDetailModel
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from product_app.models import ProductModel


# Create your views here.


class OrderView(View):
    def get(self, request):
        try:
            user = request.user
            basket = BasketOrderModel.objects.filter(user= user, is_paid=False).first()
            details =basket.orderdetailmodel_set.all()
            return render(request, 'order_page.html', {
                'details' : details ,
                'basket' : basket

            })
        except:
            return render(request, 'order_page.html', {


            })


def add_to_order(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = int(request.GET.get('product_id'))
        # count = int(request.GET.get('count'))
        # product = ProductModel.objects.filter(id=product_id).first()
        basket, created_ = BasketOrderModel.objects.get_or_create(user=user, is_paid=False)
        order_detail = OrderDetailModel.objects.filter(basket=basket, product_id=product_id).first()
        if order_detail is not None:
            print('lo')
            return JsonResponse({'status': 'already_add'})

        else:
            order_detail = OrderDetailModel(basket=basket, product_id=product_id,count=1, off=5)
            print(order_detail.count)
            order_detail.save()
            return render(request, 'template_service/icon_basket.html', {
                'basket' : basket
            })

    else:
        return JsonResponse({'status': 'not_login'})

def change_count_basket(request):
    try:
        detail_id = int(request.GET.get('detail_id'))
        state = request.GET.get('state')
        user = request.user
        basket = BasketOrderModel.objects.filter(user=user, is_paid=False).first()
        details = OrderDetailModel.objects.filter(basket__user_id=user.id, basket__is_paid=False)
        detail = OrderDetailModel.objects.filter(
            basket__user=user, basket__is_paid=False, product_id=detail_id
        ).first()

        if not detail:
            return JsonResponse({'status': 'not_found'})

        product = detail.product

        if state == 'plus':
            detail.count += 1
            if detail.count > product.count:
                return JsonResponse({'status': 'not_enough'})
            else:
                detail.save()
                basket = detail.basket
                return render(request, 'basket.html', {
                    'details' : basket.orderdetailmodel_set.all,
                    'basket':basket
                })

        elif state == 'minus':
            detail.count -= 1
            if detail.count < 1:
                detail.delete()
                return render(request, 'basket.html', {
                    "basket" : basket,
                    'details': details
                })
            else:
                detail.save()
                basket = detail.basket
                return render(request, 'basket.html', {
                    "basket": basket,
                    'details': basket.orderdetailmodel_set.all
                })

        basket = detail.basket
        return render(request, 'order_page.html', {
            'basket': basket
        })

    except Exception as e:
        print('Error:', e)
        return JsonResponse({'status': 'error'})

@csrf_exempt
def remove_detail(request):
    if request.method == 'POST':
        detail_id = int(request.POST.get('detail_id'))
        user = request.user
        basket = BasketOrderModel.objects.filter(is_paid=False, user = user).first()
        details = OrderDetailModel.objects.filter(basket__user_id=user.id, basket__is_paid=False)
        detail = OrderDetailModel.objects.filter(basket__user= user, id= detail_id, basket__is_paid=False).first()
        if detail is not None:
            detail.delete()
            if details is not None:
                return render(request, 'basket.html', {
                    "basket" : basket,
                    'details' : details
                })
            else:
                return render(request, 'basket.html', {
                    "basket" : basket,
                    'empty_basket':  True
                })

        else:
            return JsonResponse({'message' : 'not_found'} , status=404)
        # if detail is not None:
        #     print('lo')
        #     detail.delete()
        #     return JsonResponse({'message':'success'}, status=201)
        # else:
        #     return JsonResponse({'message':'not_found'}, status=404)
