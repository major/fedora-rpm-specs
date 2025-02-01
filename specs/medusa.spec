%global commit0 4e9be7e91da6d1431e604338c1d3b8aff848541e
%global date 20240130
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:        Speedy, parallel, and modular, login brute-forcer
Name:           medusa
Version:        2.3
Release:        4.%{date}git%{shortcommit0}%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.foofus.net/jmk/medusa/medusa.html

Source0:        https://github.com/jmk-foofus/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

# https://github.com/jmk-foofus/medusa/pull/72
# https://bugzilla.redhat.com/show_bug.cgi?id=2340838
# Fix build with GCC 15
Patch:          0001-Fix-build-with-GCC-15-by-simplifying-libssh-callback.patch

BuildRequires:  apr-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freerdp2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libpq-devel
BuildRequires:  libssh2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  perl-Carp
BuildRequires:  subversion-devel

%description
Medusa is a speedy, massively parallel, modular, login brute-forcer for network
services. Some of the key features of Medusa are:

* Thread-based parallel testing. Brute-force testing can be performed against
  multiple hosts, users or passwords concurrently.
* Flexible user input. Target information (host/user/password) can be specified
  in a variety of ways.  For example, each item can be either a single entry or
  a file containing multiple entries.  Additionally, a combination file format
  allows the user to refine their target listing.
* Modular design. Each service module exists as an independent .mod file. This
  means that no modifications are necessary to the core application in order to
  extend the supported list of services for brute-forcing.

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build
autoreconf -vif
%configure \
    --enable-module-afp=no \
    --with-default-mod-path=%{_libdir}/medusa/modules
%make_build

%install
%make_install
 
%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_libdir}/%{name}

%changelog
* Thu Jan 30 2025 Adam Williamson <awilliam@redhat.com> - 2.3-4.20240130git4e9be7e
- Backport PR #72 to fix build with GCC 15
- Disable afpfs support as afpfs-ng has been retired

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3-3.20240130git4e9be7e
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2.20240130git4e9be7e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 09 2024 Simone Caronni <negativo17@gmail.com> - 2.3-1.20240130git4e9be7e
- Update to latest snapshot.
- Clean up SPEC file.
- Require FreeRDP 2 for building, FreeRDP 3 not supported.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-26.20220728git0796963
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-25.20220728git0796963
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-24.20220728git0796963
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 12 2020 Michal Ambroz <rebus AT seznam.cz> - 2.2-23.20220728git0796963
- bump to current git snapshot from 20220728

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-22.20181216git292193b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Simone Caronni <negativo17@gmail.com> - 2.2-21.20181216git292193b
- Rebuild for updated FreeRDP.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-20.20181216git292193b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-19.20181216git292193b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.2-18.20181216git292193b
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-17.20181216git292193b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 15 2021 Simone Caronni <negativo17@gmail.com> - 2.2-16.20181216git292193b
- Rebuild for updated FreeRDP.

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 2.2-15.20181216git292193b
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-14.20181216git292193b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
