from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
# user model을 admin패널에서 보고 싶다
# 데코레이터가admin.site.register(models.User, CustomUserAdmin) 과 같은 뜻
@admin.register(models.User)  # decorator는 이렇게 클래스 위에 있어야 작동함
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
