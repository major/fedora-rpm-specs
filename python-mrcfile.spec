# main package is archful to run tests everywhere but produces noarch packages
%global debug_package %{nil}
%bcond_without check
%global pname mrcfile

%global desc \
mrcfile is a Python implementation of the MRC2014 file format, which is used in\
structural biology to store image and volume data.\
\
It allows MRC files to be created and opened easily using a very simple API,\
which exposes the file's header and data as numpy arrays. The code runs in\
Python 2 and 3 and is fully unit-tested.\
\
This library aims to allow users and developers to read and write\
standard-compliant MRC files in Python as easily as possible, and with no\
dependencies on any compiled libraries except numpy. You can use it\
interactively to inspect files, correct headers and so on, or in scripts and\
larger software packages to provide basic MRC file I/O functions.

Name: python-%{pname}
Version: 1.3.0
Release: 7%{?dist}
Summary: MRC2014 file format used in structural biology to store image and volume data
License: BSD
URL: https://github.com/ccpem/mrcfile
Source0: https://github.com/ccpem/mrcfile/archive/v%{version}/%{pname}-%{version}.tar.gz
Patch0: 0001-Use-explicit-endianness-for-FEI-extended-header-dtyp.patch
Patch1: 0002-Finish-applying-extended-header-byte-order-fix.patch
Patch2: 0003-Check-that-test-file-extended-header-is-always-littl.patch
Patch3: 0001-Switch-to-built-in-bool-type-to-avoid-numpy-deprecat.patch
# fix test failures with python 3.11 due to changed error messages
Patch10: %{name}-python311.patch

%description
%{desc}

%package -n python3-%{pname}
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%if %{with check}
BuildRequires: python3-numpy
%endif
%{?python_provide:%python_provide python3-%{pname}}
BuildArch: noarch

%description -n python3-%{pname}
%{desc}

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
# 8 tests are failing on s390x: https://github.com/ccpem/mrcfile/issues/35
PYTHONDONTWRITEBYTECODE=1 \
PATH=%{buildroot}/usr/bin:${PATH} \
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} \
python3 -m unittest tests
%endif

%files -n python3-%{pname}
%license LICENSE.txt
%doc CHANGELOG.txt README.rst
%{_bindir}/mrcfile-header
%{_bindir}/mrcfile-validate
%{python3_sitelib}/%{pname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pname}

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.3.0-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.11

* Fri Jun 10 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.3.0-3
- fix test failures with python 3.11 (due to changed error messages)

* Wed Apr 27 2022 Dominik Mierzejewski <dominik@greysector.net> - 1.3.0-2
- backport upstream endiannes fixes
- backport upstream numpy deprecation warning fix

* Fri Mar 11 2022 Dominik Mierzejewski <dominik@greysector.net> 1.3.0-1
- initial build
