# mailman3's TestableMaster can't be used outside of a
# source checkout?
%bcond_with tests

Name:           python-postorius
Version:        1.3.13
Release:        %autorelease
Summary:        Web UI for GNU Mailman

License:        GPL-3.0-or-later
URL:            https://gitlab.com/mailman/postorius
Source:         %{pypi_source postorius}
# allow Django 5.2, for Python 3.14 compatibility
Patch:          postorius-django52.diff
# https://nvd.nist.gov/vuln/detail/CVE-2026-44742
# per https://www.openwall.com/lists/oss-security/2026/05/07/3
# this fix was committed but never published as a new version
# backport https://gitlab.com/mailman/postorius/-/merge_requests/972.diff to 1.3.12
Patch:          postorius-fix-CVE-2026-44742.diff

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
