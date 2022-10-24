%bcond_without tests

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:               python-flask-migrate
Version:            3.1.0
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
BuildRequires:      python3dist(sphinx)
BuildRequires:      make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
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
%py3_shebang_fix tests/app*.py


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
%if %{with tests}
env PYTHONPATH="${PYTHONPATH:-%{buildroot}%{python3_sitelib}}" \
    PYTHONDONTWRITEBYTECODE=1 \
    %{python3} -m unittest discover -v
%else
echo 'Tests are disabled'
%endif


%files -n python3-flask-migrate -f %{pyproject_files}


%files doc
%license LICENSE
%doc README.md
%if %{with doc_pdf}
%doc docs/_build/latex/Flask-Migrate.pdf
%endif


%changelog
%autochangelog
