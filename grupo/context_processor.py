
from .grupo import Grupo



def cantidad_total_grupo(request):
    total=0
    if request.user.is_authenticated:
        for key, values in request.session["grupo"].items():
            total=total+(int(values["valor"])*values["valor"])
    return {"cantidad_total_grupo":total}