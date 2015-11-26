from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render

from delivery.models import Route, PostedItem

from delivery.forms import RouteForm

from delivery.forms import PostedItemForm

from delivery.forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

# Use the login_required() decorator to ensure only those logged in can access the view.
#@login_required
#def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
 #   logout(request)

    # Take the user back to the homepage.
  #  return HttpResponseRedirect('/delivery/')

#@login_required
#def restricted(request):
 #   return HttpResponse("Since you're logged in, you can see this text!")




def add_route(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = RouteForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = RouteForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'delivery/add_route.html', {'form': form})

def add_item(request):
    item_list=PostedItem.objects.all()
    c_dict = {'items': item_list}
    # A HTTP POST?
    if request.method == 'POST':
        form = PostedItemForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = PostedItemForm()
  

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'delivery/add_item.html', {'form': form})


def index(request):
    return render(request, 'delivery/index.html')


def about(request):
    return render(request, 'delivery/about.html')


def routes(request):
    routes_list=Route.objects.all()
    if len(routes_list)<0:
        context_dict={'empty' : ""}
    else:  
        context_dict = {'routes': routes_list}
    return render(request, 'delivery/routes.html', context_dict)

def items(request):
    item_list=PostedItem.objects.all()
    context_dict = {'items': item_list}
    return render(request, 'delivery/items.html', context_dict)

def pending(request):
    item_list=PostedItem.objects.all()
    context_dict = {'items': item_list}
    return render(request, 'delivery/pending.html', context_dict)
