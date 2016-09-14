Hello - this project is looking for a new maintainer. Please open an issue if you'd like to help maintain.

Most pressing issue is to support modern python/django See [#6](https://github.com/burke-software/django-admin-export/issues/6)


django-admin-export
===================

Generic export to XLSX/HTML/CSV action for the Django admin interface.

Meant for fast and simple exports and lets you choose the data to export.

Features
--------
- Drop in application
- Traverse model relations recursively

django-admin-export is built with [django-report-utils](https://github.com/burke-software/django-report-utils).
For a a full query builder try using [django-report-builder](https://github.com/burke-software/django-report-builder).

Install
-------
1. ``pip install django-admin-export``
2. Add ``admin_export`` to INSTALLED_APPS
3. Add ``url(r'^admin_export/', include("admin_export.urls", namespace="admin_export")),`` to your project's urls.py

Usage
-----
Go to any admin page, select fields, then select the export to xls action. Then check off any fields you want to export.

Running tests
-------------

1. Acquire a checkout of the repository
2. ``pip install -e . -r requirements_test.txt``
3. ``py.test tests``

Or to run tests with all supported environments:

1. Acquire a checkout of the repository
2. Install tox with ``pip install tox``
3. ``tox``


Security
--------

This project assumes staff users are trusted. There may be ways for users to manipulate this project to get more data access than they should have.
