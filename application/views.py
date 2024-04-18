from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from application.tasks import process_csv_file_async, complete_postal_code_information_async
import logging
import asyncio

logger = logging.getLogger(__name__)

 
@csrf_exempt
async def upload_csv(request):
    if request.method == 'POST':
        try:
            csv_file = request.FILES['csv_file']
            csv_content = csv_file.read().decode('utf-8')
            asyncio.create_task(process_csv_file_async(csv_content))
            logger.info("Archivo CSV cargado correctamente.")
            return JsonResponse({'message': 'Archivo CSV recibido y procesando en segundo plano'})
        except KeyError:
            return JsonResponse({'error': 'No se adjuntó ningún archivo CSV'}, status=400)
        except Exception as e:
            logger.error(f"Error al procesar el archivo CSV: {e}")
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Se esperaba un archivo CSV'}, status=400)


@csrf_exempt
async def complete_postal_code(request):
    if request.method == 'GET':
        try:
            asyncio.create_task(complete_postal_code_information_async())
            return JsonResponse({'message': 'Tarea para completar informacion de codigos postales iniciada'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Se esperaba una peticion de tipo GET'}, status=400)
