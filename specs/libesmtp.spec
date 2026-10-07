Summary:        SMTP client library
Name:           libesmtp
Version:        1.1.0
Release:        1%{?dist}
License:        LGPL-2.1-or-later
Source:         https://github.com/libesmtp/libESMTP/archive/v%{version}/libESMTP-%{version}.tar.gz
URL:            https://libesmtp.github.io/
BuildRequires:  gcc
BuildRequires:  pkgconfig(openssl)
BuildRequires:  meson
# Fix build with OpenSSL 4.0 opaque ASN1_STRING
Patch:          https://github.com/libesmtp/libESMTP/pull/34.patch
# Debian patches
Patch:          1001-meson-build-soname.patch
Patch:          1003-default-source.patch

%description
LibESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA) such as
Exim. It may be used as part of a Mail User Agent (MUA) or another
program that must be able to post electronic mail but where mail
functionality is not the program's primary purpose.

%package devel
Summary: Headers and development libraries for libESMTP
# example file is under the GPLv2+
License: LGPL-2.1-or-later AND GPL-2.0-or-later
Requires: %{name} = %{version}-%{release}, openssl-devel

%description devel
LibESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA) such as
Exim.

The libesmtp-devel package contains headers and development libraries
necessary for building programs against libesmtp.

%prep
%autosetup -n libESMTP-%{version} -p1

%build
%meson
%meson_build

# deprecated; still used by esmtp
cat << "EOF" > libesmtp-config
#! /bin/sh
exec pkg-config "$@" libesmtp-1.0
EOF

%install
%meson_install
install -p -m755 -D -t %{buildroot}%{_bindir} libesmtp-config

%files
%doc README.md
%license LICENSE
%{_libdir}/libesmtp.so.6{,.*}
%{_libdir}/esmtp-plugins-6.*

%files devel
%doc examples
%license COPYING.GPL
%{_bindir}/libesmtp-config
%{_prefix}/include/*
%{_libdir}/libesmtp.so
%{_libdir}/pkgconfig/libesmtp-1.0.pc

%changelog
* Fri Aug 28 2026 Yaakov Selkowitz <yselkowi@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jun 12 2026 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.6-36
- Rebuilt for openssl 4.0

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.6-32
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Florian Weimer <fweimer@redhat.com> - 1.0.6-26
- C99 compatibility fix for the configure script

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.0.6-23
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Pawel Salek <salek@kth.se> - 1.0.6-16
- apply the ssl patch from https://bugzilla.redhat.com/show_bug.cgi?id=1483350

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec  3 2010 Pawel Salek <pawsa@theochem.kth.se> - 1.0.6-1
- update to upstream 1.0.6

* Sat Jun 12 2010 Pawel Salek <pawsa@theochem.kth.se> - 1.0.4-14

- fix bug 599428: use 'version' macro instead of '_version'.
- Use SSL patch by Ludwig Nussel of SUSE (bugzilla att id 399130).

* Tue Mar  9 2010 Pawel Salek <pawsa@theochem.kth.se> - 1.0.4-13
- fix CVE-2009-2408 (#571817).

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.0.4-12
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.0.4-9
- rebuild with new openssl

* Sat Nov  1 2008 Manuel "lonely wolf" Wolfshant <wolfy@fedoraproject.org> - 1.0.4-8
- do not package libtool files from the plugin directory

* Fri Apr  4 2008 Pawel Salek <pawsa@theochem.kth.se> - 1.0.4-7
- attempt at multilib support (#342011).

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.4-6
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.0.4-5
 - Rebuild for deps

* Sun Nov 18 2007 Patrice Dumas <pertusus@free.fr> - 1.0.4-4
- use --disable-static

* Thu Nov 15 2007 Pawel Salek <pawsa@theochem.kth.se> - 1.0.4-3
- drop static libs as suggested in bug 377731.

* Mon Sep 11 2006 Pawel Salek <pawsa@theochem.kth.se> - 1.0.4-2
- rebuild for FC6.

* Fri Mar 24 2006 Pawel Salek <pawsa@theochem.kth.se> - 1.0.4-1
- Update to 1.0.4 - redo build and ssl patches.

* Wed Mar  1 2006 Pawel Salek <pawsa@theochem.kth.se> - 1.0.3r1-8
- Rebuild for Fedora Extras 5

* Sun Dec  4 2005 Pawel Salek <pawsa@theochem.kth.se> - 1.0.3r1-7
- Fix bug 173332 completely, including licence issues.

* Thu Nov 17 2005 Pawel Salek <pawsa@theochem.kth.se> - 1.0.3r1-6
- fix #173332.

* Tue Nov 15 2005 Dan Williams <dcbw@redhat.com> - 1.0.3r1-5
- rebuild against newer crypto libs

* Wed Oct 19 2005 Pawel Salek <pawsa@theochem.kth.se> - 1.0.3r1-4
- fix crashes on certificates with subjectAltName extension. Fix #166844.

* Sun Jun 12 2005 Pawel Salek <pawsa@theochem.kth.se> - 1.0.3r1-3
- Add libesmtp-build.patch - fix building under FC4.

* Thu Sep 30 2004 Miloslav Trmac <mitr@redhat.com> - 1.0.3r1-2
- Include libesmtp-config in libesmtp-devel (#125426, patch by Robert Scheck)

* Tue Jul 13 2004 John Dennis <jdennis@redhat.com> 1.0.3r1-1
- bring up to latest upstream release

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 29 2004 Bill Nottingham <notting@redhat.com> 1.0.2-1
- upgrade to 1.0.2 (#113894)

* Fri Oct  3 2003 Bill Nottingham <notting@redhat.com> 1.0.1-1
- update to 1.0.1, rebuild to fix some broken 64-bit libs

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 0.8.12-4
- include compilation flags for openssl as defined for pkg-config
- don't blow up on compile because key schedules aren't arrays

* Tue Nov  5 2002 Bill Nottingham <notting@redhat.com> 0.8.12-3
- build on various platforms

* Tue Jul 23 2002 Bill Nottingham <notting@redhat.com> 0.8.12-2
- fix broken lib (no pthread dependency)
