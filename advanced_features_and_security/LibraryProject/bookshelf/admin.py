from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from .models import Book

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book  # Replace with your app and model

def setup_groups_and_permissions():
    # Create groups
    librarian_group, _ = Group.objects.get_or_create(name="Librarians")
    member_group, _ = Group.objects.get_or_create(name="Members")

    # Define permissions
    book_content_type = ContentType.objects.get_for_model(Book)

    can_add_book = Permission.objects.get(
        codename="can_add_book", content_type=book_content_type
    )
    can_change_book = Permission.objects.get(
        codename="can_change_book", content_type=book_content_type
    )
    can_delete_book = Permission.objects.get(
        codename="can_delete_book", content_type=book_content_type
    )

    # Assign permissions to groups
    librarian_group.permissions.add(can_add_book, can_change_book, can_delete_book)

    print("Groups and permissions setup completed.")


user = User.objects.get(username="librarian_user")  # Replace with actual username
librarian_group = Group.objects.get(name="Librarians")
librarian_group.user_set.add(user)



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)


admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ('title', 'author')
    list_filter = ('publication_year')