from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import SpecificationValueCountsResource
from PyCommerce.models import specificationValueCounts


class IGetSpecificationValueCounts(ABC):
    @abstractmethod
    def specification_value_counts():
        pass


class SpecificationValueCounts():
    def specification_value_counts(self, request):
        if request.method == 'GET':
            sanitizer = SpecificationValueCountsResource(
                specificationValueCounts.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_specification_value_counts = SpecificationValueCounts().specification_value_counts
