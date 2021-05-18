from api.get import get
from django.urls import path


urlpatterns = [
    path('<model>/<id>', get.get_data),
]
