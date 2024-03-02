%global srcname django-mailman3

Name:           python-%{srcname}
Version:        1.3.11
Release:        %autorelease
Summary:        Django library to help interaction with Mailman
License:        GPL-3.0-or-later
URL:            https://gitlab.com/mailman/django-mailman3
Source:         %{pypi_source %{srcname}}
Patch:          %{srcname}-localdeps.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description %{expand:
This package contains libraries and templates for Django-based interfaces
interacting with Mailman.

To use this application, add django_mailman3 to the INSTALLED_APPS list in your
Django server’s settings file.}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files django_mailman3


%check
# Tests want to be run locally
PYTHONPATH=.:${PYTHONPATH} %tox


%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license COPYING.txt
%doc README.rst


%changelog
%autochangelog
