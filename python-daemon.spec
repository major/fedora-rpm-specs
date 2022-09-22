%bcond_without tests

Name:           python-daemon
Version:        2.3.1
Release:        %autorelease
Summary:        Library to implement a well-behaved Unix daemon process

# Some build scripts and test franework are licensed GPLv3+ but those aren't shipped
License:        ASL 2.0
URL:            https://pagure.io/python-daemon
Source0:        %pypi_source
# Downstream-only patch, twine is unnecessary to build
# https://pagure.io/python-daemon/c/cc9e6a0321a547aacd568aa1e8c7d94a000d5d11
Patch0:         remove-twine-dependency.patch

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-docutils

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-testscenarios
BuildRequires:  python%{python3_pkgversion}-lockfile
BuildRequires:  python%{python3_pkgversion}-testtools
%endif

%global _description\
This library implements the well-behaved daemon specification of PEP 3143,\
"Standard daemon process library".\

%description %_description

%package -n python%{python3_pkgversion}-daemon
Summary:        Library to implement a well-behaved Unix daemon process

%description -n python%{python3_pkgversion}-daemon %_description

This is the python3 version of the library.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install
rm -fr %{buildroot}%{python3_sitelib}/tests

%if %{with tests}
# Test suite requires minimock and lockfile
%check
PYTHONPATH=$(pwd) %{__python3} -m unittest discover
%endif

%files -n python%{python3_pkgversion}-daemon
%license LICENSE.ASF-2
%{python3_sitelib}/daemon/
%{python3_sitelib}/python_daemon-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
