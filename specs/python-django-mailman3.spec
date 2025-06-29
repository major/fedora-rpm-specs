Name:           python-django-mailman3
Version:        1.3.15
Release:        %autorelease
Summary:        Django library to help interaction with Mailman

License:        GPL-3.0-or-later
URL:            https://gitlab.com/mailman/django-mailman3
Source:         %{pypi_source django_mailman3}
Patch:          django-mailman3-localdeps.patch
# Allow Django 5.2, for Python 3.14 compatibility
Patch:          django-mailman3-django52.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description %{expand:
This package contains libraries and templates for Django-based interfaces
interacting with Mailman.

To use this application, add django_mailman3 to the INSTALLED_APPS list in your
Django server’s settings file.}

%description %{_description}


%package -n python%{python3_pkgversion}-django-mailman3
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-mailman3 %{_description}


%prep
%autosetup -p1 -n django_mailman3-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files django_mailman3


%check
# Tests want to be run locally
PYTHONPATH=.:${PYTHONPATH} %pytest -v --deselect \
  django_mailman3/tests/test_signals.py::SignalsTestCase::test_social_account_added


%files -n  python%{python3_pkgversion}-django-mailman3 -f %{pyproject_files}
%license COPYING.txt
%doc README.rst


%changelog
%autochangelog
