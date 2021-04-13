from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import CountriesResource
from PyCommerce.models import countries


class IGetCountries(ABC):
    @abstractmethod
    def countries():
        pass


class Countries():
    def countries(self, request):
        if request.method == 'GET':
            sanitizer = CountriesResource(countries.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_countries = Countries().countries
