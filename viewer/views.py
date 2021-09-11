import base64
from django.http.response import JsonResponse,HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from apps.user.models import Article






@xframe_options_exempt
def iframe(request):
    print("sadksdajkdasjkdsjk")
    return render(request,'viewer.html')

@xframe_options_exempt
def annotation_iframe(request):
    return render(request,'pdf_annotation/index.html')


@xframe_options_exempt
def annotation2_iframe(request):
    return render(request,'pdf_annotation2/index.html')

@csrf_exempt
def receive_pdf(request):
    try:
        print("in request.files")
    except:
        print("NOT IN FILES")
    
    # print('item \t type \t size')
    # for item in list(request.FILES.items()):
    #     print(item[1],'\t' ,item[1].content_type,'\t' , item[1].size)

    files = list(request.FILES.items())
    
    file_to_upload = files[0][1]
    file_to_upload._set_name(request.POST['fileName']+'.pdf')
    print(request.POST['userId'])
    user = Article.objects.get(user__pk=request.POST['userId'])
    article = Article.objects.get(user=user)                                   
    article.file = file_to_upload
    article.save()

    return JsonResponse({'a':'b'})
