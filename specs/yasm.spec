%global git 1
%global commit 9defefae9fbcb6958cddbfa778c1ea8605da8b8b
%global date 20230922
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary: Modular Assembler
Name: yasm
Version: 1.3.0^%{date}git%{shortcommit}
Release: 3%{?dist}
# See COPYING for the detail, there is quite a lot!
# Bitvect is (GPL-1.0-or-later AND GPL-2.0-or-later OR Artistic-1.0-Perl OR LGPL-2.0-or-later
# Everything else is BSD. Either 2 or 3 clause.
License: BSD-2-Clause AND BSD-3-Clause AND (GPL-1.0-or-later AND GPL-2.0-or-later OR Artistic-1.0-Perl OR LGPL-2.0-or-later)

URL: http://yasm.tortall.net/
%if 0%{?git}
Source: https://github.com/yasm/yasm/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# https://github.com/yasm/yasm/issues/270
Patch0: yasm-tests.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: python3
%else
Source: http://www.tortall.net/projects/yasm/releases/yasm-%{version}.tar.gz
%endif

BuildRequires: make
BuildRequires:  gcc
BuildRequires: bison
BuildRequires: byacc
BuildRequires: gettext-devel
BuildRequires: xmlto
Provides: bundled(md5-plumb)

%description
Yasm is a complete rewrite of the NASM assembler under the "new" BSD License
(some portions are under other licenses, see COPYING for details). It is
designed from the ground up to allow for multiple assembler syntaxes to be
supported (eg, NASM, TASM, GAS, etc.) in addition to multiple output object
formats and even multiple instruction sets. Another primary module of the
overall design is an optimizer module.


%package devel
Summary: Header files and static libraries for the yasm Modular Assembler
Requires: %{name} = %{version}-%{release}
Provides: %{name}-static = %{version}-%{release}
Provides: bundled(md5-plumb)

%description devel
Yasm is a complete rewrite of the NASM assembler under the "new" BSD License
(some portions are under other licenses, see COPYING for details). It is
designed from the ground up to allow for multiple assembler syntaxes to be
supported (eg, NASM, TASM, GAS, etc.) in addition to multiple output object
formats and even multiple instruction sets. Another primary module of the
overall design is an optimizer module.
Install this package if you need to rebuild applications that use yasm.


%prep
%if 0%{?git}
%setup -q -n %{name}-%{commit}
%ifarch i686
%patch 0 -p1
%endif
autoreconf -I m4 -fiv
%else
%setup -q
%endif


%build
%configure
%make_build


%install
%make_install


%check
# tests must be run sequentially
# https://github.com/yasm/yasm/issues/269
make check

%files
%license Artistic.txt BSD.txt COPYING GNU_GPL-2.0 GNU_LGPL-2.0
%doc AUTHORS
%{_bindir}/vsyasm
%{_bindir}/yasm
%{_bindir}/ytasm
%{_mandir}/man1/yasm.1*

%files devel
%{_includedir}/libyasm/
%{_includedir}/libyasm-stdint.h
%{_includedir}/libyasm.h
%{_libdir}/libyasm.a
%{_mandir}/man7/yasm_*.7*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0^20230922git9defefa-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0^20230922git9defefa-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 21 2024 Dominik Mierzejewski <dominik@greysector.net> - 1.3.0^20230922git9defefa-1
- update to latest git snapshot
- drop obsolete patch
- use modern macros
- run the test suite in %check
- fixes: CVE-2023-37732 CVE-2023-31975 CVE-2021-33454

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 22 2023 Nick Clifton  <nickc@redhat.com> - 1.3.0-19
- Spec File: Migrated to SPDX license.  (#2222115)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 01 2015 Christian Dersch <lupinix@mailbox.org> - 1.3.0-2
- Fixed bogus date (RHBZ #1190908)

* Wed Sep 30 2015 Christian Dersch <lupinix@mailbox.org> - 1.3.0-1
- new version
- spec cleanup

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 17 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-3
- Add missing Provides: bundled(md5-plumb)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 15 2012 Matthias Saou <matthias@saou.eu> 1.2.0-1
- Update to 1.2.0 (#750234).
- Minor spec file cleanups (keep EPEL compatibility, #802162).

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 15 2010 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Update to 1.1.0 (#622240).

* Thu Jul 29 2010 Matthias Saou <http://freshrpms.net/> 1.0.1-2
- Provide static sub-package from devel (#609626).

* Sun May 23 2010 Matthias Saou <http://freshrpms.net/> 1.0.1-1
- Update to 1.0.1 (#593250).

* Wed Apr 28 2010 Matthias Saou <http://freshrpms.net/> 1.0.0-1
- Update to 1.0.0 (#580872).
- Include new vsyasm binary.

* Mon Dec  7 2009 Matthias Saou <http://freshrpms.net/> 0.8.0-1
- Update to 0.8.0 (#523729).
- Include new ytasm binary.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 24 2008 Matthias Saou <http://freshrpms.net/> 0.7.2-1
- Update to 0.7.2.
- Remove useless /sbin/ldconfig calls, as we don't ship any shared library.
- Update summary.

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.7.1-2
- fix license tag so that it doesn't trigger a false positive on the check
  script.

* Tue May 20 2008 Matthias Saou <http://freshrpms.net/> 0.7.1-1
- Update to 0.7.1.

* Tue May 13 2008 Matthias Saou <http://freshrpms.net/> 0.7.0-1
- Update to 0.7.0.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Mon Sep 24 2007 Matthias Saou <http://freshrpms.net/> 0.6.2-1
- Update to 0.6.2.

* Thu Aug 23 2007 Matthias Saou <http://freshrpms.net/> 0.6.1-3
- Rebuild for new BuildID feature.

* Fri Aug  3 2007 Matthias Saou <http://freshrpms.net/> 0.6.1-2
- Update License field, it wasn't simply "BSD"...

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 0.6.1-1
- Update to 0.6.1.

* Sun Feb 25 2007 Matthias Saou <http://freshrpms.net/> 0.6.0-1
- Update to 0.6.0.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 0.5.0-2
- FC6 rebuild.
- Require the same release in the devel sub-package.

* Fri Jul 14 2006 Matthias Saou <http://freshrpms.net/> 0.5.0-1
- Update to 0.5.0.
- Remove empty files from %%doc.
- There are no more shared libraries, only a static one, so update %%files.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 0.4.0-6
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 0.4.0-5
- Rebuild for new gcc/glibc.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.4.0-4
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Feb 14 2005 David Woodhouse <dwmw2@infradead.org> 0.4.0-2
- Fix corruption in genmacro

* Fri Jan 28 2005 Matthias Saou <http://freshrpms.net/> 0.4.0-1
- Initial RPM release.

