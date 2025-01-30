Name:		kakasi
Version:	2.3.6
Release:	31%{?dist}
URL:		http://kakasi.namazu.org/
License:	GPL-2.0-or-later
BuildRequires:	autoconf automake libtool gettext-devel
BuildRequires: make

Source:	http://kakasi.namazu.org/stable/%{name}-%{version}.tar.xz
Patch4:		kakasi-multilib.patch
Patch5: kakasi-configure-c99.patch
Patch6:	%{name}-ftbfs.patch


Summary:	A Japanese character set conversion filter

%description
KAKASI is a filter for converting Kanji characters to Hiragana or
Katakana characters, or into Romaji (phonetic transcription of
Japanese pronunciation).

%package libs
Summary:	Libraries for KAKASI

%description libs
The kakasi-libs package contains the library file for KAKASI

%package devel
Summary:	Files for development of applications which will use KAKASI
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Conflicts:	%{name} < 2.3.6

%description devel
The kakasi-devel package contains the header file and library for
developing applications which will use the KAKASI Japanese character
set filter.


%package dict
Summary:	The base dictionary for KAKASI
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description dict
The kakasi-dict package contains the base dictionary for the KAKASI
Japanese character set filter.


%prep
%autosetup -p1
autoreconf -f -i

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# correct timestamp
touch -r kakasi-config.in $RPM_BUILD_ROOT%{_bindir}/kakasi-config

# remove the unnecesary files
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

mkdir -p $RPM_BUILD_ROOT%{_mandir}/ja/man1
iconv -f euc-jp -t utf-8 man/kakasi.1.ja > man/kakasi.1.ja.utf8 && touch -r man/kakasi.1.ja man/kakasi.1.ja.utf8 && install -m 0644 man/kakasi.1.ja.utf8 $RPM_BUILD_ROOT/%{_mandir}/ja/man1/kakasi.1


%ldconfig_scriptlets	libs

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%lang(ja) %doc README-ja
%dir %{_datadir}/kakasi
%{_bindir}/*
%exclude %{_bindir}/kakasi-config
%{_mandir}/man1/kakasi.1*
%{_mandir}/ja/man1/kakasi.1*
%{_datadir}/kakasi/itaijidict

%files libs
%license COPYING
%{_libdir}/libkakasi.so.*

%files devel
%license COPYING
%{_bindir}/kakasi-config
%{_libdir}/libkakasi.so
%{_mandir}/man1/kakasi-config.1*
%{_includedir}/libkakasi.h

%files dict
%license COPYING
%{_datadir}/kakasi/kanwadict


%changelog
* Tue Jan 28 2025 Akira TAGOH <tagoh@redhat.com> - 2.3.6-31
- Fix FTBFS
  Resolves: rhbz#2340685

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 15 2023 Florian Weimer <fweimer@redhat.com> - 2.3.6-25
- Port configure script to C99 (#2186999)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec  1 2022 Akira TAGOH <tagoh@redhat.com> - 2.3.6-23
- Convert License tag to SPDX.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Akira TAGOH <tagoh@redhat.com> - 2.3.6-18
- Fix FTBFS
  Resolves: rhbz#1863927

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Akira TAGOH <tagoh@redhat.com> - 2.3.6-11
- Modernize spec file.
- Use ldconfig rpm macro.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.3.6-10
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Akira TAGOH <tagoh@redhat.com> - 2.3.6-1
- New upstream release. (#1077558)

* Mon Feb 10 2014 Akira TAGOH <tagoh@redhat.com> - 2.3.5-1
- New upstream release. (#1063015)

* Tue Sep  3 2013 Akira TAGOH <tagoh@redhat.com> - 2.3.4-36
- Drop the older Obsoletes line. (#1002128)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Akira TAGOH <tagoh@redhat.com> - 2.3.4-34
- Rebuild for aarch64 support (#925619)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Akira TAGOH <tagoh@redhat.com> - 2.3.4-28
- Fix a build fail on ppc64.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 12 2008 Akira TAGOH <tagoh@redhat.com> - 2.3.4-26
- Rebuild for gcc-4.3.

* Tue Nov 20 2007 Akira TAGOH <tagoh@redhat.com> - 2.3.4-25
- Clean up spec file.
- Get rid of -L%%libdir% from kakasi-config because it's a standard library
  directory. (#341691)
- Separate the shread library to kakasi-libs package.

* Thu Aug 23 2007 Akira TAGOH <tagoh@redhat.com> - 2.3.4-24
- Rebuild

* Wed Aug  8 2007 Akira TAGOH <tagoh@redhat.com> - 2.3.4-23
- Update License tag.
- Build with --disable-static
- Not ship *.la files.

* Mon Sep 11 2006 Akira TAGOH <tagoh@redhat.com> - 2.3.4-22
- rebuilt
- clean up.

* Thu Mar  2 2006 Akira TAGOH <tagoh@redhat.com> - 2.3.4-21
- rebuilt.

* Mon May 30 2005 Akira TAGOH <tagoh@redhat.com> - 2.3.4-20
- import to Fedora Extras.

* Thu Mar 17 2005 Akira TAGOH <tagoh@redhat.com> - 2.3.4-19
- rebuilt

* Thu Feb 10 2005 Akira TAGOH <tagoh@redhat.com> - 2.3.4-18
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 03 2004 Akira TAGOH <tagoh@redhat.com> 2.3.4-15
- kakasi-2.3.4-fix-bad-source.patch: applied to fix gcc warning. (#114744)

* Tue Dec 02 2003 Akira TAGOH <tagoh@redhat.com> 2.3.4-14
- doh. refixed wrong array size. (#110788)

* Tue Sep 30 2003 Akira TAGOH <tagoh@redhat.com> 2.3.4-13
- converted Japanese manpage to UTF-8.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr 25 2003 Akira TAGOH <tagoh@redhat.com> 2.3.4-11
- kakasi-2.3.4-arraysize.patch: fix wrong array size. (#80675)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches

* Thu Jul 18 2002 Akira TAGOH <tagoh@redhat.com> 2.3.4-8
- add the owned directory.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Apr 16 2002 Akira TAGOH <tagoh@redhat.com> 2.3.4-5
- kakasi-2.3.4-fixdict.patch: applied to fix an incorrect entry
  in dictionary.

* Wed Feb 27 2002 Akira TAGOH <tagoh@redhat.com> 2.3.4-3
- Build against new environment.

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Nov  1 2001 Akira TAGOH <tagoh@redhat.com> 2.3.4-1
- New upstream release.
- Replaced the appropriate rpmmacros.
- Added requires: kakasi to kakasi-dict

* Thu Aug  9 2001 Tim Powers <timp@redhat.com>
- redhatify specfile
- no more man pages in /usr/man

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.
 
* Thu Feb 08 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add libtoolize to make porting to new archs easy
 
* Sun Aug 06 2000 Yukihiro Nakai <ynakai@redhat.com>
- Rebuild for 7.0J beta
 
* Sat Mar 04 2000 Ryuji Abe <raeva@t3.rim.or.jp>
- fix summary.
 
* Wed Dec 08 1999 Motonobu Ichimura <famao@kondara.org>
- change Group ( Utilities/Text -> Applications/Text ) for Kondara
 
* Thu Oct 28 1999 Ryuji Abe <raeva@t3.rim.or.jp>
- added japanese manpage in packages.
- build dict packages.
 
* Sat Oct 16 1999 Ryuji Abe <raeva@t3.rim.or.jp>
- fixed including libkakasi.so* in non-devel packages.
