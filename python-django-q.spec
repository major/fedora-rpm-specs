# "can't find tests module"
%bcond_with tests

%global srcname django-q
%global modname django_q

%global forgeurl https://github.com/koed00/django-q

Name:           python-%{srcname}
Version:        1.3.9
Release:        %autorelease
Summary:        A multiprocessing distributed task queue for Django
License:        MIT
URL:            https://django-q.readthedocs.org/
# pyproject.toml from GH doesn't seem to work
Source0:        %{pypi_source %{srcname}}
# Source0:        %%{forgeurl}/archive/v%%{version}/%%{srcname}-%%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
%if %{with tests}
# Test dependencies:
# BuildRequires:  python3dist(django-redis)
%endif

%global _description %{expand:
A multiprocessing distributed task queue for Django

Features:
- Multiprocessing worker pool
- Asynchronous tasks
- Scheduled, cron and repeated tasks
- Signed and compressed packages
- Failure and success database or cache
- Result hooks, groups and chains
- Django Admin integration
- PaaS compatible with multiple instances
- Multi cluster monitor
- Redis, Disque, IronMQ, SQS, MongoDB or ORM
- Rollbar and Sentry support}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
# project's pyproject.toml caused our script to choke
# seems fine when using PyPI
%pyproject_buildrequires


%build
%pyproject_wheel


%install
# these installs UNKNOWN-0.0.0.dist-info
# when using GH tarball
%pyproject_install
%pyproject_save_files %{modname}


%if %{with tests}
%check
%python3 -m django test -v2 --settings=django_q.tests.settings
%endif


%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md README.rst


%changelog
%autochangelog
