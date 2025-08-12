from django.http import JsonResponse
from django.shortcuts import render
from .models import BasketOrderModel, OrderDetailModel
from django.views import View
from product_app.models import ProductModel


# Create your views here.


class OrderView(View):
    def get(self, request):
        user = request.user
        details = OrderDetailModel.objects.filter(basket__user=user, basket__is_paid=False)
        return render(request, 'order_page.html', {
            'details' : details

        })


def add_to_order(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = int(request.GET.get('product_id'))
        count = int(request.GET.get('count'))
        product = ProductModel.objects.filter(id=product_id).first()
        basket, created = BasketOrderModel.objects.get_or_create(user=user, is_paid=False)
        # order_detail, created = OrderDetailModel.objects.filter(basket_id=basket.id, product_id=product_id)
        # if created:
        #     if count > int(product.count):
        #         return JsonResponse({'status': 'over_count'})
        # else:
        #     if order_detail:
        #         order_detail.count += count
        #         if order_detail.count>int(product.count):
        #             return JsonResponse({'status': 'over_count'})
        #         else:
        #             order_detail.save()
        #             return JsonResponse({'status': 'success'})

        order_detail = OrderDetailModel.objects.filter(basket=basket, product_id=product_id).first()
        if order_detail is not None:
            order_detail.count += count
            if order_detail.count>int(product.count):
                return JsonResponse({'status': 'over_count'})
            else:
                order_detail.save()
                return JsonResponse({'status': 'success'})

        else:
           if count > int(product.count):
               return JsonResponse({'status': 'over_count'})
           else:
               order_detail = OrderDetailModel(basket_id=basket.id, count=count, product_id=product_id, off=0)
               order_detail.save()
               return JsonResponse({'status': 'success'})

    else:
        return JsonResponse({'status': 'not_login'})

def change_count_basket(request):
    try:
        detail_id =int(request.GET.get('detail_id'))
        state = request.GET.get('state')
        user = request.user
        detail = OrderDetailModel.objects.filter(basket__user=user, basket__is_paid=False,product_id = detail_id).first()
        product = detail.product
        print(product)
        if  state =='plus':
            detail.count += 1
            if detail.count > product.count:
                return JsonResponse({'status': 'not_enough'})
            else:
                detail.save()
                basket = detail.basket
                return render(request, 'order_page.html', {
                    'basket' : basket
                })
        elif state =='minus':
            detail.count -= 1
            if detail.count < 1:
                detail.delete()
                return JsonResponse({'status': 'not_enough'})
            else:
                detail.save()
                basket = detail.basket
                return render(request, 'order_page.html', {
                    'basket': basket
                })


    except:
        print('lo')
# def change_count_basket(request):
#     try:
#         detail_id = int(request.GET.get('detail_id'))
#         state = request.GET.get('state')
#         user = request.user
#         detail = OrderDetailModel.objects.filter(
#             basket__user=user, basket__is_paid=False, product_id=detail_id
#         ).first()
#
#         if not detail:
#             return JsonResponse({'status': 'not_found'})
#
#         product = detail.product
#
#         if state == 'plus':
#             detail.count += 1
#             if detail.count > product.count:
#                 return JsonResponse({'status': 'not_enough'})
#             detail.save()
#
#         elif state == 'minus':
#             detail.count -= 1
#             if detail.count < 1:
#                 detail.delete()
#                 return JsonResponse({'status': 'removed'})
#             detail.save()
#
#         # اینجا همیشه در نهایت چیزی برمی‌گردونیم
#         basket = detail.basket
#         return render(request, 'order_page.html', {
#             'basket': basket
#         })

    # except Exception as e:
    #     print('Error:', e)
    #     return JsonResponse({'status': 'error'})
