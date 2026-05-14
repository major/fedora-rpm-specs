# Many test dependencies still missing
%bcond_with tests

Name:           python-django-q2
Version:        1.10.0
Release:        %autorelease
Summary:        A multiprocessing distributed task queue for Django

License:        MIT
URL:            https://django-q2.readthedocs.org
Source:         %{pypi_source django_q2}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{without tests}
# still need this for import checks
BuildRequires:  python3dist(django-redis)
%endif


%global _description %{expand:
Django Q2 is a native Django task queue, scheduler and worker application using
Python multiprocessing.}

%description %_description

%package -n     python3-django-q2
Summary:        %{summary}
# django-q stalled at 1.3.9
Obsoletes:      python3-django-q < 1.3.10

%description -n python3-django-q2 %_description


%prep
%autosetup -p1 -n django_q2-%{version}


%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -x testing
%else
%pyproject_buildrequires
%endif


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l django_q


%check
export DJANGO_SETTINGS_MODULE=django_q.tests.settings
%pyproject_check_import -e django_q.admin -e django_q.models -e 'django_q.brokers.*' -e 'django_q.tests.*'


%files -n python3-django-q2 -f %{pyproject_files}
%doc CHANGELOG.md README.rst


%changelog
%autochangelog
