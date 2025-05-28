from django.shortcuts import render

def group_queryset(n,queryset):
    result = []
    temp = []

    for q in queryset:
        temp.append(q)
        if len(temp) == n:
            result.append(temp)
            temp = []
        return result
    
def index(request):
    return render(request,'index.html')