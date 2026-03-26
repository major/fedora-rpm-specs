Name:       llconf
Version:    0.4.6
Release:    32%{?dist}
Summary:    Loss-less configuration file parser
# COPYING:              LGPL-2.1 text
# examples/example.c:   GPL-2.0-or-later
# src/entry.c:          LGPL-2.1-or-later
# src/entry.h:          LGPL-2.1-or-later
# src/lines.c:          LGPL-2.1-or-later
# src/lines.h:          LGPL-2.1-or-later
# src/llconf.c:         LGPL-2.1-or-later
# src/modules.c:        LGPL-2.1-or-later
# src/modules.h:        LGPL-2.1-or-later
# src/nodes.c:          LGPL-2.1-or-later
# src/nodes.h:          LGPL-2.1-or-later
# src/parseerror.c:     LGPL-2.1-or-later
# src/parseerror.h:     LGPL-2.1-or-later
# src/parsers/conserver.c:  LGPL-2.1-or-later
# src/parsers/conserver.h:  LGPL-2.1-or-later
# src/parsers/cron.c:   LGPL-2.1-or-later
# src/parsers/cron.h:   LGPL-2.1-or-later
# src/parsers/cyconf.c: LGPL-2.1-or-later
# src/parsers/cyconf.h: LGPL-2.1-or-later
# src/parsers/dhcp.c:   LGPL-2.1-or-later
# src/parsers/dhcp.h:   LGPL-2.1-or-later
# src/parsers/dhcp_leases.c:    LGPL-2.1-or-later
# src/parsers/dhcp_leases.h:    LGPL-2.1-or-later
# src/parsers/file.c:   LGPL-2.1-or-later
# src/parsers/file.h:   LGPL-2.1-or-later
# src/parsers/funcexpr.c:   LGPL-2.1-or-later
# src/parsers/funcexpr.h:   LGPL-2.1-or-later
# src/parsers/ifupdown.c:   LGPL-2.1-or-later
# src/parsers/ifupdown.h:   LGPL-2.1-or-later
# src/parsers/ini.c:    LGPL-2.1-or-later
# src/parsers/ini.h:    LGPL-2.1-or-later
# src/parsers/iproute.c:    LGPL-2.1-or-later
# src/parsers/iproute.h:    LGPL-2.1-or-later
# src/parsers/ipsec.c:  LGPL-2.1-or-later
# src/parsers/ipsec.h:  LGPL-2.1-or-later
# src/parsers/iptables.c:   LGPL-2.1-or-later
# src/parsers/iptables.h:   LGPL-2.1-or-later
# src/parsers/mgetty.c: LGPL-2.1-or-later
# src/parsers/mgetty.h: LGPL-2.1-or-later
# src/parsers/options.c:    LGPL-2.1-or-later
# src/parsers/options.h:    LGPL-2.1-or-later
# src/parsers/pair.c:   LGPL-2.1-or-later
# src/parsers/pair.h:   LGPL-2.1-or-later
# src/parsers/properties.c: LGPL-2.1-or-later
# src/parsers/properties.h: LGPL-2.1-or-later
# src/parsers/pslave.c: LGPL-2.1-or-later
# src/parsers/pslave.h: LGPL-2.1-or-later
# src/parsers/ppp.c:    LGPL-2.1-or-later
# src/parsers/ppp.h:    LGPL-2.1-or-later
# src/parsers/python.c: LGPL-2.1-or-later
# src/parsers/python.h: LGPL-2.1-or-later
# src/parsers/route.c:  LGPL-2.1-or-later
# src/parsers/route.h:  LGPL-2.1-or-later
# src/parsers/shell.c:  LGPL-2.1-or-later
# src/parsers/shell.h:  LGPL-2.1-or-later
# src/parsers/snmpd.c:  LGPL-2.1-or-later
# src/parsers/snmpd.h:  LGPL-2.1-or-later
# src/parsers/syslogng.c:   LGPL-2.1-or-later
# src/parsers/syslogng.h:   LGPL-2.1-or-later
# src/parsers/table.c:  LGPL-2.1-or-later
# src/parsers/table.h:  LGPL-2.1-or-later
# src/parsers/tz.c:     LGPL-2.1-or-later
# src/parsers/tz.h:     LGPL-2.1-or-later
# src/strutils.c:       LGPL-2.1-or-later
# src/strutils.h:       LGPL-2.1-or-later
# src/parsers/xinetd.c: LGPL-2.1-or-later
# src/parsers/xinetd.h: LGPL-2.1-or-later
## Unbundled
# aclocal.m4:           FSFULLRWD AND GPL-2.0-or-later WITH Autoconf-exception-generic AND FSFULLR
# config.guess:         GPL-2.0-or-later WITH Autoconf-exception-generic
# config.sub:           GPL-2.0-or-later WITH Autoconf-exception-generic
# configure:            FSFUL AND GPL-2.0-or-later WITH Autoconf-exception-generic
# debian/Makefile.in:   FSFULLRWD
# depcomp:              GPL-2.0-or-later WITH Autoconf-exception-generic
# doc/Makefile.in:      FSFULLRWD
# examples/Makefile.in: FSFULLRWD
# INSTALL:              FSFUL
# install-sh:           X11
# ltmain.sh:            GPL-2.0-or-later WITH Autoconf-exception-generic
# Makefile.in:          FSFULLRWD
# missing:              GPL-2.0-or-later WITH Autoconf-exception-generic
# src/Makefile.in:      FSFULLRWD
# src/parsers/Makefile.in:  FSFULLRWD
License:    LGPL-2.1-or-later
SourceLicense:  LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-2.0-or-later WITH Autoconf-exception-generic AND X11 AND FSFULLRWD AND FSFULLR AND FSFUL
# The code.google.com home is dead. There is
# <https://github.com/lipnitsk/llconf> but its 0.4.6 archive contains some
# additional files (e.g. src/parsers/cron.c copied into src/cron.c with
# changes license text.)
URL:        http://code.google.com/p/%{name}/
Source0:    http://%{name}.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:     llconf-0.4.6-Install-parsers-headers-into-subdirectory.patch
Patch1:     llconf-0.4.6-Unify-paths-in-examples.patch
# Fix a use-after-free in cnf_del_branch(),
# <https://github.com/lipnitsk/llconf/commit/aa33098dbe1246bc4d19843a63f25f799442f74a>
Patch2:     llconf-0.4.6-llconf-entry-fix-use-after-free-condition.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}

