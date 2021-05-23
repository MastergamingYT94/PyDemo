from api.add import update
from django.urls import path
from ..add import add

urlpatterns = [
    path('<model>', add.add_data),
    path('<model>/<int:id>', update.update_data),
]
