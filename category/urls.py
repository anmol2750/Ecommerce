from django.urls import path
from . import views

# Application Name
app_name = 'category'

urlpatterns = [
    # Category List URL :
    path('', views.categoryListView, name = "category_list"),
    # Add Category URL :
    path('addcategory', views.categoryAddView, name = "category_add"),
    # Update Category URL :
    path('updatecategory/<int:id>', views.categoryUpdateView, name = "category_update"),
    # Delete Category URL :    
    path('deletecategory/<int:id>', views.categoryDeleteView, name = "category_delete"),
]