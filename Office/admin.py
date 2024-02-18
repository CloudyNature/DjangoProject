from django.contrib import admin
from .models import User, Company, Branch, Department, Employee, EmployeeProfile, Attendance, AttendenceLog, LeaveType, Leave

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'username', 'password',
                    'role', 'created_at', 'updated_at')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_code','title', 'address', 'phone_number', 'email', 'industry',
                    'sector', 'created_at', 'updated_at')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'title', 'address', 'created_at', 'updated_at')


@admin.register(Department)
class DeparmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'branch', 'created_at', 'updated_at')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('branch', 'user', 'department', 'emp_id', 'status',
                    'date_of_joining', 'date_of_birth', 'type', 'created_at', 'updated_at')


@admin.register(EmployeeProfile)
class EmployeeProfile(admin.ModelAdmin):
    list_display = ('employee','full_name','address','mobile','country',
                    'emergency_contact','employee_photo','created_at', 'updated_at')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'worked_time', 'break_time', 'latitude', 'longitude',
                    'date', 'created_at', 'updated_at')

@admin.register(AttendenceLog)
class AttendenceLogAdmin(admin.ModelAdmin):
    list_display = ('status','attendance', 'created_at', 'updated_at')

@admin.register(LeaveType)
class LeaveTypeAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'created_at', 'updated_at')

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('leave_type', 'employee', 'start_date', 'end_date', 'reason',
                    'approval_status', 'created_at', 'updated_at')
