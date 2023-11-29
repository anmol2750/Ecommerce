from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from . import constants

# Category List View :
def categoryListView(request):
    category = Category.objects.filter(is_deleted = 0)
    
    context = {
        'category'     : category,
        
        # Constant Rendering to Template. 
        'CATEGORY'     : constants.CategoryListConstants.CATEGORY,
        'TOTAL_VENDOR' : constants.CategoryListConstants.TOTAL_VENDOR,
        'ACTIVE'       : constants.CategoryListConstants.ACTIVE,
        'INACTIVE'     : constants.CategoryListConstants.INACTIVE,
        'ADD_CATEGORY' : constants.ADD_CATEGORY,
        'RESET'        : constants.CategoryListConstants.RESET,
        'ID'           : constants.CategoryListConstants.ID,
        'DATE_JOINED'  : constants.CategoryListConstants.DATE_JOINED,
        'CATEGORY_NAME': constants.CATEGORY_NAME,
        'ACTION'       : constants.CategoryListConstants.ACTION,
        'UPDATE'       : constants.CategoryListConstants.UPDATE,
        'DELETE'       : constants.CategoryListConstants.DELETE
    }
    
    return render(request, constants.categoryListURL, context) # Rendering to Category List.


# Category Add View :
def categoryAddView(request):
    if request.method == 'POST':
        category = request.POST['name'] 
            
        existing_category = Category.objects.filter(name = category, is_deleted = True).first()
        
        if existing_category:
            existing_category.is_deleted = False
            existing_category.save()
        else:
            category = Category.objects.create(name=category) 
        return redirect(constants.categoryListURLNAME)     # Redirect to Category List. 
    
    context = {
        # Constant Rendering to Template. 
        'ADD_CATEGORY'          : constants.ADD_CATEGORY,
        'CATEGORY_NAME'         : constants.CATEGORY_NAME,
        'CATEGORY_INFO_MESSAGE' : constants.CategoryAddConstants.CATEGORY_INFO_MESSAGE,
        'CANCEL'                : constants.CANCEL, 
    }

    return render(request, constants.addCategoryURL, context)  # Rendering to Add Category.


# Category Update View :
def categoryUpdateView(request, id):
    category = get_object_or_404(Category, pk = id)
    if request.method == "POST":
        category = Category.objects.update_or_create(
            pk = id,
            defaults = {
                "name": request.POST["name"],
            },
        )
        return redirect(constants.categoryListURLNAME)
    context = {
        'category'        : category,
        
        # Constant Rendering to Template. 
        'UPDATE_CATEGORY' : constants.CategoryUpdateConstants.UPDATE_CATEGORY,
        'CATEGORY_NAME'   : constants.CATEGORY_NAME,
        'CANCEL'          : constants.CANCEL, 
    }
    return render(request, constants.updateCategoryURL, context)   # Rendering to Update Category. 


# Category Delete View :
def categoryDeleteView(request, id):
    category = Category.objects.get(pk = id)
    category.is_deleted = True
    category.save()
    return redirect(constants.categoryListURLNAME)    # Redirect to Category List.