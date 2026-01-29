from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

# ── Custom Base Admin for reusable fields ──
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ("id", "uuid", "status", "is_deleted", "created_at", "updated_at")
    list_filter = ("status", "is_deleted")
    readonly_fields = ("uuid", "created_at", "updated_at")


# ── User Admin ──
@admin.register(User)
class UserAdmin(DjangoUserAdmin, BaseModelAdmin):
    model = User
    list_display = (
        "id", "username", "email", "is_staff", "is_active",
        "is_verified", "status", "created_at", "updated_at"
    )
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_active", "is_verified", "status", "is_deleted")
    readonly_fields = ("uuid", "created_at", "updated_at", "date_joined", "last_login")

    fieldsets = DjangoUserAdmin.fieldsets + (
        (None, {"fields": ("phone_number", "avatar", "is_verified", "status", "is_deleted")}),
    )
    actions = ['soft_delete_users','restore_users']
    


    def soft_delete_users(self, request, queryset):
        queryset.update(is_deleted=True)
    soft_delete_users.short_description = "Soft delete selected users"

    def restore_users(self, request, queryset):
        queryset.update(is_deleted=False)
    restore_users.short_description = "Restore selected users"
