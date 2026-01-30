from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
# from .models import User
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from .forms import RegisterForm

User = get_user_model()

# ── Custom Base Admin for reusable fields ──
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ("uuid", "status", "is_deleted", "created_at", "updated_at")
    list_filter = ("status", "is_deleted")
    readonly_fields = ("uuid", "created_at", "updated_at")


# ── User Admin ──
@admin.register(User)
class UserAdmin(BaseModelAdmin, DjangoUserAdmin):
    add_form = RegisterForm
    model = User
    list_display = (
       "avatar_preview", "id", "username", "email", "is_staff", "is_active",
        "is_verified", "status", "created_at", "updated_at"
    )
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_active", "is_verified", "status", "is_deleted")
    readonly_fields = ("uuid", "created_at", "updated_at", "date_joined", "last_login","avatar_preview")

    fieldsets = DjangoUserAdmin.fieldsets + (
        (None, {"fields": ("phone_number", "avatar_preview", "avatar", "is_verified", "status", "is_deleted")}),
    )
    actions = ['soft_delete_users','restore_users']
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "is_active", "is_staff", "is_superuser"),
        }),
    )

    @admin.action(description="Soft delete selected users")
    def soft_delete_users(self, request, queryset):
        for obj in queryset:
            obj.is_deleted = True
            obj.save(update_fields=["is_deleted", "updated_at"])


    @admin.action(description="Restore selected users")
    def restore_users(self, request, queryset):
        for obj in queryset:
            obj.is_deleted = False
            obj.save(update_fields=["is_deleted", "updated_at"])

    
    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:50%; object-fit:cover;" />',
                obj.avatar.url
            )
        return "No Avatar"

    avatar_preview.short_description = "Avatar Preview"