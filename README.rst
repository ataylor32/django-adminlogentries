========================
Django Admin Log Entries
========================

By default, ``django.contrib.admin``'s index shows the logged in user's 10 most
recent actions. This app provides a ``ModelAdmin`` for
``django.contrib.admin``'s ``LogEntry`` model (with everything except the list
disabled), allowing you to see every action taken by every user. The list can
be filtered, searched, and sorted, as you would expect of a ``ModelAdmin``.
This app is for Django 1.11+. It may work on older versions of Django, but it
has not been tested.

------------
Installation
------------

Step 1 of 2: Install the package
================================

.. code-block:: bash

    pip install django-adminlogentries

Step 2 of 2: Update "settings.py"
=================================

Add ``admin_log_entries`` to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'admin_log_entries',
        ...
    )

-------------
Configuration
-------------

By default, the ``has_module_permission`` method of this app's ``ModelAdmin``
retains Django's default behavior. If you want it to return ``False`` instead,
add the following to your "settings.py":

.. code-block:: python

    ADMIN_LOG_ENTRIES = {
        'has_module_permission_false': True,
    }

This will prevent "Log entries" from being displayed on the admin index page
and will also prevent accessing the ``admin`` module's index page.
