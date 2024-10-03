from django.urls import path
from .views import home,add,deleteShow,update,profile,success,delete,updateEmp

# port address is 8001
# creating a list of urls in employe management system app
urlpatterns = [
    path("",home,name='home'),
    path("add/",add,name='add'),
    path("update/",update,name='update'),
    path("delete/",deleteShow,name='delete'),
    path("profile/",profile,name='profile'),
    path("successful/",success, name='successful'),
    path("deleteEmp/<int:Emp_id>",delete,name='deleteEmp'),
    path("updateEmp/<int:Emp_id>",updateEmp, name='updateEmp'),
]