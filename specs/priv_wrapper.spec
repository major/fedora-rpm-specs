Name:           priv_wrapper
Version:        1.0.1
Release:        13%{?dist}

Summary:        A library to disable resource limits and other privilege dropping
License:        GPL-3.0-or-later
Url:            http://cwrap.org/

Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
# Upstream signing key from its website, completed from keyservers/WKD:
#   curl -fsSL -o key.asc https://cryptomilk.org/0x8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D_asn_cryptomilk_org_gpgkey.asc
#   sq --home=none network search --output - 8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D | sq keyring filter --experimental --cert 8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D --output update.pgp
#   sq keyring merge key.asc update.pgp | sq packet dearmor --output priv_wrapper.keyring.new
#   mv priv_wrapper.keyring.new priv_wrapper.keyring
#   rm -f key.asc update.pgp
Source2:        priv_wrapper.keyring

Patch0:         priv_wrapper-fix-cmocka-1.1.6+-support.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openpgpverify
BuildRequires:  libcmocka-devel >= 1.1.0

Recommends:     cmake
Recommends:     pkgconfig

%description
priv_wrapper aims to help running processes which are dropping privileges or
are restricting resources in test environments.
It can disable chroot, prctl, pledge and setrlmit system calls. A disabled call
always succeeds (i.e. returns 0) and does nothing.
The system call pledge exists only on OpenBSD.

To use it, set the following environment variables:

LD_PRELOAD=libpriv_wrapper.so
PRIV_WRAPPER_CHROOT_DISABLE=1

This package does not have a devel package, because this project is for
development/testing.

%prep
%{openpgpverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake \
  -DUNIT_TESTING=ON
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%check
%ctest

%files
%doc AUTHORS README.md CHANGELOG.md
%license LICENSE
%{_libdir}/libpriv_wrapper.so*
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/priv_wrapper
%{_libdir}/cmake/priv_wrapper/priv_wrapper-config-version.cmake
%{_libdir}/cmake/priv_wrapper/priv_wrapper-config.cmake
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/priv_wrapper.pc
%{_mandir}/man1/priv_wrapper.1*

%changelog
* Tue Nov 03 2026 Jakub Jelen <jjelen@redhat.com> - 1.0.1-13
- Verify upstream source signatures with openpgpverify

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 06 2023 Andreas Schneider <asn@redhat.com> - 1.0.1-4
- Update License to SPDX expression

* Mon Feb 27 2023 Andreas Schneider <asn@redhat.com> - 1.0.1-3
- Fix building with cmocka >= 1.1.6

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Pavel Filipenský <pfilipenn@redhat.com> - 1.0.1-1
- Update to version 1.0.1

* Thu Nov 10 2022 Pavel Filipenský <pfilipen@redhat.com> - 1.0.0-3
- Patch prctl() on ppc64le

* Tue Oct 25 2022 Pavel Filipenský <pfilipen@redhat.com> - 1.0.0-2
- Verify packages using gpgverify
- Make description line length < 80

* Mon Oct 24 2022 Pavel Filipenský <pfilipen@redhat.com> -  1.0.0-1
- Initial package
