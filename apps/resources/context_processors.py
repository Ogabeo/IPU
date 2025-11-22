from apps.home.models import MeyoriyHujjat, TalimShakli, Fan, Worker
def categories(request):

    context = {
        "xodimlar" : Worker.objects.all(),
        "kafedra_mudiri" : Worker.objects.first(),
        "fanlar":Fan.objects.all(),
        "meyoriy_hujjatlar" : MeyoriyHujjat.objects.all(),
    }
    return context


