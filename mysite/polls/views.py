from django.shortcuts import render, redirect
from django.http import JsonResponse
import pandas as pd
import pickle
import os

def index_func(request):
    res = None
    error_message = ''
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in request.headers.get('Accept', '')

    if request.method == 'POST':
        try:
            name = request.POST.get('Name', '').strip()
            repute = request.POST.get('repute', '').strip()
            height = request.POST.get('Height', '').strip()
            width = request.POST.get('Width', '').strip()
            weight = request.POST.get('Weight', '').strip()
            material = request.POST.get('material', '').strip()
            basePrice = request.POST.get('basePrice', '').strip()
            basePriceShipping = request.POST.get('basePriceShipping', '').strip()
            international = request.POST.get('international', '0').strip()
            expressShipment = request.POST.get('expressShipment', '0').strip()
            installments = request.POST.get('installments', '0').strip()
            transport = request.POST.get('Transport', '0').strip()
            fragile = request.POST.get('Fragile', '0').strip()
            customer = request.POST.get('cust', '0').strip()
            remote = request.POST.get('remote', '0').strip()
            waiting = request.POST.get('waiting', '').strip()

            if not name:
                error_message = 'Please enter the artist name.'
            elif not repute or not height or not width or not weight or not basePrice or not basePriceShipping or not waiting:
                error_message = 'Please fill in all numerical dimensions and pricing fields.'
            elif not material:
                error_message = 'Please select a primary sculpture material.'
            else:
                repute_val = float(repute)
                height_val = float(height)
                width_val = float(width)
                weight_val = float(weight)
                material_val = int(material)
                basePrice_val = float(basePrice)
                basePriceShipping_val = float(basePriceShipping)
                international_val = int(international)
                expressShipment_val = int(expressShipment)
                installments_val = int(installments)
                transport_val = int(transport)
                fragile_val = int(fragile)
                customer_val = int(customer)
                remote_val = int(remote)
                waiting_val = float(waiting)

                if not (0 <= repute_val <= 1):
                    error_message = 'Artist reputation score must be between 0.0 and 1.0.'
                elif height_val <= 0 or width_val <= 0 or weight_val <= 0:
                    error_message = 'Height, width, and weight must be positive numbers.'
                elif basePrice_val <= 0 or basePriceShipping_val <= 0:
                    error_message = 'Base price and shipping price must be positive numbers.'
                else:
                    df = pd.DataFrame([{
                        'Artist Reputation': repute_val,
                        'Height': height_val,
                        'Width': width_val,
                        'Weight': weight_val,
                        'Material': material_val,
                        'Price Of Sculpture': basePrice_val,
                        'Base Shipping Price': basePriceShipping_val,
                        'International': international_val,
                        'Express Shipment': expressShipment_val,
                        'Installation Included': installments_val,
                        'Transport': transport_val,
                        'Fragile': fragile_val,
                        'Customer Information': customer_val,
                        'Remote Location': remote_val,
                        'Waiting time': waiting_val
                    }])

                    model_path = os.path.join(os.path.dirname(__file__), 'Artist.pickle')
                    if os.path.exists(model_path):
                        with open(model_path, 'rb') as f:
                            loaded_model = pickle.load(f)
                        raw_pred = loaded_model.predict(df)[0]
                        res = round(float(raw_pred), 2)
                        
                        if is_ajax:
                            return JsonResponse({
                                'status': 'success',
                                'predicted_cost': res,
                                'artist_name': name,
                                'currency': 'USD'
                            })
                    else:
                        error_message = 'Trained model file (Artist.pickle) was not found on the server.'
                        if is_ajax:
                            return JsonResponse({'status': 'error', 'error_message': error_message}, status=500)

        except ValueError as e:
            error_message = f'Invalid number format detected: {str(e)}'
        except Exception as e:
            error_message = f'An error occurred during prediction: {str(e)}'

        if error_message and is_ajax:
            return JsonResponse({'status': 'error', 'error_message': error_message}, status=400)

    context = {
        'response': res,
        'error': error_message,
        'form_data': request.POST if request.method == 'POST' else {}
    }
    return render(request, 'index.html', context)
