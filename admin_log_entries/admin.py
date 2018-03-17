from django.conf import settings
from django.contrib import admin
from django.contrib.admin.models import ADDITION, CHANGE, DELETION, LogEntry
from django.core.exceptions import PermissionDenied
from django.template.defaultfilters import capfirst
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from .settings import ADMIN_LOG_ENTRIES_SETTINGS


class ActionListFilter(admin.SimpleListFilter):
    title = _('action')
    parameter_name = 'action_flag'

    def lookups(self, request, model_admin):
        return (
            (ADDITION, _('Addition')),
            (CHANGE, _('Change')),
            (DELETION, _('Deletion')),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(
                action_flag=self.value(),
            )


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    actions = None

    date_hierarchy = 'action_time'

    list_display = (
        'action_time',
        'action',
        'user',
    )

    list_display_links = None

    list_filter = (
        ActionListFilter,
        ('user', admin.RelatedOnlyFieldListFilter),
    )

    list_select_related = (
        'user',
        'content_type',
    )

    search_fields = (
        'action_time',
        'content_type__model',
        'object_repr',
        'change_message',
    )

    def action(self, entry):
        if entry.is_deletion() or not entry.get_admin_url():
            link_or_text = entry
        else:
            link_or_text = format_html(
                u'<a href="{}">{}</a>',
                entry.get_admin_url(),
                entry,
            )

        if entry.content_type:
            content_type = capfirst(entry.content_type)
        else:
            content_type = _('Unknown content')

        return format_html(
            u'{}<br><span class="mini quiet">{}</span>',
            link_or_text,
            content_type,
        )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        raise PermissionDenied

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        if ADMIN_LOG_ENTRIES_SETTINGS['has_module_permission_false']:
            admin_app = 'default'

            for admin_app_to_check in (
                'grappelli',
                'suit',
            ):
                if admin_app_to_check in settings.INSTALLED_APPS:
                    admin_app = admin_app_to_check
                    break

            extra_context.update({
                'has_module_permission_false': True,
                'admin_app': admin_app,
            })

        extra_context['title'] = 'Log entries'
        return super(LogEntryAdmin, self).changelist_view(
            request, extra_context=extra_context,
        )

    def history_view(self, request, object_id, extra_context=None):
        raise PermissionDenied

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_module_permission(self, request):
        if ADMIN_LOG_ENTRIES_SETTINGS['has_module_permission_false']:
            return False
        return super(LogEntryAdmin, self).has_module_permission(request)
