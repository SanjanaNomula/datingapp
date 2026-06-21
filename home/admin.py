from django import forms
from django.contrib import admin
from .models import Profile, Question, Option, UserAnswer, RoomRequest, Conversation


# ✅ Inline options inside Question admin
class OptionInline(admin.TabularInline):  # or admin.StackedInline
    model = Option
    extra = 2  # show 2 blank options by default


class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        verify = {'verification_image', 'verification_status', 'is_face_verified'}
        for field_name in self.fields:
            if field_name not in verify:
                self.fields[field_name].required = False


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ('name', 'user', 'age', 'gender', 'campus', 'clg_year', 'verification_status', 'is_face_verified')
    search_fields = ('name', 'user__username', 'campus')
    list_filter = ('campus', 'gender', 'clg_year', 'looking_for', 'verification_status')
    fieldsets = (
        ('Verification', {
            'fields': ('verification_image', 'verification_status', 'is_face_verified'),
            'classes': ('wide',),
        }),
        ('Profile Info', {
            'fields': ('name', 'gender', 'profile_pic', 'age', 'clg_year', 'campus', 'course',
                       'living_place', 'native_place', 'languages', 'mother_tongues',
                       'bio', 'liked_songs', 'liked_movies', 'fav_shows', 'interest_tags',
                       'looking_for', 'pref_age_min', 'pref_age_max', 'pref_gender',
                       'pref_languages', 'pref_campus', 'is_banned', 'is_discoverable'),
        }),
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text",)
    inlines = [OptionInline]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ("text", "question")


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "option")
    list_filter = ("question", "option", "user")


@admin.register(RoomRequest)
class RoomRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'campus', 'min_rent', 'max_rent', 'preferred_room_type', 'is_active', 'created_at')
    list_filter = ('campus', 'preferred_room_type', 'is_active')
    search_fields = ('title', 'user__username', 'looking_near')


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'source', 'listing_id', 'request_id', 'created_at')
    list_filter = ('source',)
    search_fields = ('user1__username', 'user2__username')

