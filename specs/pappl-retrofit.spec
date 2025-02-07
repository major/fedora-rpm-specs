# the original SPEC file was created by Brandon Nielsen in his COPR repo and this comment
# is to honor his great contribution - thank you for all you work, Brandon!
#
# Brandon changes are present in Changelog as well to let people know he worked on this SPEC file.

%global serverbin /usr/lib/

%if 0%{?fedora}
%bcond_without mdns
%else
%bcond_with mdns
%endif

Name: pappl-retrofit
Version: 1.0b2
Release: 7%{?dist}
# the CUPS exception text is the same as LLVM exception, so using that name with
# agreement from legal team
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/A7GFSD6M3GYGSI32L2FC5KB22DUAEQI3/
License: Apache-2.0 WITH LLVM-exception
Summary: Library for common functions used in retrofitting printer applications
URL: https://github.com/OpenPrinting/pappl-retrofit/
Source0: %{URL}/releases/download/%{version}/pappl-retrofit-%{version}.tar.gz
Source1: legacy-printer-app.conf

# Patches
# FTBFS
# https://github.com/OpenPrinting/pappl-retrofit/commit/0317fae79ce
Patch001: 0001-pappl-retrofit-private.h-Add-include-cups-sidechanne.patch
# add man page
# https://github.com/OpenPrinting/pappl-retrofit/commit/33be36f28
Patch002: 0001-Added-man-page-for-the-Legacy-Printer-Application.patch
# fix use after free
# part of https://github.com/OpenPrinting/pappl-retrofit/commit/eebb36724a62
Patch003: pappl-retrofit-use-after-free.patch
# https://github.com/OpenPrinting/pappl-retrofit/pull/27
Patch004: 0001-Use-PAPPL-configuration-options-from-file.patch
# https://github.com/OpenPrinting/pappl-retrofit/pull/28
Patch005: 0001-Fix-possible-unterminated-string.patch
Patch006: 0001-cups-backends.c-Ensure-read-string-is-NULL-terminate.patch
Patch007: 0001-Protect-_prASCII-from-negative-lengths.patch
Patch008: 0001-Fix-potential-memory-leaks.patch
# https://github.com/OpenPrinting/pappl-retrofit/pull/31
Patch009: 0001-Fix-memory-leaks-from-compiled_re_list.patch


# for autogen.sh - generating configure scripts
BuildRequires: autoconf
# for autogen.sh - generating Makefiles
BuildRequires: automake
# for autopoint
BuildRequires: gettext-devel
# compiled by gcc
BuildRequires: gcc
# for autosetup
BuildRequires: git-core
# uses make
BuildRequires: make
# uses libtool during build
BuildRequires: libtool
# supports PAM authentication
BuildRequires: pam-devel
# for pkg-config in configure and in SPEC file
BuildRequires: pkgconf-pkg-config
# CUPS API for arrays, IPP etc.
BuildRequires: pkgconfig(cups) >= 2.2.0
# API for filter functions
BuildRequires: pkgconfig(libcupsfilters) >= 2.0b2
# API for loading PPDs and its conversion to IPP
BuildRequires: pkgconfig(libppd) >= 2.0b2
# printer application library for common objects
BuildRequires: pkgconfig(pappl) >= 1.1b2
# used to fix unused shlib dependency error from rpmlint
BuildRequires: sed
# uses systemd macros in %%files
BuildRequires: systemd-rpm-macros


%description
This library together with PAPPL and cups-filters 2.x allows to convert classic
CUPS printer drivers into Printer Applications. This way the printer appears as
an emulated IPP printer and one can print on it from practically any operating
system, especially also mobile operating systems and IoT platforms,
without need any client-side driver.

%package devel
Summary: Development environment for pappl-retrofit
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the pappl-retrofit headers and development environment.

%package -n legacy-printer-app
Summary: Legacy printer application

# virtual provide for /usr/sbin -> /usr/bin link
# the original daemon is installed in /usr/sbin
Provides: /usr/bin/legacy-printer-app

%if %{with mdns}
# Avahi has to run for mDNS support
Recommends: avahi
# if we go for mDNS, we need a resolver
Recommends: nss-mdns
%endif
# recommend CUPS, the daemon which usually picks up IPP services
Recommends: cups

