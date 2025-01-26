# License
# ===========
#
# The GNUstep libraries and library resources are covered under the GNU
# Lesser Public License.  This means you can use these libraries in any
# program (even non-free programs).

# GNUstep tools, test programs, and other files are covered under the
# GNU Public License.

Name: gnustep-base
Version: 1.30.0
Release: 7%{?dist}
License: GPL-3.0-or-later and LGPL-2.0-or-later
Summary: GNUstep Base library package
URL: http://www.gnustep.org/
Source0: ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=1179297
Patch0: %{name}-use_system-wide_crypto-policies.patch

Patch1: %{name}-fix_GCC15.patch

BuildRequires: gcc
BuildRequires: gcc-objc
BuildRequires: libffi-devel >= 3.0.9
BuildRequires: gnutls-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: pkgconfig
BuildRequires: gnustep-make >= 2.9.2
BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: gmp-devel
BuildRequires: texi2html texinfo-tex
BuildRequires: libicu-devel
BuildRequires: texi2html

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: make

Conflicts: libFoundation

%description
The GNUstep Base Library is a powerful fast library of general-purpose,
non-graphical Objective C classes, inspired by the superb OpenStep API but
implementing Apple and GNU additions to the API as well.  It includes for
example classes for unicode strings, arrays, dictionaries, sets, byte
streams, typed coders, invocations, notifications, notification dispatchers,
scanners, tasks, files, networking, threading, remote object messaging
support (distributed objects), event loops, loadable bundles, attributed
unicode strings, xml, mime, user defaults. This package includes development
headers too.


%package libs
Summary: GNUStep Base Libraries
Requires: gnustep-make%{?_isa} >= 2.9.2

%description libs
The GNUstep Base Library is a powerful fast library of general-purpose,
non-graphical Objective C classes, inspired by the superb OpenStep API but
implementing Apple and GNU additions to the API as well.  It includes for
example classes for unicode strings, arrays, dictionaries, sets, byte
streams, typed coders, invocations, notifications, notification dispatchers,
scanners, tasks, files, networking, threading, remote object messaging
support (distributed objects), event loops, loadable bundles, attributed
unicode strings, xml, mime, user defaults. This package includes development
headers too.
This packages contains the run-time libraries for %{name}.


%package devel
Summary: Header of the GNUstep Base library packes
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files of the gnustep-base package.


%package doc
Summary: Documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gnustep-filesystem

%description doc
The GNUstep Base Library is a powerful fast library of general-purpose,
non-graphical Objective C classes, inspired by the superb OpenStep API but
implementing Apple and GNU additions to the API as well.  It includes for
example classes for unicode strings, arrays, dictionaries, sets, byte
streams, typed coders, invocations, notifications, notification dispatchers,
scanners, tasks, files, networking, threading, remote object messaging
support (distributed objects), event loops, loadable bundles, attributed
unicode strings, xml, mime, user defaults. This package includes development
headers too.
This package contains the documentation for %{name}

%prep
%autosetup -p1

iconv -f iso-8859-1 -t utf-8 ChangeLog.2 -o ChangeLog.2.utf8
mv ChangeLog.2.utf8 ChangeLog.2

%build
ffi_include=$(pkg-config --cflags-only-I libffi | sed -e 's/^\-\I//')
export LDFLAGS="%{__global_ldflags}"
export OBJCFLAGS="-std=gnu17"
%gnustep_configure --disable-ffcall --with-ffi-include="$ffi_include"

%gnustep_make -n

%install
%gnustep_install -n

# Rename pl to pllist to fix naming conflict
mv ${RPM_BUILD_ROOT}%{_bindir}/pl ${RPM_BUILD_ROOT}%{_bindir}/pllist

rm -f Examples/.cvsignore
rm -f Examples/.gdbinit

# We need a modified GNUstep.conf, because the DTDs are install not
# on there real destination

