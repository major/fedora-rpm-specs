# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc 1

Name:               python-flask-migrate
Version:            4.0.7
Release:            %autorelease
Summary:            SQLAlchemy database migrations for Flask applications using Alembic

# SPDX
License:            MIT
URL:                https://github.com/miguelgrinberg/Flask-Migrate
Source:             %{url}/archive/v%{version}/Flask-Migrate-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel

%if %{with doc}
BuildRequires:      make
BuildRequires:      latexmk
BuildRequires:      %{py3_dist sphinx}
BuildRequires:      python3-sphinx-latex
%endif

# Tests
# We do not use %%pyproject_buildrequires -t and %%tox because tox.ini
# explicitly runs “pip install.”
BuildRequires:      %{py3_dist pytest}

%global common_description %{expand:
SQLAlchemy database migrations for Flask applications using Alembic.}

%description %{common_description}


%package -n python3-flask-migrate
Summary:            %{summary}

%description -n python3-flask-migrate %{common_description}


%if %{with doc}
%package doc
Summary:            Documentation for Flask-Migrate

%description doc
Documentation for Flask-Migrate.
%endif


%prep
%autosetup -n Flask-Migrate-%{version}
# Fix shebangs that use /bin/env and unversioned Python
%py3_shebang_fix tests/app.py tests/app_multidb.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%if %{with doc}
%make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l flask_migrate


%check
# See tox.ini:
%pytest -p no:logging


%files -n python3-flask-migrate -f %{pyproject_files}
%if %{without doc}
%doc README.md
%endif


%if %{with doc}
%files doc
%license LICENSE
%doc README.md
%doc docs/_build/latex/Flask-Migrate.pdf
%endif


%changelog
%autochangelog
