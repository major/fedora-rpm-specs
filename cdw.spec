Name: cdw
Version: 0.8.1
Release: 1%{?dist}
Summary: Front-end for tools used for burning data CD/DVD
License: GPLv2+ 
URL: http://cdw.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: 0001-add-formatstring.patch

BuildRequires: gcc
BuildRequires: libcdio-devel, ncurses-devel, libburn-devel
BuildRequires: make
#It does not make sense install cdw without the packages below:
Requires: dvd+rw-tools,wodim,genisoimage,xorriso 

%description
cdw is a ncurses based front-end for some command-line tools used for burning
data CD and DVD discs and for related tasks. The tools are: cdrecord/wodim,
mkisofs/genisoimage, growisofs, dvd+rw-mediainfo, dvd+rw-format, xorriso.
cdw is able to rip tracks from your audio CD to raw audio files.
Limited support for copying content of data CD and DVD discs to image files
is also provided. cdw can verify correctness of writing ISO9660 image to
CD or DVD disc using md5sum or some of  programs that verifies SHA hashes.

%prep
%autosetup -p1

%build
export CXXFLAGS="%{optflags}" LIBS="-lm"
%configure
%make_build

%install
%make_install

%check
make check LIBS="-lm"

%files
%{_bindir}/*
%doc COPYING AUTHORS ChangeLog NEWS README THANKS
%{_mandir}/man1/*

%changelog
* Tue Feb 21 2023 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.1-1
- Update to 0.8.1 fix FTBFS rhbz#2113143

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Adrian Reber <adrian@lisas.de> - 0.7.1-23
- Rebuilt for libcdio-2.1.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Adrian Reber <adrian@lisas.de> - 0.7.1-17
- Rebuilt for libcdio-2.0.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Adrian Reber <adrian@lisas.de> - 0.7.1-13
- Rebuilt for new libcdio-0.94

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 11 2014 Adrian Reber <adrian@lisas.de> - 0.7.1-10
- Rebuilt for new libcdio-0.93

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 16 2013 Adrian Reber <adrian@lisas.de> - 0.7.1-7
- Rebuilt for new libcdio-0.92

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Adrian Reber <adrian@lisas.de> - 0.7.1-4
- Rebuilt for new libcdio-0.90

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

*Fri Jun 22 2012 Sergio Belkin <sebelk@fedoraproject.org> 0.7.1-2
- Fixed changelog and missing sources

*Wed Jun 20 2012 Sergio Belkin <sebelk@fedoraproject.org> 0.7.1-1
- Lots of bugfixes and improvements about of interface and workings
- better detection of external tools
- COPYING file have updated the FSF address

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
 
*Mon Oct 17 2011 Sergio Belkin <sebelk@fedoraproject.org> 0.7.0-2
- Fixed FSF address in COPYING file
- Minor change in Description

*Fri Oct 14 2011 Sergio Belkin <sebelk@fedoraproject.org> 0.7.0-1
- Adding limited support for xorriso
- Adding new compile-time and run-time dependency: libburn
- Adding support for more digest (checksum) tools: sha1sum, sha224sum,
  sha256sum, sha384sum, sha512sum;
- Fixing verification of ISO images failures
- Several fixes and UI improvements
- Improved recognition of track formats (TAO/DAO/SAO) supported
 by disc/drive when burning with cdrecord;
- Adding (partial) recognition of capacity of CD/DVD discs

*Mon Feb 28 2011 Sergio Belkin <sebelk@fedoraproject.org> 0.6.0-8
- Changed email address
- Fixes about timestamp and LIBS variables really applied

*Mon Feb 28 2011 Sergio Belkin <sebelk@gmail.com> 0.6.0-7
- Fixed license
- Fixed timestamp in %%install section
- Fixed LIBS variable
- Fixed previous changelog

* Sat Feb 26 2011 Sergio Belkin <sebelk@gmail.com> 0.6.0-6
- Fixed spaces between entries

* Tue Feb 22 2011 Sergio Belkin <sebelk@gmail.com> 0.6.0-5
- Minor change in BuildRequires
- Fixed typo in Requires and comment
- Added %%check section

* Sat Feb 19 2011 Sergio Belkin <sebelk@gmail.com> 0.6.0-4
- Added %%doc entry, removed, removed redundant attr

* Fri Feb 18 2011 Sergio Belkin <sebelk@gmail.com> 0.6.0-3
- Removed %%clean section 

* Thu Feb 17 2011 Sergio Belkin <sebelk@gmail.com> 0.6.0-2
- Replaced LDFLAGS for LIBS variable

* Tue Feb 01 2011 Sergio Belkin <sebelk@gmail.com> 0.6.0-1
- First public cdw RPM for fedora
