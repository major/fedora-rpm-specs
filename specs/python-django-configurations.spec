%if 0%{?rhel} < 10
# sphinx version is too old
%bcond_with doc
%else
%bcond_without doc
%endif

%global pypi_name django-configurations

Name:           python-%{pypi_name}
Version:        2.5.1
Release:        %autorelease
Summary:        A helper for organizing Django settings

License:        BSD-3-Clause
URL:            https://django-configurations.readthedocs.io/
Source:         %{pypi_source}
Patch:          %{pypi_name}-adjust_test_cases.diff
Patch:          django-redis.diff

BuildArch:      noarch

%global _description %{expand:
django-configurations eases Django project configuration by relying on the
composability of Python classes. It extends the notion of Django's module
based settings loading with well established object oriented programming
patterns.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name} %_description

%if %{with doc}
%package -n python-%{pypi_name}-doc
Summary:        The documentation for %{name}

%description -n python-%{pypi_name}-doc
Documentation for %{name}.
%endif


%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info

# Remove unnecessary test BRs
sed -i '/coverage$/d' tox.ini
sed -i '/coverage_enable_subprocess$/d' tox.ini

%generate_buildrequires
%if %{with doc}
%pyproject_buildrequires -e docs -t
%else
%pyproject_buildrequires -t
%endif


%build
%pyproject_wheel

%if %{with doc}
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install

%pyproject_save_files configurations


%check
export DJANGO_CONFIGURATION="Test"
export DJANGO_SETTINGS_MODULE="tests.settings.main"
export PATH=$PATH:%{buildroot}%{_bindir}
export PYTHONPATH=%{buildroot}%{python3_sitelib}:$(pwd)
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/django-cadmin

%if %{with doc}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif


%changelog
%autochangelog
