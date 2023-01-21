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
Version: 1.3.1
Release: 1%{?dist}
License: ASL 2.0
Source: https://github.com/michaelrsweet/pappl/releases/download/v%{version}/pappl-%{version}.tar.gz
Url: https://www.msweet.org/pappl

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
export DSOFLAGS="$DSOFLAGS -Wl,-z,now,--as-needed"
#need this to enable build with '-D_TIME_BITS=64' flag
export CPPFLAGS="$CPPFLAGS -D_FILE_OFFSET_BITS=64"
%configure
%make_build

%install
%make_install BUILDROOT=%{buildroot}
# Removal of the static library.
rm -f %{buildroot}/%{_libdir}/libpappl.a

%check
#new upstream tests from v1.3.0 are failing in mock
#make test

%files
%{_libdir}/libpappl.so.*
%doc *.md
%license LICENSE NOTICE

%files devel
%{_bindir}/*
%doc %{_docdir}/pappl/*
%{_mandir}/*/*
%dir %{_datadir}/pappl
%dir %{_includedir}/pappl
%{_datadir}/pappl/*
%{_includedir}/pappl/*.h
%{_libdir}/libpappl.so
%{_libdir}/pkgconfig/pappl.pc

%changelog
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
