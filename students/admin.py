from django.contrib import admin
from django.db.models import QuerySet
from django.utils.safestring import mark_safe

from students.models import (Student, Group, Incentives, SpecialistRecomendations,
                             WorkWithParents, AntisocialBehavior, IndividualWork)
from user.models import User



class AllStudents(admin.TabularInline):
    model = Student
    extra = 1

class AllIncentives(admin.TabularInline):
    model = Student.incentives.through
    extra = 1
    def __str__(self):
        return f'{self.model._meta.verbose_name}'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['group_number', 'get_html_photo', 'last_name', 'first_name', 'otchestvo']
    list_display_links = ['last_name']
    list_editable = ['first_name', 'otchestvo', 'group_number']
    readonly_fields = ['get_html_photo']
    ordering = ['group_number', 'last_name', 'first_name']
    exclude = []
    list_per_page = 30
    actions = ['set_group']
    search_fields = ['group_number__group_number' ,'last_name', 'first_name', 'otchestvo']
    list_filter = ['group_number']
    inlines = [AllIncentives]
    @admin.action(description='Установить группу ученикам')
    def set_group(self, request, qs: QuerySet):
        selected_group = request.POST.get(
            'group_number')
        if selected_group:
            count_updated = qs.update(group_number=selected_group)

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100px>")

    get_html_photo.short_description = 'Фотография'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_number']
    ordering = ['group_number']
    list_per_page = 30
    search_fields = ['group_number']
    inlines = [AllStudents]



@admin.register(Incentives)
class IncentivesAdmin(admin.ModelAdmin):
    list_display = ['date', 'achievements', 'form_of_incentives']
    ordering = ['date']
    list_per_page = 30
    search_fields = ['date']
    inlines = [AllIncentives]


@admin.register(AntisocialBehavior)
class AntiSocialBehaviorAdmin(admin.ModelAdmin):
    list_display = ['date', 'character', 'meri', 'result']
    ordering = ['date', 'character', 'meri', 'result']
    list_per_page = 30
    search_fields = ['date']


@admin.register(SpecialistRecomendations    )
class SpecialistRecommendationsAdmin(admin.ModelAdmin):
    list_display = ['recomendations', 'result']
    list_per_page = 30
    search_fields = ['recomendations', 'result']


@admin.register(IndividualWork)
class IndividualWorkAdmin(admin.ModelAdmin):
    list_display = ['date', 'content', 'result']
    list_per_page = 30
    search_fields = ['date', 'content', 'result']


@admin.register(WorkWithParents)
class WorkWithParentsAdmin(admin.ModelAdmin):
    list_display = ['date', 'content', 'result']
    list_per_page = 30
    search_fields = ['date', 'content', 'result']
