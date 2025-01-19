#
# RPM spec file for the Printer Application Framework
#
# Copyright © 2020-2021 by Michael R Sweet
#
# Licensed under Apache License v2.0.  See the file "LICENSE" for more
# information.
#

Summary: Printer Application Framework (PAPPL)
Name: pappl
Version: 1.4.8
Release: 3%{?dist}
License: Apache-2.0 WITH LLVM-exception
Source: https://github.com/michaelrsweet/pappl/releases/download/v%{version}/pappl-%{version}.tar.gz
Url: https://www.msweet.org/pappl


# Add listing raw sockets
# https://github.com/michaelrsweet/pappl/pull/341
Patch001: 0001-List-raw-sockets-during-printers-subcommand-if-avail.patch
# raise MAX_VENDOR https://sourceforge.net/p/gimp-print/mailman/gimp-print-devel/thread/e24b2385-6576-a949-a40d-3786c8067520%40gmail.com/#msg37353830
# downstream only, Mike does not want to merge the change
Patch002: pappl-max-vendors.patch


BuildRequires: avahi-devel
BuildRequires: cups-devel
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: glibc-devel
BuildRequires: gnutls-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: libusbx-devel
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: pam-devel
BuildRequires: zlib-devel

%description
PAPPL is a simple C-based framework/library for developing CUPS Printer
Applications, which are the recommended replacement for printer drivers.

PAPPL supports JPEG, PNG, PWG Raster, Apple Raster, and "raw" printing to
printers connected via USB and network (AppSocket/JetDirect) connections.
PAPPL provides access to the printer via its embedded IPP Everywhere™ service,
either local to the computer or on your whole network, which can then be
discovered and used by any application.

PAPPL is licensed under the Apache License Version 2.0 with an exception
to allow linking against GPL2/LGPL2 software (like older versions of CUPS),
so it can be used freely in any project you'd like.

%package devel
Summary: PAPPL - development environment
Requires: %{name}%{?_isa} = %{version}-%{release}

BuildRequires: avahi-devel

%description devel
This package provides the PAPPL headers and development environment.

%prep
%autosetup -S git

%build
#need this to enable build with '-D_TIME_BITS=64' flag
export CPPFLAGS="$CPPFLAGS -D_FILE_OFFSET_BITS=64"
%configure --enable-libjpeg\
  --enable-libpng\
  --enable-libusb\
  --disable-static\
  --with-dnssd=avahi\
  --with-tls=gnutls\
  --with-dsoflags="$DSOFLAGS -Wl,-z,now,--as-needed"
# add --enable-libpam once there is a new version - cosmetic issue, libpam is used when
# found in buildroot, which is taken care of by BuilrRequires for pam-devel
%make_build

%install
%make_install BUILDROOT=%{buildroot}

%check
make test

%files
%dir %{_datadir}/pappl
%{_datadir}/pappl/*
%dir %{_docdir}/pappl
%doc *.md
%{_libdir}/libpappl.so.*
%license LICENSE NOTICE

%files devel
%{_bindir}/pappl-makeresheader
%{_docdir}/pappl/*.png
%{_docdir}/pappl/*.html
%dir %{_includedir}/pappl
%{_includedir}/pappl/*.h
%{_libdir}/libpappl.so
%{_libdir}/pkgconfig/pappl.pc
%{_mandir}/man1/pappl.1.gz
%{_mandir}/man1/pappl-makeresheader.1.gz
%{_mandir}/man3/pappl-client.3.gz
%{_mandir}/man3/pappl-device.3.gz
%{_mandir}/man3/pappl-job.3.gz
%{_mandir}/man3/pappl-log.3.gz
%{_mandir}/man3/pappl-mainloop.3.gz
%{_mandir}/man3/pappl-printer.3.gz
%{_mandir}/man3/pappl-resource.3.gz
%{_mandir}/man3/pappl-system.3.gz

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 15 2024 Zdenek Dohnal <zdohnal@redhat.com> - 1.4.8-2
- moved files between library and devel to prevent conflicts

* Fri Nov 15 2024 Zdenek Dohnal <zdohnal@redhat.com> - 1.4.8-1
- 1.4.8 (fedora#2326364)

* Thu Nov 14 2024 Zdenek Dohnal <zdohnal@redhat.com> - 1.4.7-2
- provide support for registering on localhost-only
- fix password parsing issue

* Wed Oct 16 2024 Zdenek Dohnal <zdohnal@redhat.com> - 1.4.7-1
- 1.4.7 (fedora#2319037)

* Thu Aug 08 2024 Zdenek Dohnal <zdohnal@redhat.com> - 1.4.6-5
- have to rebuilt in side-tag to avoid crashes

* Mon Jul 29 2024 Zdenek Dohnal <zdohnal@redhat.com> - 1.4.6-4
- enlarge array for vendor specific attributtes

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Zdenek Dohnal <zdohnal@redhat.com> - 1.4.6-2
- provide a way how to define port of the printer

* Thu Feb 15 2024 Zdenek Dohnal <zdohnal@redhat.com> - 1.4.6-1
- 2260676 - pappl-1.4.6 is available

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Zdenek Dohnal <zdohnal@redhat.com> - 1.4.4-1
- 2255704 - pappl-1.4.4 is available

* Mon Dec 18 2023 Richard Lescak <rlescak@redhat.com> - 1.4.3-1
- rebase to version 1.4.3 (#2250222)

* Wed Oct 18 2023 Richard Lescak <rlescak@redhat.com> - 1.4.2-1
- rebase to version 1.4.2 (#2238033)

* Fri Oct 13 2023 Richard Lescak <rlescak@redhat.com> - 1.4.1-1
- rebase to version 1.4.1 (#2238033)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 11 2023 Richard Lescak <rlescak@redhat.com> - 1.3.2-1
- rebase to version 1.3.2 (#2195988)

* Thu Apr 13 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1.3.1-3
- fix crash due invalid buffer size in `write_log()`
- use the correct license tag

* Thu Feb 16 2023 Richard Lescak <rlescak@redhat.com> - 1.3.1-2
- SPDX migration

* Thu Jan 19 2023 Richard Lescak <rlescak@redhat.com> - 1.3.1-1
- Rebase to version 1.3.1 (#2157744)

* Fri Dec 16 2022 Richard Lescak <rlescak@redhat.com> - 1.3.0-1
- Rebase to version 1.3.0 (#2150441)

* Fri Oct 21 2022 Richard Lescak <rlescak@redhat.com> - 1.2.3-1
- Rebase to version 1.2.3 (#2133319)

* Tue Sep 27 2022 Richard Lescak <rlescak@redhat.com> - 1.2.2-1
- Rebase to version 1.2.2 (#2129391)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Richard Lescak <rlescak@redhat.com> - 1.2.1-2
- link libpappl with -Wl,-z,now 

* Tue Jun 21 2022 Richard Lescak <rlescak@redhat.com> - 1.2.1-1
- Rebase to version 1.2.1 (#2078148)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Richard Lescak <rlescak@redhat.com> - 1.1.0-1
- Rebase to version 1.1.0 (#2020646)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Richard Lescak <rlescak@redhat.com> - 1.0.3-1
- Update to version 1.0.3 (#1962959)

* Tue Apr 13 2021 Richard Lescak <rlescak@redhat.com> - 1.0.2-2
- Added patch to fix tests, added DSOFLAGS in build, made changes according to review.

* Fri Mar 26 2021 Richard Lescak <rlescak@redhat.com> - 1.0.2-1
- Initial version of package
