# the package gets input from scanner devices from network
# can be possibly dangerous if an attacker camouflages himself
# as a scanner
%global _hardened_build 1

Name:           sane-airscan
Version:        0.99.31
Release:        1%{?dist}
Summary:        SANE backend for AirScan (eSCL) and WSD document scanners
# SANE related source and header files - GPL 2.0+ with SANE exception
# http_parser.c/.h - MIT
# the exception is defined in LICENSE, meant for SANE project in most cases
License:        GPL-2.0-or-later WITH SANE-exception AND MIT
URL:            https://github.com/alexpevzner/sane-airscan
Source:         %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

# backported from upstream


# needed for querying and getting mDNS messages from local network
BuildRequires:  avahi-devel
# project is written in C
BuildRequires:  gcc
# fuzzer for testing is written in C++
BuildRequires:  gcc-c++
# git is used during autosetup
BuildRequires:  git-core
# creating credentials and SHA256 for UUID
BuildRequires:  gnutls-devel
# needed for creating output image
BuildRequires:  libjpeg-turbo-devel, libpng-devel
# XML data are carried on HTTP protocol, we need to create them and parse them
BuildRequires:  libxml2-devel
# uses meson
BuildRequires: meson
# used in Makefile to get the correct compile and link flags
BuildRequires:  pkgconf-pkg-config
# package is meant to be as one of SANE backends - it uses SANE API for handling
# devices, strings, words (bytes) and backend itself
BuildRequires:  sane-backends-devel

%if 0%{?fedora} >= 38 || 0%{?rhel} >= 9
Recommends: ipp-usb
%endif

# needs shared library implementing the backend
Requires: libsane-airscan%{?_isa} = %{version}-%{release}

%description
This package contains a tool for discovering scanning devices in cases
when automatic discovery fails - airscan-discover.

%package -n libsane-airscan
Summary: SANE backend for eSCL or WSD

# USB scanners which support IPP-over-USB interface can communicate
# via sane-airscan once ipp-usb brings up an IPP interface for them
# remove for now until migration app is implemented
#Recommends: ipp-usb

%description -n libsane-airscan
This package contain a SANE backend for MFP and document scanners that
implements either eSCL (AirScan/AirPrint scanning) or WSD "driverless"
scanning protocol.


%prep
%autosetup -S git

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

rm -f %{buildroot}%{_libdir}/sane/libsane-airscan.so

%files
%license COPYING LICENSE
%{_bindir}/airscan-discover
# I'm not fond of wildcards in %%files, but FPG demands it for manpages
%{_mandir}/man1/airscan-discover.1*

%files -n libsane-airscan
%license COPYING LICENSE
%dir %{_sysconfdir}/sane.d
%config(noreplace) %{_sysconfdir}/sane.d/airscan.conf
%dir %{_sysconfdir}/sane.d/dll.d
%config(noreplace) %{_sysconfdir}/sane.d/dll.d/airscan
%dir %{_libdir}/sane
%{_libdir}/sane/libsane-airscan.so.1
# I'm not fond of wildcards in %%files, but FPG demands it for manpages
%{_mandir}/man5/sane-airscan.5*


%changelog
* Fri Jan 10 2025 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.31-1
- 0.99.31 (fedora#2334230)

* Thu Dec 19 2024 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.30-1
- 0.99.30 (fedora#2327285)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 18 2024 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.29-1
- 2263109 - sane-airscan-0.99.29 is available

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.27-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 08 2023 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.27-11
- fix FTBFS

* Wed Aug 30 2023 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.27-10
- applied accepted license exception - SANE-exception

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 23 2023 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.27-8
- move to meson

* Thu Feb 02 2023 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.27-7
- 2165612 - IPP-USB as a weak dependency of CUPS and sane-airscan

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 31 2022 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.27-4
- remove ipp-usb for now until there is a migration path

* Wed Mar 23 2022 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.27-3
- recommend ipp-usb in case of USB scanner capable of IPP-over-USB

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 11 2021 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.27-1
- 2012253 - sane-airscan-0.99.27 is available

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 19 2021 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.26-1
- 1949055 - sane-airscan-0.99.26 is available

* Thu Feb 04 2021 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.24-1
- 1922563 - sane-airscan-0.99.24 is available

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.23-1
- 1914565 - sane-airscan-0.99.23 is available

* Tue Dec 15 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.22-1
- 1906510 - sane-airscan-0.99.22 is available

* Tue Nov 24 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.21-1
- 0.99.21

* Mon Nov 23 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.20-1
- 1900160 - sane-airscan-0.99.20 is available
- 1897935 - Crash on libsane-airscan when trying to activate scanner

* Wed Nov 18 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.19-1
- 1890866 - sane-airscan-0.99.19 is available

* Thu Nov 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.18-2
- make is no longer in buildroot by default
- use smaller git-core instead of git

* Tue Oct 20 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.18-1
- 1887870 - sane-airscan-0.99.18 is available

* Fri Oct 09 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.17-1
- 1886593 - sane-airscan-0.99.17 is available

* Mon Oct 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.16-2
- 1882520 - Crash on libsane-airscan when trying to activate scanner

* Tue Sep 01 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.16-1
- 0.99.16

* Mon Aug 24 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.15-1
- 0.99.15

* Mon Aug 17 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.14-1
- 0.99.14 - fixing 1867126

* Thu Aug 13 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.13-2
- 1867692 - airscan driver crashes in mock during wsdd_cleanup()

* Mon Aug 10 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.13-1
- 0.99.13

* Wed Aug 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.12-1
- 0.99.12
- removed dependency to glib and libsoup - HTTP parser is implemented inside,
  bringing gnutls dependency
- sort buildrequires alphabetically

* Wed Jul 29 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.99.11-1
- Initial import (#1859207)