%description
llconf (loss-less configuration) tool is meant as a middle ware to unify
control over configuration files. It tries to parse different
configuration files using different modules, and rewrite them after
applying changes, without destroying user changes and comments, so
that it is still possible to edit the files with a common text editor.


%package libs
Summary:    Loss-less configuration file parser library

%description libs
llconf (loss-less configuration) is meant as a middle ware to unify
control over configuration files. It tries to parse different
configuration files using different modules, and rewrite them after
applying changes, without destroying user changes and comments, so
that it is still possible to edit the files with a common text editor.


%package devel
Summary:    Development files for %{name}
License:    LGPL-2.1-or-later AND GPL-2.0-or-later
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}
Requires:   pkgconfig

%description devel
Libraries and header files needed for developing applications that use
%{name}.


%prep
%autosetup -p1
# Remove bundled and pregenerated files
rm aclocal.m4 config.guess config.sub configure depcomp debian/Makefile.in \
    doc/Makefile.in examples/Makefile.in INSTALL install-sh ltmain.sh \
    Makefile.in missing mkinstalldirs src/Makefile.in src/parsers/Makefile.in
# Regenerate build scripts
libtoolize -fi
autoreconf -i
chmod -x examples/wizard

%build
%configure --disable-static
%{make_build}
make -C doc doxygen

%install
%{make_install}
find "$RPM_BUILD_ROOT" -name '*.la' -delete

%ldconfig_scriptlets libs


%files
%doc examples/etc examples/wizard README.llconf
%{_bindir}/%{name}

%files libs
%license COPYING
%doc README
%{_libdir}/libllconf.so.0{,.*}

%files devel
%doc examples/example.c doc/html
%{_includedir}/%{name}
%{_libdir}/libllconf.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Mar 24 2026 Petr Pisar <ppisar@redhat.com> - 0.4.6-32
- Correct a license tag

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.6-28
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Petr Pisar <ppisar@redhat.com> - 0.4.6-13
- Modernize spec file
- Fix a use-after-free in cnf_del_branch()

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Petr Pisar <ppisar@redhat.com> - 0.4.6-5
- Allow autoreconf to install missing files (bug #1106112)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Apr 27 2011 Petr Pisar <ppisar@redhat.com> - 0.4.6-1
- Version 0.4.6 packaged
- Upgrade libtool to get rid of useless RPATH
- Do not install libtool archives
- Install additional documentation

