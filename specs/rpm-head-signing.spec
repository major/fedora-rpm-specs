# Currently broken in koji
%bcond_with tests

# Without this, the resulting insertlib will segfault
%define _lto_cflags %{nil}

%define debug_package %{nil}

%global pkgname rpm-head-signing
%global srcname rpm_head_signing

Name:           rpm-head-signing
Version:        1.7.4
Release:        11%{?dist}
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
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  zstd
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-koji
BuildRequires:  python%{python3_pkgversion}-rpm
BuildRequires:  python%{python3_pkgversion}-cryptography
BuildRequires:  python%{python3_pkgversion}-pyxattr

Requires:  python%{python3_pkgversion}-koji
Requires:  python%{python3_pkgversion}-rpm
Requires:  python%{python3_pkgversion}-cryptography
Requires:  python%{python3_pkgversion}-pyxattr

%{?python_provide:%python_provide python3-%{pkgname}}

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


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}


%if %{with tests}
%check
# To make sure we get to use the installed version
mv rpm_head_signing rpm_head_signing.orig

PYTHONPATH=%{buildroot}%{python3_sitearch} SKIP_IMA_LIVE_CHECK=true python3 test.py
%endif


%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/verify-rpm-ima-signatures


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jul 09 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.4-10
- Migrate to new python build macros (rhbz: 2378441)

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.7.4-9
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.7.4-6
- Rebuilt for Python 3.13

* Mon Feb 19 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.4-5
- Check valgrind arches

* Fri Feb 16 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.4-4
- Update runtime requires

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 25 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.4-1
- Update to 1.7.4
- Upstream and package fixes

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
