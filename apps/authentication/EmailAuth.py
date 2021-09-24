# """This views for login auth usecase for login with email so that i can customize default username and password"""
# #i should use AUTHENTICATION_BACKENDS in settings to make it work

# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend


# class EmailBackEnd(ModelBackend):
#     def authenticate(self,username=None, password=None, **kwargs):
#         UserModel=get_user_model()
#         try:
#             user=UserModel.objects.get(email=username)#passing email instead of username
            
#         except UserModel.DoesNotExist:
#             return None
        
#         else:
#             if user.check_password(password):#if password is true then it returns user
#                 return user
            
#         return None
    
# """
# After this dont forget to register

# AUTHENTICATION_BACKENDS=['student_management_app.EmailBackEnd.EmailBackEnd'] in settings.py
# """