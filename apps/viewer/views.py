from student_management_app.models import Student
from school_apps.exam.models import AnswerSheet
from django.http.response import JsonResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
import base64
from school_apps.courses.models import Exams

@xframe_options_exempt
def iframe(request):
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
        # print(list(request.FILES.items()))
    except:
        print("NOT IN FILES")
    
    # print('item \t type \t size')
    # for item in list(request.FILES.items()):
    #     print(item[1],'\t' ,item[1].content_type,'\t' , item[1].size)

    files = list(request.FILES.items())
    # print(files)
    # print(files[0][1])
    
    file_to_upload = files[0][1]
    file_to_upload._set_name(request.POST['fileName']+'.pdf')

    answer_object = AnswerSheet.objects.get(student=Student.objects.get(student_user__username=request.POST['studentId']),
                                            exam=Exams.objects.get(exam_id=request.POST['examId']))
    # print(answer_object)
    # print(request.POST['studentId'])
    # print(request.POST['examId'])

    answer_object.answer_upload = file_to_upload
    answer_object.save()

    return JsonResponse({'a':'b'})
