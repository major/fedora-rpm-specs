%global pypi_name pytest-django

Name:           python-%{pypi_name}
Version:        4.12.0
Release:        %autorelease
Summary:        A Django plugin for pytest

License:        BSD-3-Clause
URL:            https://pytest-django.readthedocs.io/
Source:         %{pypi_source pytest_django}
# temporarily lower pytest requirement for self-test, bumped in
# https://github.com/pytest-dev/pytest-django/pull/1263
Patch:          pytest_django-lower-pytest-req.diff

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
pytest-django allows you to test your Django project/applications with the
pytest testing tool.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
pytest-django allows you to test your Django project/applications with the
pytest testing tool.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{name}

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n pytest_django-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l pytest_django

%check
export DJANGO_SETTINGS_MODULE=pytest_django_test.settings_sqlite
PYTHONPATH=${PWD} %pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
