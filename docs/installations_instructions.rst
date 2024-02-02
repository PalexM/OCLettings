Installation Instructions
=========================

Prerequisites
-------------

- A GitHub account with read access to this repository.
- Git CLI.
- SQLite3 CLI.
- Python interpreter, version 3.6 or higher.

In the rest of the documentation on local development, it is assumed that your OS shell's `python` command executes the above Python interpreter (unless a virtual environment is activated).

macOS / Linux
-------------

Clone the Repository
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cd /path/to/put/project/in
    git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git

Create the Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    python -m venv venv
    apt-get install python3-venv  # If the previous step fails with a package not found error on Ubuntu
    source venv/bin/activate
    # Confirm that `python` now runs the Python interpreter in the virtual environment
    which python
    python --version  # Confirm Python version is 3.6 or higher
    which pip  # Confirm `pip` runs the pip executable in the virtual environment
    deactivate  # To deactivate the environment
