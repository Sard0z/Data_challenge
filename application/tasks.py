from infrastructure.repositories import DjangoCoordinateRepository
from infrastructure.services import PostcodesServiceImpl
from .use_cases import ProcessFileCSVUseCase, CompletePostalCodeInformationUseCase
from .exceptions import CSVFileError
from django.http import JsonResponse
import asyncio



async def process_csv_file_async(csv_content):
    try:
        coordinate_repository = DjangoCoordinateRepository()
        post_code_service = PostcodesServiceImpl(api_url='https://api.postcodes.io')
        process_file_csv_use_case = ProcessFileCSVUseCase(coordinate_repository, post_code_service)
        await asyncio.sleep(1)
        await process_file_csv_use_case.process_csv_file(file=csv_content)
    except CSVFileError as e:
        raise e
    
    
async def complete_postal_code_information_async():
    try:
        coordinate_repository = DjangoCoordinateRepository()
        post_code_service = PostcodesServiceImpl(api_url='https://api.postcodes.io')
        use_case = CompletePostalCodeInformationUseCase(coordinate_repository, post_code_service)
        await asyncio.sleep(1)
        await use_case.complete_postal_code_information()
        return JsonResponse({'message': 'Tarea para completar informacion de codigos postales iniciada'})

    except Exception as e:
        raise e