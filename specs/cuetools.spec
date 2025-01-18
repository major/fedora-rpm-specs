Name:    cuetools
Version: 1.4.1
Release: 10%{?dist}
Summary: Utilities to work with cue and TOC files
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://github.com/svend/cuetools
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:  %{url}/commit/fa3b2f4.patch#/cueprint-fix-typo-in-performer-tag.patch
Patch3:  0003-cuetag.sh-Correct-typo-in-error-output.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: flex
BuildRequires: bison
BuildRequires: gcc
BuildRequires: make

%description
Cuetools is a set of utilities for working with cue files and TOC files.
It includes programs for conversion between the formats, file renaming based
on cue/TOC information, and track breakpoint printing. 

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%files
%doc NEWS README.md TODO doc/formats.txt
%license COPYING
%{_bindir}/cue*
%{_mandir}/man1/cue*.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.1-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 05 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1
- Switch to the new upstream URL
- Drop unnecessary patches
- Update spec for the current packaging guidelines

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.27.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.26.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.25.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.24.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.23.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.22.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Paul Komkoff <i@stingr.net> - 1.4.0-0.21.svn305
- BuildRequires: gcc (bz#1603725)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.20.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.19.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.18.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.17.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.16.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.15.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-0.14.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-0.13.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-0.12.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-0.11.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-0.10.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-0.9.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-0.8.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 01 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.4.0-0.7.svn305
- Fix up timestamps on pre-generated sources (Fix FTBFS BZ#716187, BZ#660830).

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-0.6.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-0.5.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 08 2009 Todd Zullinger <tmz@pobox.com> - 1.4.0-0.4.svn305
- cuetag.sh: Fix metaflac options for flac >= 1.1.3 (bug 488586)
- cuetag.sh: Fix handling of files with spaces (bug 499910)
- cuetag.sh: Correct typo in error output

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-0.3.svn305
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar 26 2008 Paul P. Komkoff Jr <i@stingr.net> - 1.4.0-0.2.svn305
- add COPYING and doc/formats.txt
- remove *.so

* Tue Mar 4 2008 Paul P. Komkoff Jr <i@stingr.net> - 1.4.0-0.1.svn305
- update base code to svn305
- add PIE compilation options
- change library to be .so, link tools agains it, this gives us 3x size
  reduction
- fix issues when you're trying to process 99 CD tracks
  http://developer.berlios.de/bugs/?func=detailbug&bug_id=9592&group_id=2130
- fix some minor issues with build system

* Wed Jul 4 2007 Marius ROMAN <marius.roman@gmail.com> 1.3.1-1
- Initial RPM release
