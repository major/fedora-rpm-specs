Summary:        Rsync remote-delta algorithm library
Name:           librsync
Version:        2.3.4
Release:        7%{?dist}
License:        LGPL-2.1-or-later
URL:            https://librsync.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/librsync-%{version}.tar.gz
BuildRequires:  cmake >= 3.6
BuildRequires:  gcc
BuildRequires:  popt-devel
# Compression isn't functional: https://github.com/librsync/librsync/issues/8
#BuildRequires:  bzip2-devel
#BuildRequires:  zlib-devel

%description
librsync is a library for calculating and applying network deltas, with an
interface designed to ease integration into diverse network applications.

librsync encapsulates the core algorithms of the rsync protocol, which help
with efficient calculation of the differences between two files. The rsync
algorithm is different from most differencing algorithms because it does not
require the presence of the two files to calculate the delta. Instead, it
requires a set of checksums of each block of one file, which together form a
signature for that file. Blocks at any in the other file which have the same
checksum are likely to be identical, and whatever remains is the difference.

%package devel
Summary:        Headers and development libraries for librsync
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The librsync-devel package contains header files and library necessary for
developing programs based on librsync.

%if 0%{!?_without_doc:1}
%package doc
Summary:         Documentation files for %{name}
BuildArch:       noarch
BuildRequires:   doxygen
BuildRequires:   graphviz

%description doc
librsync is a library for calculating and applying network deltas, with an
interface designed to ease integration into diverse network applications.
This package contains the API documentation for developing applications that
use librsync.
%endif

%prep
%setup -q

%build
%cmake
%cmake_build

%if 0%{!?_without_doc:1}
%cmake_build --target doc
%endif

%install
%cmake_install

%check
%cmake_build --target check

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS.md README.md
%{_libdir}/%{name}.so.2*
%{_bindir}/rdiff
%{_mandir}/man1/rdiff.1*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{name}*
%{_mandir}/man3/%{name}.3*

%if 0%{!?_without_doc:1}
%files doc
%if 0%{?__cmake_in_source_build}%{?__cmake3_in_source_build}
%doc html
%else
%doc %{_vpath_builddir}/html
%endif
%endif

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 19 2023 Robert Scheck <robert@fedoraproject.org> 2.3.4-1
- Upgrade to 2.3.4 (#2170502 #c2)

* Sat Feb 18 2023 Robert Scheck <robert@fedoraproject.org> 2.3.3-1
- Upgrade to 2.3.3 (#2170502)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr 10 2021 Robert Scheck <robert@fedoraproject.org> 2.3.2-1
- Upgrade to 2.3.2 (#1948216)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Robert Scheck <robert@fedoraproject.org> 2.3.1-3
- Work around CMake out-of-source builds on all branches (#1864045)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Robert Scheck <robert@fedoraproject.org> 2.3.1-1
- Upgrade to 2.3.1

* Sat May 16 2020 Robert Scheck <robert@fedoraproject.org> 2.3.0-1
- Upgrade to 2.3.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 31 2019 Robert Scheck <robert@fedoraproject.org> 2.0.2-1
- Upgrade to 2.0.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Robert Scheck <robert@fedoraproject.org> 1.0.0-1
- Upgrade to 1.0.0 (#1126712)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 08 2013 Robert Scheck <robert@fedoraproject.org> 0.9.7-22
- Solved build failures with "-Werror=format-security" (#1037171)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Robert Scheck <robert@fedoraproject.org> 0.9.7-20
- Made autoreconf copying the missing auxiliary files (#914147)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 0.9.7-14
- Rebuilt against gcc 4.4 and rpm 4.6

* Sat Dec 20 2008 Robert Scheck <robert@fedoraproject.org> 0.9.7-13
- Run libtoolize before %%configure to avoid libtool 2.2 errors
- Added a patch to make rdiff aware of -i and -z getopt options
- Updated man page for how to use rdiff and removed a dead link

* Sun Feb 10 2008 Robert Scheck <robert@fedoraproject.org> 0.9.7-12
- Rebuilt against gcc 4.3
- Updated the source URL to match with the guidelines

* Tue Aug 28 2007 Robert Scheck <robert@fedoraproject.org> 0.9.7-11
- Updated the license tag according to the guidelines
- Buildrequire %%{_includedir}/popt.h for separate popt (#249352)

* Mon May 07 2007 Robert Scheck <robert@fedoraproject.org> 0.9.7-10
- rebuilt

* Thu Dec 14 2006 Robert Scheck <robert@fedoraproject.org> 0.9.7-9
- removed static library from librsync-devel (#213780)

* Mon Oct 09 2006 Gavin Henry <ghenry@suretecsystems.com> 0.9.7-8
- rebuilt

* Tue Oct 03 2006 Robert Scheck <robert@fedoraproject.org> 0.9.7-7
- rebuilt

* Mon Sep 25 2006 Robert Scheck <robert@fedoraproject.org> 0.9.7-6
- added an upstream patch to solve a lfs overflow (#207940)

* Wed Sep 20 2006 Robert Scheck <robert@fedoraproject.org> 0.9.7-5
- some spec file cleanup, added %%{?dist} and rebuild

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.9.7-4
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Jan 23 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.9.7-2
- Recreate autotools files with autoreconf to fix x86_64 build.

* Wed Nov 10 2004 Adrian Reber <adrian@lisas.de> - 0:0.9.7-0.fdr.1
- updated to 0.9.7 (#2248)
- changed source URL to be downloadable with wget

* Fri Aug 8 2003 Ben Escoto <bescoto@stanford.edu> 0.9.6-0.fdr.3
- Build no longer requires GNU tools
- Install shared library and rdiff executable by default

* Sun Jul 20 2003 Ben Escoto <bescoto@stanford.edu> 0.9.5.1-0.fdr.2
- Repackaged Laurent Papier's <papier@sdv.fr> rpm.
