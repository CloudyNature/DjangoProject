from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    ROLE_CHOICES = {
        'admin': 'Admin',
        'manager': 'Manager',
        'employee': 'Employee',
    }
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Company(models.Model):
    company_code = models.CharField(max_length=20)
    title = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    industry = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Branch(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Department(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Employee(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    emp_id = models.IntegerField()
    STATUS_CHOICES = {
        'Part-time': 'Part-time',
        'Full-time': 'Full-time',
    }
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Part-time')
    date_of_joining = models.DateField()
    date_of_birth = models.DateField()
    TYPE_CHOICES = {
        'Permanent': 'Permanent',
        'Contract': 'Contract',
    }
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, default='Contract')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class EmployeeProfile(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    mobile = models.IntegerField()
    country = models.CharField(max_length=50)
    emergency_contact = models.IntegerField()
    employee_photo = models.ImageField(upload_to='employee_photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    worked_time = models.IntegerField()
    break_time = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee.user.username

class AttendenceLog(models.Model):
    STATUS_CHOICES = {
        'Punch In' : 'Punch In',
        'Punch Out' : 'Punch Out',
        'Break In': 'Break In',
        'Break Out': 'Break Out',
    }

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.attendance.employee.user.username

class LeaveType(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Leave(models.Model):
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=250)
    APPROVAL_CHOICES = {
        'Pending': 'Pending',
        'Approved' : 'Approved',
        'Rejected': 'Rejected'
    }

    approval_status = models.CharField(max_length=10, choices=APPROVAL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.leave_type.title
