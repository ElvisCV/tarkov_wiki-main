from django.views.generic import ListView
from .models import Weapon

class WeaponListView(ListView):
    model = Weapon
    template_name = 'weapons/weapon_list.html'
    context_object_name = 'weapons'
    paginate_by = 10  # 10 registros por página
    
    def get_queryset(self):
        return Weapon.objects.all().order_by('-created')