%global srcname dj_database_url

Name:           python-django-database-url
Version:        0.5.0
Release:        27%{?dist}
Summary:        Use Database URLs in your Django Application
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/kennethreitz/dj-database-url
Source0:        https://github.com/kennethreitz/dj-database-url/archive/v%{version}.tar.gz#/dj-database-url-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This simple Django utility allows you to utilize the 12factor inspired
DATABASE_URL environment variable to configure your Django application.}

%description %_description

%package -n python3-django-database-url
Summary:        %summary
Requires:       python3-django
Obsoletes:      python-django-database-url < 0.4.2-4
Obsoletes:      python2-django-database-url < 0.4.2-4

%description -n python3-django-database-url %_description

%prep
%autosetup -n dj-database-url-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import
%{py3_test_envvars} %{python3} test_dj_database_url.py

%files -n python3-django-database-url -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
