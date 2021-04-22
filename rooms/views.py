from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models, forms



class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


# pk = primary key // This is FBV
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


def search(request):
    form = forms.SearchForm()
    return render(request, "rooms/search.html", {"form": form})