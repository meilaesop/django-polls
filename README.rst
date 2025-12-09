=======================
meilaesop-django-polls
=======================

A Django app to conduct web-based polls. For each question,
visitors can choose between a fixed number of answers.

.. image:: https://img.shields.io/pypi/v/meilaesop-django-polls.svg
    :target: https://pypi.org/project/meilaesop-django-polls/
    :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/meilaesop-django-polls.svg
    :target: https://pypi.org/project/meilaesop-django-polls/
    :alt: Python Versions

.. image:: https://img.shields.io/pypi/djversions/meilaesop-django-polls.svg
    :target: https://pypi.org/project/meilaesop-django-polls/
    :alt: Django Versions

Installation
------------

Install from PyPI:

.. code-block:: bash

    pip install meilaesop-django-polls

Or install the latest development version:

.. code-block:: bash

    pip install git+https://github.com/meilaesop/django-polls.git

Quick Start
-----------

1. Add ``django_polls`` to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'django_polls',
    ]

2. Include the polls URLconf in your project ``urls.py``:

.. code-block:: python

    from django.urls import include, path

    urlpatterns = [
        # ...
        path('polls/', include('django_polls.urls')),
        # ...
    ]

3. Run migrations:

.. code-block:: bash

    python manage.py migrate

4. Start the development server and visit the admin to create a poll.

5. Visit the ``/polls/`` URL to participate in the poll.

Features
--------

- Create and manage polls through Django admin
- User-friendly voting interface
- Results display with charts
- Customizable templates
- Bootstrap 5 integration
- Responsive design

Requirements
------------

- Django >= 3.2, < 5.0
- Python >= 3.8

Documentation
-------------

Detailed documentation is in the "docs" directory.

License
-------

BSD 3-Clause License

Links
-----

- GitHub: https://github.com/meilaesop/django-polls
- PyPI: https://pypi.org/project/meilaesop-django-polls/
- Issues: https://github.com/meilaesop/django-polls/issues
