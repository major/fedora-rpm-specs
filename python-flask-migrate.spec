# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:               python-flask-migrate
Version:            4.0.1
Release:            %autorelease
Summary:            SQLAlchemy database migrations for Flask applications using Alembic

# SPDX
License:            MIT
URL:                https://github.com/miguelgrinberg/Flask-Migrate
Source0:            %{url}/archive/v%{version}/Flask-Migrate-%{version}.tar.gz
BuildArch:          noarch

BuildRequires:      python3-devel

# Documentation
%if %{with doc_pdf}
BuildRequires:      make
BuildRequires:      latexmk
BuildRequires:      python3dist(sphinx)
BuildRequires:      python3-sphinx-latex
%endif

%global common_description %{expand:
SQLAlchemy database migrations for Flask applications using Alembic.}

%description %{common_description}


%package -n python3-flask-migrate
Summary:            %{summary}

%description -n python3-flask-migrate %{common_description}


%package doc
Summary:            Documentation for Flask-Migrate

%description doc
Documentation for Flask-Migrate.


%prep
%autosetup -n Flask-Migrate-%{version}
# Fix shebangs that use /bin/env and unversioned Python
%py3_shebang_fix tests/app.py tests/app_multidb.py


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel
%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files flask_migrate


%check
%tox


%files -n python3-flask-migrate -f %{pyproject_files}


%files doc
%license LICENSE
%doc README.md
%if %{with doc_pdf}
%doc docs/_build/latex/Flask-Migrate.pdf
%endif


%changelog
%autochangelog
