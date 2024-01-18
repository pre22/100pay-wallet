import requests

from decouple import config

from django.http import HttpResponse, JsonResponse


def create_payment_charge_view(request):

    url = "https://api.100pay.co/api/v1/pay/charge"

    payload = {
        "ref_id": "012232",
        "customer": {
            "user_id": "111",
            "name": "Brainy Josh",
            "phone": "80123456789",
            "email": "user@site.com"
        },
        "billing": {
            "description": "MY TEST PAYMENT",
            "amount": 10000,  # Converted string to integer
            "country": "NG",
            "currency": "NGN",
            "vat": 10,  # Converted string to integer
            "pricing_type": "fixed_or_partial_price"
        },
        "metadata": {
            "is_approved": True  # Converted string to boolean
        },
        "call_back_url": "http://localhost:8000/verify-payment",
        "userId": "6143bfb7fe85e0020bf243f9",
        "charge_source": "api"
    }

    headers = {
        'api-key': config('100PAY-APIKEY')
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    data = response.json()

    print(data)

    return HttpResponse('success')


def get_payment_charge_view(request, chargeId):

    url = f"https://api.100pay.co/api/v1/pay/charge/{chargeId}"

    payload={}

    headers = {
        'api-key': config('100PAY-APIKEY')
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return HttpResponse('success')


def create_crypto_charge_view(request, charge_id):
    url = f"https://api.100pay.co/api/v1/pay/crypto/{charge_id}"

    payload = ""

    headers = {
        'api-key': config('100PAY-APIKEY')
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return HttpResponse('success')


def get_crypto_charge_view(request, crypto_charge_id):
    url = f"https://api.100pay.co/api/v1/pay/crypto/{crypto_charge_id}"

    payload={}

    headers = {
        'api-key': config('100PAY-APIKEY')
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return HttpResponse('success')


def cancel_crypto_charge_view(request, crypto_charge_id):

    url = f"https://api.100pay.co/api/v1/pay/crypto/cancel/{crypto_charge_id}"

    payload={}

    headers = {
    'api-key': '{{api-key}}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return HttpResponse('success')


def convert_checkout_view(request):
    url = "https://api.100pay.co/api/v1/pay/crypto/convert"

    payload = {
        "wallet": {
            "symbol": "USDT",
            "convert_id": 825,  # Converted string to integer
            "chart": "cmc"
        },
        "local": {
            "amount": 20,  # Converted string to integer
            "currency": "USD"
        },
        "_id": "641bf59387aae40037176543",
        "network": "bsc"
    }
    
    headers = {
        'api-key': '{{api-key}}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return HttpResponse('success')


def verify_payment_view(request, payment_ID):

    url = f"https://api.100pay.co/api/v1/pay/crypto/payment/{payment_ID}"

    payload={}

    headers = {
        'api-key': config('100PAY-APIKEY')
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return HttpResponse('success')
