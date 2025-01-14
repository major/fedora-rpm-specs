Name:               python-flask-migrate
Version:            4.1.0
Release:            %autorelease
Summary:            SQLAlchemy database migrations for Flask applications using Alembic

# SPDX
License:            MIT
URL:                https://github.com/miguelgrinberg/Flask-Migrate
Source:             %{url}/archive/v%{version}/Flask-Migrate-%{version}.tar.gz

BuildArch:          noarch

# For %%py3_shebang_fix in %%prep, before generated BuildRequires are ready
BuildRequires:      pyproject-rpm-macros

BuildSystem:            pyproject
BuildOption(install):   -l flask_migrate
# Both flask_migrate/templates/aioflask/env.py and
# flask_migrate/templates/flask/env.py are meant for execution via alembic;
# importing them directly fails with:
#   AttributeError: module 'alembic.context' has no attribute 'config'
BuildOption(check):     -e flask_migrate.templates.*flask.env

# We do not use %%pyproject_buildrequires -t and %%tox because tox.ini
# explicitly runs “pip install.” We do not use %%pyproject_buildrequires -x dev
# because this brings in tox and at least one linter (flake8).
BuildRequires:      %{py3_dist pytest}

%global common_description %{expand:
SQLAlchemy database migrations for Flask applications using Alembic.}

%description %{common_description}


%package -n python3-flask-migrate
Summary:            %{summary}

# We stopped building PDF documentation and removed the -doc subpackage for
# Fedora 42; this can be removed after Fedora 44 reaches end of life.
Obsoletes:          python-flask-migrate-doc < 4.1.0-3

%description -n python3-flask-migrate %{common_description}


%prep -a
# Fix shebangs that use /bin/env and unversioned Python
%py3_shebang_fix tests/app.py tests/app_multidb.py


%check -a
# See tox.ini:
%pytest -p no:logging


%files -n python3-flask-migrate -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
