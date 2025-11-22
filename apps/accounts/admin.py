from django.contrib import admin
from apps.accounts.models import User, UserJob, UserScienceTip, UserDegree
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": ("email", "password1", "password2", "username"),
                },
            ),
        )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email" , "phone", "birth",  "photo")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "status",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    'job',
                    'science_tip',
                    'degree',
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "phone", "job","status", "is_staff")
    list_editable = ("status", )

# User modelini inline ko‘rinishda chiqarish (UserJob sahifasida)
class UserInline(admin.TabularInline):
    model = User
    extra = 0
    fields = ['username', 'email', 'status', 'favourites_count', 'favourites_books']
    readonly_fields = ['username', 'email', 'status', 'favourites_count', 'favourites_books']

    def favourites_count(self, obj):
        return obj.favourites.count()
    favourites_count.short_description = "Likes"

    def favourites_books(self, obj):
        return "\n".join([f.resource.title for f in obj.favourites.select_related('resource').all()])
    favourites_books.short_description = "Favourite Books"


# UserJob admini
@admin.register(UserJob)
class UserJobAdmin(admin.ModelAdmin):
    list_display = ['name', 'users_job__count']
    inlines = [UserInline]

    def users_job__count(self, obj):
        return obj.users_job.count()

@admin.register(UserScienceTip)
class UserScienceTipAdmin(admin.ModelAdmin):
    list_display = ['name', 'users_science_tip__count']
    inlines = [UserInline]

    def users_science_tip__count(self, obj):
        return obj.users_science_tip.count()

@admin.register(UserDegree)
class UserDegreeAdmin(admin.ModelAdmin):
    list_display = ['name', 'users_degree__count']
    inlines = [UserInline]

    def users_degree__count(self, obj):
        return obj.users_degree.count()


