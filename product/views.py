from django.shortcuts import render
from . forms import FromResisters
# Create your views here.
def product(request):
    frm = FromResisters()
    frm.order_fields(field_order=['fast_name','last_name','email','batch'])
    return render(request,'contact/contacts.html',{'froms': frm})
    
    