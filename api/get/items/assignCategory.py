from PyCommerce.models import categories
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.encrypt import encrypt


class IAssignCategories(ABC):
    @abstractmethod
    def assign_categories():
        pass


class AssignCategories():
    def assign_categories(self, request, MainCategory):
        if request.method == 'GET':
            data = categories.objects.filter(
                Level=2, MainCategoryId=MainCategory).values('id').first()
            return JsonResponse(data, safe=False)


assign_categories = AssignCategories().assign_categories
