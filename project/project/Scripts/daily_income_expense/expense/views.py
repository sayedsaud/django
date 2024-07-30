from django.shortcuts import render,redirect
from .models import Expense,expenseform
# Create your views here.
def add_expense(request):
    if request.method=='POST':
        f=expenseform(request.POST)
        f.save()
        return redirect('/')
    else:
        f=expenseform
        context={'form':f}
        return render(request,'add_expense.html',context)
    

def expense_list(request):
    uid=request.session.get('uid')
    #expl=expense.objects.all
    expl=Expense.objects.filter(user=uid)
    context={'expl':expl}
    return render(request,'exp_list.html',context)


def delete_exp(request,expid):
    exp1=Expense.objects.get(id=expid)
    exp1.delete()
    return redirect('/')