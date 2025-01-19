Name:    libptytty
Version: 2.0
Release: 12%{?dist}
Summary: OS independent and secure pty/tty and utmp/wtmp/lastlog handling
License: GPL-2.0-or-later
URL:     http://software.schmorp.de/pkg/libptytty.html

Source0: http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.gz
Source1: http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.gz.sig
Source2: http://dist.schmorp.de/signing-key.pub
Source3: http://dist.schmorp.de/signing-key.pub.gpg.sig
Source4: gpgkey-84874CAB6D1A397A.gpg
# To recreate Source4:
#     gpg --recv-key 84874CAB6D1A397A
#     gpg --export --export-options export-minimal 84874CAB6D1A397A \
#         > gpgkey-84874CAB6D1A397A.gpg

Patch0: libptytty-cmake-c99.patch

BuildRequires: cmake
BuildRequires: gcc-g++
BuildRequires: gnupg2
BuildRequires: git
BuildRequires: ninja-build
BuildRequires: signify

%global desc \
libptytty is a small library that offers pseudo-tty management in an \
OS-independent way.  It also offers session database support (utmp and \
optional wtmp/lastlog updates for login shells) and supports fork'ing after \
startup and dropping privileges in the calling process.  Libptytty is \
written in C++, but it also offers a C-only API. \
%{nil}
%description %{desc}

%package devel
Summary: Development headers for libptytty
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%desc

%prep
%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE3}' --data='%{SOURCE2}'
signify -V -p '%{SOURCE2}' -m '%{SOURCE0}'
%autosetup -S git

%build
%cmake -G Ninja
%cmake_build

%install
%cmake_install

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
%doc Changes
%doc README

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 29 2024 David Cantrell <dcantrell@redhat.com> - 2.0-10
- Fix URL

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Arjun Shankar <arjun@redhat.com> - 2.0-6
- Port to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 David Cantrell <dcantrell@redhat.com> - 2.0-4
- Convert license to SPDX format: GPL-2.0-or-later

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 22 2021 Robbie Harwood <rharwood@redhat.com> - 2.0-1
- Initial import (2.0)
