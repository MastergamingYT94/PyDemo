from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import SpecificationsResource
from PyCommerce.models import specifications


class IGetSpecifications(ABC):
    @abstractmethod
    def specifications():
        pass


class Specifications():
    def specifications(self, request):
        if request.method == 'GET':
            sanitizer = SpecificationsResource(
                specifications.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_specifications = Specifications().specifications
