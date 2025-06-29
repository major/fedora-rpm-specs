# mailman3's TestableMaster can't be used outside of a
# source checkout?
%bcond_with tests

Name:           python-postorius
Version:        1.3.12
Release:        %autorelease
Summary:        Web UI for GNU Mailman

License:        GPL-3.0-or-later
URL:            https://gitlab.com/mailman/postorius
Source:         %{pypi_source postorius}
# don't ship examples, they end up in sitelib
Patch:          postorius-dont-ship-examples.diff
# allow Django 5.2, for Python 3.14 compatibility
Patch:          postorius-django52.diff

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description %{expand:
The Postorius Django app provides a web user interface to access GNU Mailman.}

%description %{_description}


%package -n postorius
Summary:        %{summary}

%description -n postorius %{_description}


%prep
%autosetup -p1 -n postorius-%{version}


%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t
%else
%pyproject_buildrequires
%endif


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files postorius


%check
# this requires the Django app to be set up first
# export DJANGO_SETTINGS_MODULE=postorius.doc.settings
# %%pyproject_check_import
%if %{with tests}
PYTHONPATH=$(pwd)/src:${PYTHONPATH} \
%tox
%endif


%files -n postorius -f %{pyproject_files}
%license COPYING
%doc README.rst


%changelog
%autochangelog
