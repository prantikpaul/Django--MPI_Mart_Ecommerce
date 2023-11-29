from django.shortcuts import render,redirect
from sslcommerz_lib import SSLCOMMERZ
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def payment(request,id):
    
    total=id
    
    sslcz = SSLCOMMERZ({'store_id': 'niyam6412dc52e1e89', 'store_pass': 'niyam6412dc52e1e89@ssl', 'issandbox': True})
    total_amount = total
    data = {
        'total_amount': total_amount,
        'currency': "BDT",
        'tran_id': "tran_12345",
        'success_url': "http://127.0.0.1:8000/Payment/born_To_redirect/",
        # if transaction is succesful, user will be redirected here
        'fail_url': "http://127.0.0.1:8000/Payment/payment_failed/",  # if transaction is failed, user will be redirected here
        # 'cancel_url': "http://127.0.0.1:8000/payment-cancelled",
        # after user cancels the transaction, will be redirected here
        'emi_option': "0",
        'cus_name': "test",
        'cus_email': "test@test.com",
        'cus_phone': "01700000000",
        'cus_add1': "customer address",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'multi_card_name': "",
        'num_of_item': 1,
        'product_name': "Test",
        'product_category': "Test Category",
        'product_profile': "general",
    }
    

    response = sslcz.createSession(data)

    return redirect(response['GatewayPageURL'])

@csrf_exempt
def born_To_redirect(request):
    
    return redirect ('order_success')

@csrf_exempt
def payment_failed(request):
    

    return render (request,'payment/payment_failed.html',locals())