Requires: %{name}%{?_isa} = %{version}-%{release}
# for password-auth PAM module
Requires: authselect-libs
# it is needed for providing /usr/lib/cups as well
Requires: cups-filesystem

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description -n legacy-printer-app
Legacy printer application provides support for classic printer drivers
which are not part of official Linux repositories - it enables possibility
to set your printer with proprietary printer drivers from manufacturers,
so such printer will be seen by CUPS.


%prep
%autosetup -S git


%build
# needed for regenerating .in files, which contents might change across releases
# f.e. BZ#2341000 was caused requiring automake-1.16 for unknown reason
./autogen.sh

%configure --enable-legacy-printer-app-as-daemon\
  --enable-shared\
  --disable-static\
  --disable-silent-rules

sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build


%install
%make_install

# Remove license files from doc
rm -f %{buildroot}/%{_docdir}/%{name}/{LICENSE,NOTICE,COPYING}

# remove symlink, we need it in /usr/lib
rm -f %{buildroot}/%{_libdir}/legacy-printer-app
ln -sf /usr/lib/cups %{buildroot}/%{serverbin}/legacy-printer-app

install -p -D -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/legacy-printer-app.conf


%check
make check


%post -n legacy-printer-app
%systemd_post legacy-printer-app.service

%preun -n legacy-printer-app
%systemd_preun legacy-printer-app.service

%postun -n legacy-printer-app
%systemd_postun_with_restart legacy-printer-app.service

%files
%license LICENSE NOTICE COPYING
%doc AUTHORS README.md
%{_libdir}/libpappl-retrofit.so.1
%{_libdir}/libpappl-retrofit.so.1.0.0

%files devel
%{_docdir}/%{name}/CONTRIBUTING.md
%{_docdir}/%{name}/DEVELOPING.md
%{_includedir}/pappl-retrofit.h
%{_libdir}/libpappl-retrofit.so
%{_libdir}/pkgconfig/libpappl-retrofit.pc

%files -n legacy-printer-app
%config(noreplace) %{_sysconfdir}/legacy-printer-app.conf
%{_sbindir}/legacy-printer-app
%{_unitdir}/legacy-printer-app.service
%dir %{_datadir}/legacy-printer-app
%{_datadir}/legacy-printer-app/testpage.ps
%{_datadir}/legacy-printer-app/testpage.pdf
# this symlink is required if the app should use CUPS backends/filters
# in /usr/lib/cups
%{serverbin}/legacy-printer-app
%{_mandir}/man1/legacy-printer-app.1.gz

%changelog
* Wed Feb 05 2025 Zdenek Dohnal <zdohnal@redhat.com> - 1.0b2-7
- fix memory leaks from CUPS array

* Mon Feb 03 2025 Zdenek Dohnal <zdohnal@redhat.com> - 1.0b2-6
- Fix FTBFS (fedora#2341000)
- Fix issues reported by OSH

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0b2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 08 2024 Zdenek Dohnal <zdohnal@redhat.com> - 1.0b2-5
- really use /usr/lib/...

* Mon Jul 29 2024 Zdenek Dohnal <zdohnal@redhat.com> - 1.0b2-4
- remove auth-service, use password if needed

* Mon Jul 29 2024 Zdenek Dohnal <zdohnal@redhat.com> - 1.0b2-3
- use legacy-printer-app.conf for default server options

* Thu Jan 18 2024 Zdenek Dohnal <zdohnal@redhat.com> 1.0b2-2
- 2300030 - review request: pappl-retrofit

* Mon Sep 18 2023 Brandon Nielsen <nielsenb@jetfuse.net> 1.0b2-1
- Update to 1.0b2
- Change to SPDX license identifier
- Enable the legacy printer app as a daemon

* Thu Feb 2 2023 Brandon Nielsen <nielsenb@jetfuse.net> 1.0b1-1
- Update to 1.0b1

* Thu Aug 25 2022 Brandon Nielsen <nielsenb@jetfuse.net> 0-1.20220825git32483ad
- Update to 32483ad git snapshot

* Sun Feb 27 2022 Brandon Nielsen <nielsenb@jetfuse.net> 0-1.20220227gitfe6c189
- Update to fe6c189 git snapshot

* Tue Nov 16 2021 Brandon Nielsen <nielsenb@jetfuse.net> 0-1.20211116git95113dc
- Update to latest git

* Wed Sep 22 2021 Brandon Nielsen <nielsenb@jetfuse.net> 0-1.20210916git59864c0
- Initial specfile
