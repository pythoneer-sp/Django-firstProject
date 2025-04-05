from django.shortcuts import render
from .models import IITPStudent, Store
from django.shortcuts import get_object_or_404
from .forms import IITPStudentForm

# Create your views here.
def allapp(request):
    students = IITPStudent.objects.all()
    return render(request, 'firstapp/allapp.html', {'student': students})

def student_details(request, student_id):
    student = get_object_or_404(IITPStudent, pk=student_id)  #pk is primary key
    return render(request, 'firstapp/student_details.html', {'students': student})

def store_view(request):
    stores = None
    if request.method == 'POST':
        form = IITPStudentForm(request.POST)
        if form.is_valid():
            item_s = form.cleaned_data['item_s']
            stores = Store.objects.filter(items=item_s)
    else:
        form = IITPStudentForm()

    return render(request, 'firstapp/Store_forms.html', {'form':form , 'stores':stores})