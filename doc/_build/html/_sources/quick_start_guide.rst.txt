Quick Start Guide
=================

Local Development
-----------------

### macOS / Linux

Running the Site
~~~~~~~~~~~~~~~~

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    source venv/bin/activate
    pip install --requirement requirements.txt
    python manage.py runserver

Navigate to `http://localhost:8000` in a web browser to confirm the site is working and navigable (you should see several profiles and listings).

Linting
~~~~~~~

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    source venv/bin/activate
    flake8

Unit Tests
~~~~~~~~~~

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    source venv/bin/activate
    pytest

### Windows

Use PowerShell for the above steps, with the following modifications:

- Activate the virtual environment using `.\venv\Scripts\Activate.ps1`.
- Replace `which <command>` with `(Get-Command <command>).Path`.