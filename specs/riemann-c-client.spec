#
# spec file for package riemann-c-client
#
# Copyright (c) 2014 Peter Czanik, Budapest, Hungary.
#

%global sover 0

Name:		riemann-c-client
Version:	1.10.5
Release:	12%{?dist}
Summary:	The riemann C client
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
Url:		https://github.com/algernon/riemann-c-client
Source0:	%{url}/archive/refs/tags/%{name}-%{version}.tar.gz
Patch0000:	riemann-c-client-1.10.5-gcc10_symver.patch
Patch0001:      fix-gnutls-send-recv-when-return-eagain
Patch0002:      fix-gnutls-send-recv-when-return-less-than-expected
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig
BuildRequires:	protobuf-c-devel
BuildRequires:	json-c-devel
BuildRequires:  gnutls-devel

%description
This is a C client library for the Riemann monitoring system, providing a
convenient and simple API, high test coverage and a copyleft license,
along with API and ABI stability.

%package devel
Summary:	Development files for riemann-c-client
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	protobuf-c-devel%{?_isa}
Requires:	json-c-devel

%description devel
This package provides files necessary for riemann-c-client development.

%prep
%setup -qn %{name}-%{name}-%{version}
%patch -P0 -p1 -b.gcc10_symver
%patch -P1 -p1
%patch -P2 -p1
autoreconf -fiv

%build
%configure --disable-static
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/libriemann-client.la

%ldconfig_scriptlets

%files
%doc README.md NEWS.md
%license LICENSE*
%{_libdir}/libriemann-client.so.%{sover}*
%{_bindir}/riemann-client
%{_mandir}/man1/*.1*

%files devel
%{_includedir}/riemann/
%{_libdir}/libriemann-client.so
%{_libdir}/pkgconfig/riemann-client.pc

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10.5-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 05 2024 Peter Czanik <peter@czanik.hu> - 1.10.5-9
- add patches to fix gnutls error handling

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Björn Esser <besser82@fedoraproject.org> - 1.10.5-2
- Fix function mapping in versioned symbols
- Add sover macro to prevent accidental soname bumps

* Sun Nov 07 2021 Björn Esser <besser82@fedoraproject.org> - 1.10.5-1
- Update to 1.10.5

* Sun Nov 07 2021 Björn Esser <besser82@fedoraproject.org> - 1.9.0-25
- Add patch to fix parallel make and modernize spec file

* Sun Nov 07 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.9.0-24
- Disable parallel make

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 1.9.0-24
- Rebuilt for protobuf 3.19.0

* Mon Oct 25 2021 Adrian Reber <adrian@lisas.de> - 1.9.0-23
- Rebuilt for protobuf 3.18.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 1.9.0-21
- Rebuild for versioned symbols in json-c

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 14:43:12 CET 2021 Adrian Reber <adrian@lisas.de> - 1.9.0-19
- Rebuilt for protobuf 3.14

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 1.9.0-18
- Rebuilt for protobuf 3.13

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.9.0-16
- Rebuilt for protobuf 3.12

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 1.9.0-15
- Rebuild (json-c)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 1.9.0-10
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.9.0-8
- Rebuilt for libjson-c.so.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.9.0-5
- Rebuild for protobuf 3.3.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Orion Poplawski <orion@cora.nwra.com> - 1.9.0-3
- Rebuild for protobuf 3.2.0

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 1.9.0-2
- Rebuild for protobuf 3.1.0

* Thu Sep 15 2016 Peter Czanik <peter@czanik.hu> - 1.9.0-1
- update to 1.9.0 with mostly TLS fixes
- remove patch, which was merged upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Peter Czanik - 1.6.1-4
- new upstream which brings TLS support
- add patch to fix gnutls support on F20
- add workaround to detect json on EL6

* Thu Aug 14 2014 Peter Czanik <czanik@balabit.hu> - 1.2.1-3
- cleanup based on reviews at (#1129630)

* Mon Aug 11 2014 Peter Czanik <czanik@balabit.hu> - 1.2.1-1
- update to 1.2.1 (bugfix release)

* Thu Feb 27 2014 Peter Czanik <czanik@balabit.hu> - 1.1.0-1
- initial release
