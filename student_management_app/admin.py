from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser, AdminHOD, Courses, Subjects, Students, Attendance, AttendanceReport, LeaveReportStudent, FeedBackStudent, NotificationStudent

# Register your models here. 
class UserModel(UserAdmin): 
	pass


admin.site.register(CustomUser, UserModel) 

admin.site.register(AdminHOD) 
admin.site.register(Courses) 
admin.site.register(Subjects) 
admin.site.register(Students) 
admin.site.register(Attendance) 
admin.site.register(AttendanceReport) 
admin.site.register(LeaveReportStudent) 
admin.site.register(FeedBackStudent) 
admin.site.register(NotificationStudent) 
