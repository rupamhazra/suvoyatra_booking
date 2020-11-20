from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import *
from users.forms import CustomUserCreationForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
	model = Users
	add_form = CustomUserCreationForm

	fieldsets = (
		*UserAdmin.fieldsets,
		(
			'Other Details',
			{
				'fields':(
					'name',
                    'mobile',
                    'profile_img',
                    'change_pass',
                    'password_to_know',
                    'street_address',
                    'zip_code',
                    'city',
                    'created_by',
                    'created_at',
                    'updated_at',
                    'updated_by'
				)
			}
		)
	)

@admin.register(Users)
class Users(CustomUserAdmin):
    list_display = ['username','first_name','last_name','is_active']
    search_fields = ('username',)


#admin.site.register(User)