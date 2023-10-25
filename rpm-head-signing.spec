%if 0%{?fedora} || 0%{?rhel} >= 8
%bcond_with python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with python3
%endif

# Currently broken in koji
%bcond_with tests

# Without this, the resulting insertlib will segfault
%define _lto_cflags %{nil}

%define debug_package %{nil}

%global pkgname rpm-head-signing
%global srcname rpm_head_signing

Name:           rpm-head-signing
Version:        1.7.2
Release:        1%{?dist}
Summary:        Small python module to extract RPM header and file digests
License:        MIT
URL:            https://github.com/fedora-iot/rpm-head-signing
Source0:        %url/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  ima-evm-utils
BuildRequires:  ima-evm-utils-devel
BuildRequires:  rpm-devel
BuildRequires:  rpm-sign
BuildRequires:  cpio
BuildRequires:  valgrind
BuildRequires:  zstd
%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-koji
BuildRequires:  python%{python3_pkgversion}-rpm
BuildRequires:  python%{python3_pkgversion}-cryptography
BuildRequires:  python%{python3_pkgversion}-pyxattr
%{?python_provide:%python_provide python3-%{pkgname}}
%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
Requires:       python%{python3_pkgversion}-cryptography
Requires:       python%{python3_pkgversion}-koji
Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-xattr
Requires:       python%{python3_pkgversion}-rpm
%endif
%endif
%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-koji
BuildRequires:  python2-rpm
BuildRequires:  python2-cryptography
BuildRequires:  pyxattr
%{?python_provide:%python_provide python2-%{pkgname}}
%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
Requires:       python2-koji
Requires:       python2-six
Requires:       python2-pyxattr
Requires:       rpm-python
%endif
%endif

%description
A small Python module (with C helper) to extract a RPM header and file
digests and reinsert the signature and signed file digests. This is
used for when you want to retrieve the parts to sign if you have a
remote signing server without having to transmit the entire RPM over
to the server.

%prep
%autosetup -p1
for lib in rpm_head_signing/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new
 mv $lib.new $lib
done


%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif


%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%py3_install
%endif


%if %{with tests}
%check
# To make sure we get to use the installed version
mv rpm_head_signing rpm_head_signing.orig

%if %{with python2}
PYTHONPATH=%{buildroot}%{python2_sitearch} SKIP_BYTEORDER_CHECK=true SKIP_IMA_LIVE_CHECK=true ONLY_ALTERNATIVE_EVMCTL_CHECK=true python2 test.py
%endif
%if %{with python3}
PYTHONPATH=%{buildroot}%{python3_sitearch} SKIP_IMA_LIVE_CHECK=true python3 test.py
%endif
%endif


%files
%license LICENSE
%doc README.md
%{_bindir}/verify-rpm-ima-signatures
%if %{with python3}
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-*/
%endif
%if %{with python2}
%{python2_sitearch}/%{srcname}/
%{python2_sitearch}/%{srcname}-*/
%endif


%changelog
* Fri Sep 22 2023 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.7.2-1
- fix: add sentinel to insertlib to prevent segfault

* Mon Oct 25 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.7-1
- fix: remove the LENGTH header again

* Thu Oct 7 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.6-1
- fix: add the LENGTH header for IMA signatures
- feat: add a fix_ima_signatures method to fix missing length headers

* Mon Oct 4 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.5.1-1
- fix: ensure that the determine function handles empty packages

* Wed Sep 29 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.5-1
- feat: add determine function to determine package status

* Mon Sep 27 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.4.3-1
- Fix: ignore RPM Ghost files
- Fix: ignore empty RPMs

* Tue Sep 14 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.4.2-1
- Ignore symbolic links when verifying RPMs

* Fri Sep 10 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.4.1-1
- Ensure xattrs are passed in as bytes

* Mon Aug 23 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.4-1
- Add verify-rpm-ima-signatures script to verify RPM signatures

* Mon Aug 16 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.3-1
- Feature: fix byte order on insert_signatures
- Fix: Compile on F32
- Fix: Beta RPM version parsing

* Thu Aug 05 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.2-1
- Generate zero digest

* Wed Aug 04 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.1-1
- Fix a segfault in case of an early error
- Update spec file to support python2
- Support IMA injection only

* Wed Jun 30 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.0-1
- Bump version to v1

* Wed Apr 28 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.1-2
- Moved ima_lookup.so to libdir

* Mon Apr 26 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.1-1
- Initial packaging
