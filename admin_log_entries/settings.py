from django.conf import settings

default_settings = {
    'has_module_permission_false': False,
}

ADMIN_LOG_ENTRIES_SETTINGS = {}


def compute_settings():
    for name, value in default_settings.items():
        ADMIN_LOG_ENTRIES_SETTINGS[name] = value

    if hasattr(settings, 'ADMIN_LOG_ENTRIES'):
        ADMIN_LOG_ENTRIES_SETTINGS.update(settings.ADMIN_LOG_ENTRIES)

compute_settings()
