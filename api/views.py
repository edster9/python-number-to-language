from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from api.utils import number_to_english, number_to_spanish


# helper function for retrieving the 'number' param from the request (get/post)
def number_from_request(request: Request) -> int:
    number = None

    # retrieve the 'number' data parameter passed in based on request method
    if request.method == 'GET':
        number = request.query_params.get('number')
    elif request.method == 'POST':
        number = request.data.get('number')

    # is the number parameter supplied?
    if not number:
        raise AssertionError('missing data parameter - number')

    # is the number parameter an actual number?
    if isinstance(number, str):
        if not number.isnumeric():
            raise AssertionError(
                f'invalid parameter supplied - number={number} - must be a valid integer')

        # is the number parameter too large
        if len(number) > 15:
            raise AssertionError(
                f'invalid parameter supplied - number={number} - is too large')

    elif not isinstance(number, int):
        raise AssertionError(
            f'invalid parameter supplied - number={number} - must be a valid integer')

    return int(number)


# '/num_to_english' endpoint
@api_view(['GET', 'POST'])
def num_to_english(request: Request):
    try:
        result = {'status': 'ok', 'num_in_english': number_to_english(
            number_from_request(request))}

        return Response(result)
    except AssertionError as e:
        return Response({'status': 'error', 'error': str(e)})


# '/num_to_spanish' endpoint
@api_view(['GET', 'POST'])
def num_to_spanish(request: Request):
    try:
        result = {'status': 'ok', 'num_in_spanish': number_to_spanish(
            number_from_request(request))}

        return Response(result)
    except AssertionError as e:
        return Response({'status': 'error', 'error': str(e)})
