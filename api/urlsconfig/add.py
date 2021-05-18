from django.urls import path
from ..add import add

urlpatterns = [
    path('<model>', add.add_data),
]
