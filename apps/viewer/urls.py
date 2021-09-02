from django.urls import path
from .views import iframe, annotation_iframe,annotation2_iframe,receive_pdf

urlpatterns = [
    path('viewer.html/', iframe, name="viewer"),
      path('pdf_annotation/index.html/', annotation_iframe, name="annotation-viewer"),
    path('pdf_annotation2/index.html/', annotation2_iframe, name="annotation2-viewer"),
    path('pdf_annotation2/index.html/ajax/receivepdf', receive_pdf, name='receivepdf')
]

app_name = 'viewer'