sed -e "s|GNUSTEP_SYSTEM_LIBRARY=|GNUSTEP_SYSTEM_LIBRARY=$RPM_BUILD_ROOT|" \
    -e "s|GNUSTEP_SYSTEM_HEADERS=|GNUSTEP_SYSTEM_HEADERS=$RPM_BUILD_ROOT|" \
    %{_sysconfdir}/GNUstep/GNUstep.conf >GNUstep.conf

export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
export GNUSTEP_CONFIG_FILE=$(pwd)/GNUstep.conf

%gnustep_makedoc
%gnustep_installdoc

%files
%{_bindir}/HTMLLinker
%{_bindir}/autogsdoc
%{_bindir}/cvtenc
%{_bindir}/defaults
%{_bindir}/gdnc
%{_bindir}/gdomap
%{_bindir}/gspath
%{_bindir}/make_strings
%{_bindir}/pl2link
%{_bindir}/pldes
%{_bindir}/plget
%{_bindir}/pllist
%{_bindir}/plmerge
%{_bindir}/plparse
%{_bindir}/plser
%{_bindir}/plutil
%{_bindir}/sfparse
%{_bindir}/xmlparse
%{_mandir}/man1/*
%{_mandir}/man8/*
%{gnustep_dtddir}/

%files libs
%doc ANNOUNCE ChangeLog* NEWS README*
%license COPYING.LIB COPYINGv3
%{gnustep_libraries}/
%{_libdir}/libgnustep-base.so.1.30
%{_libdir}/libgnustep-base.so.%{version}

%files devel
%{_includedir}/Foundation/
%{_includedir}/GNUstepBase/
%{_libdir}/libgnustep-base.so
%{_libdir}/pkgconfig/gnustep-base.pc
%{gnustep_additional}/base.make
%doc Examples

%files doc
%{_infodir}/*
%dir %{_datadir}/GNUstep/Documentation
%{_datadir}/GNUstep/Documentation/*

%changelog
* Fri Jan 24 2025 Antonio Trande <sagitter@fedoraproject.org> - 1.30.0-7
- Fix GCC15 builds

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 1.30.0-5
- Rebuild for ICU 76

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 20 2024 Antonio Trande <sagitter@fedoraproject.org> - 1.30.0-3
- Fix gnustep-make name

* Wed Jun 19 2024 Antonio Trande <sagitter@fedoraproject.org> - 1.30.0-2
- gnustep-base-libs now requires gnustep-make (rhbz#2283758)

* Sat Jun 01 2024 Antonio Trande <sagitter@fedoraproject.org> - 1.30.0-1
- Release 1.30.0

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 1.29.0-4
- Rebuild for ICU 74

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 19 2023 Antonio Trande <sagitter@fedoraproject.org> - 1.29.0-1
- Release 1.29.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 1.28.0-11
- Rebuilt for ICU 73.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 1.28.0-9
- Rebuild for ICU 72

* Wed Nov 23 2022 Florian Weimer <fweimer@redhat.com> - 1.28.0-8
- Avoid C89-only constructs during the config stage

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.28.0-7
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 1.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 1.28.0-2
- Rebuild for ICU 69

* Sat May 15 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.28.0-1
- Release 1.28.0

* Sat Apr 03 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.27.0-6
- Rebuild for gnustep-make (RHBZ #1923589)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Pete Walter <pwalter@fedoraproject.org> - 1.27.0-2
- Rebuild for ICU 67

* Thu Apr 16 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.27.0-1
- Release 1.27.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 1.26.0-2
- Rebuild for ICU 65

* Sun Aug 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.26.0-1
- Release 1.26.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.25.0-13
- Remove obsolete requirements for %%post/%%preun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 1.25.0-11
- Rebuild for ICU 63

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 1.25.0-9
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.25.0-8
- Rebuild for ICU 61.1

* Fri Feb 16 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.25.0-7
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.25.0-5
- Rebuild for ICU 60.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.25.0-2
- Fix Requires

* Sat Apr 15 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.25.0-1
- Update to 1.25.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 21 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.24.9-1
- Update to 1.24.9
- Utilize system-wide crypto-policies (bz#1179297)

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 1.24.7-6
- rebuild for ICU 57.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 1.24.7-4
- rebuild for ICU 56.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 1.24.7-2
- rebuild for ICU 54.1

* Sun Oct 19 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1.24.7-1
- New bugfixing release from upstream
- Add texi2html as a BR

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 1.24.6-6
- rebuild for ICU 53.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Tomáš Mráz <tmraz@redhat.com> - 1.24.6-3
- Rebuild for new libgcrypt

* Thu Feb 13 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1.24.6-2
- Rebuilt agains new icu release

* Sun Jan 12 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1.24.6-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 15 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.24.4-7
- Splitt of gnustep-base-libs (ä963025)

* Tue May  7 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.24.4-6
- Place DTDs subdir back to %%{gnustep_libdir} (#960313)

* Fri Apr  5 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.24.4-5
- Rework for change gnustep macro definitons

* Thu Apr  4 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.24.4-4
- Built for new gnustep-make release

* Mon Apr  1 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.24.4-3
- Usage of gnustep rpm macros

* Sun Mar 31 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.24.4-2
- Usage of gnustep rpm macros
- MOve Req. to gnustep-make to devel sub-package

* Sat Mar 30 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.24.4-1
- New upstream release
- Remove xml patch
- Add BR libicu-devel

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Jochen Schmitt <Jochen herr-schmitt de> - 1.24.0-3
- Add patch to fix a issue with newer releases of libxml2
- Romove obsoletes items from the SPEC file 

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb  8 2012 Jochen Schmitt <Jochen herr-schmitt de> 1.24.0-1
- New upstream release

* Wed Jan  4 2012 Jochen Schmitt <JOchen herr-schmitt de> 1.23.0-1.3
- Fix dependencies issues on rawhide (libobjc.so.3)

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.23.0-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 1.23.0-1.1
- rebuild with new gmp

* Sun Oct  9 2011 Jochen Schmitt <Jochen herr-schmitt de> 1.23.0-1
- New upstream release

* Wed Apr 27 2011 Jochen Schmitt <JOchen.herr-schmitt de> 1.22.0-2
- Remove comment command

* Wed Apr 27 2011 Jochen Schmitt <Johen herr-schmitt de> 1.22-1
- New upstream release which is compatible with gcc-4.6

* Thu Feb 10 2011 Jochen Schmitt <Jochen herr-schmitt de> 1.22-0.20110210
- First unstable release working with gcc-4.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.20.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Jochen Schmitt <Jochen herr-schmitt de> 1.20.1-3
- Rebuild for new libobjc
- Replace objc/objc-api.h to objc/runtime.h

* Tue Jul  6 2010 Jochen Schmitt <Jochen herr-schmitt de> 1.20.1-2
- Parallels build for gnustep

* Mon Jun 21 2010 Jochen Schmitt <Jochen herr-schmitt de> 1.20.1-1
- New upstream release

* Thu May 13 2010 Jochen Schmitt <Jochen herr-schmitt de> 1.20.0-1
- New upatream release which fix CVE-2010-1457 and CVE-2010-1620 (#591602)

* Mon Nov 30 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.18.0-8
- Remove strace command

* Thu Nov 26 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.18.0-7
- Using temp. modified GNUstep.conf to access to DTDs (#539092)

* Thu Nov  5 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.18.0-6
- Add a conflict agains libFoundation

* Wed Sep 16 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.18.0-5
- Renove suid-bit on gdomap
- Create separate doc subpackage
- Fix license tag

* Mon Sep 14 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.18.0-4
- Rebuild agains gnustep-make 2.2.0

* Thu Mar 26 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.18.0-3
- Set GNUSTEP_INSTALLATION_DOMAIN=SYSTEM for make install

* Wed Mar 25 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.18.0-2
- Specify installation-domain=SYSTEM
- fix UTF-8 issue in ChangeLog.2

* Wed Mar  4 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.18.0-1
- Fallback to last stable release

* Wed Mar  4 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.19.0-2
- Switch to libffi

* Tue Feb 17 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.19.0-1
- New upstream release

* Sun Dec  7 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.16.5-1
- Initional release
