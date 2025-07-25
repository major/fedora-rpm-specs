# avoid incompatible pointer type errors with GCC 14
%global build_type_safety_c 2

Summary: An Enchanting Spell Checking Library
Name: enchant
Version: 1.6.0
Release: 40%{?dist}
Epoch: 1
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
Source: http://www.abisource.com/downloads/enchant/%{version}/enchant-%{version}.tar.gz
URL: http://www.abisource.com/
BuildRequires:  gcc-c++
BuildRequires: glib2-devel >= 2.6.0
BuildRequires: hunspell-devel
BuildRequires: libvoikko-devel
BuildRequires: automake, libtool
BuildRequires: make

# Drop at or after f44
Provides: enchant-aspell = 1.6.0-37
Obsoletes: enchant-aspell < 1.6.0-37

%description
A library that wraps other spell checking backends.

%package voikko
Summary: Integration with voikko for libenchant
Requires: enchant = %{epoch}:%{version}-%{release}

%description voikko
Libraries necessary to integrate applications using libenchant with voikko.


%package devel
Summary: Support files necessary to compile applications with libenchant.
Requires: enchant = %{epoch}:%{version}-%{release}
Requires: glib2-devel

%description devel
Libraries, headers, and support files necessary to compile applications using libenchant.

%prep
%setup -q

%build
%configure --enable-myspell --with-myspell-dir=/usr/share/hunspell --disable-static --disable-ispell --disable-hspell --disable-zemberek --disable-aspell
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/enchant/*.la

%files
%doc AUTHORS COPYING.LIB README
%{_bindir}/*
%{_libdir}/lib*.so.*
%dir %{_libdir}/enchant
%{_libdir}/enchant/lib*myspell.so*
%{_mandir}/man1/enchant.1*
%{_datadir}/enchant

%files voikko
%{_libdir}/enchant/lib*_voikko.so*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/enchant.pc
%{_includedir}/enchant

%ldconfig_scriptlets

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:1.6.0-38
- Drop aspell subpackage.

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1:1.6.0-37
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:1.6.0-30
- Update myspell directory path to /usr/share/hunspell

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 1:1.6.0-22
- rebuild for hunspell 1.7.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:1.6.0-19
- Switch to %%ldconfig_scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Caolán McNamara <caolanm@redhat.com> - 1:1.6.0-15
- rebuild for hunspell 1.5.4

* Mon Apr 18 2016 Caolán McNamara <caolanm@redhat.com> - 1:1.6.0-14
- rebuild for hunspell 1.4.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:1.6.0-11
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1:1.6.0-10
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 24 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 1:1.6.0-3
- Rebuild for new hunspell

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 01 2010 Marc Maurer <uwog@abisource.com> 1:1.6.0-1
- New upstream version.
- Drop all shipped patches, as they are included upstream.

* Tue Jan  5 2010 Michael Schwendt <mschwendt@fedoraproject.org> 1:1.5.0-5
- Revert 544473: Move libenchant.so back into the -devel package.

* Sat Dec 05 2009 Marc Maurer <uwog@abisource.com> 1:1.5.0-4
- Fix 544473: Move enchant.so from the devel to the main package

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 02 2009 Caolán McNamara <caolanm@redhat.com> 1:1.5.0-2
- Resolves: rhbz#508781 improve enchant quality, leaks, and edge-case language
  dict selection

* Mon Jun 22 2009 Caolán McNamara <caolanm@redhat.com> 1:1.5.0-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jul 26 2008 Michael Schwendt <mschwendt@fedoraproject.org> 1:1.4.2-4
- Rebuild for ABI-incompatible hunspell-1.2.4.2-2.fc10

* Thu Jul 10 2008 Marc Maurer <uwog@abisource.com> 1:1.4.2-3
- Fix 426712: don't build static libs (patch from Michael Schwendt)

* Wed May 21 2008 Marc Maurer <uwog@abisource.com> 1:1.4.2-2
- Rebuild

* Wed May 21 2008 Marc Maurer <uwog@abisource.com> 1:1.4.2-1
- New upstream release
- Add voikko support in an enchant-voikko package
- Bump glib-devel BR to 2.6.0

* Fri Feb 08 2008 Caolan McNamara <caolanm@redhat.com> 1:1.3.0-4.fc9
- minor cockup

* Sat Jan 26 2008 Caolan McNamara <caolanm@redhat.com> 1:1.3.0-3.fc9
- Resolves: rhbz#426402 use system hunspell not internal one and 
  split out aspell backend.
- See: rhbz#430354 hspell backend disabled until pic issue fixed

* Wed Dec 19 2007 Caolan McNamara <caolanm@redhat.com> 1:1.3.0-2.fc9
- tell enchant where the myspell dictionaries are

* Thu Oct 12 2006 Marc Maurer <uwog@abisource.com> 1:1.3.0-1.fc6
- Update to 1.3.0

* Mon Sep 11 2006 Marc Maurer <uwog@abisource.com> 1:1.2.5-3.fc6
- Rebuild for FC6

* Mon Apr 10 2006 Marc Maurer <uwog@abisource.com> 1:1.2.5-2.fc6
- Rebuild

* Mon Apr 10 2006 Marc Maurer <uwog@abisource.com> 1:1.2.5-1.fc6
- Package the data dir as well (bug 188516)
- New upstream version
- Add hspell requirement/support

* Tue Feb 14 2006 Marc Maurer <uwog@abisource.com> 1:1.2.2-2.fc5
- Rebuild for Fedora Extras 5

* Sun Feb 05 2006 Marc Maurer <uwog@abisource.com> 1:1.2.2-1.fc5
- Update to 1.2.2

* Mon Jan 30 2006 Marc Maurer <uwog@abisource.com> 1:1.2.1-1.fc5
- Update to 1.2.1
- Drop glib Require

* Sat Oct 22 2005 Marc Maurer <uwog@abisource.com> 1:1.2.0-1.fc5
- Update to 1.2.0

* Wed Oct  5 2005 Marc Maurer <uwog@abisource.com> 1:1.1.6-4.fc5
- Add dist flag to the release number

* Mon Apr  4 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 1:1.1.6-3
- make in %%build
- disable bad buildroot rpaths in libs, don't use %%makeinstall
- require %%{epoch} of main package in -devel package (Fridrich Strba)

* Thu Mar 31 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 1:1.1.6-2
- add dep glib2-devel for pkgconfig in -devel package
- include %%{_libdir}/enchant dir in main package
- make -devel package require exact VR of main package
- use -p /sbin/ldconfig in scriptlets

* Mon Mar 28 2005 Marc Maurer <uwog@abisource.com> 1:1.1.6-1
- update to 1.1.6
- drop the manpage patch (RH#145010#)
- fix version numbers in the spec changelog

* Wed Mar  2 2005 Caolan McNamara <caolanm@redhat.com> 1:1.1.5-3
- rebuild with gcc4

* Fri Jan 14 2005 Caolan McNamara <caolanm@redhat.com> 1:1.1.5-2
- RH#145010# misformatted manpage

* Mon Dec 20 2004 Caolan McNamara <caolanm@redhat.com> 1:1.1.5-1
- initial fedora import

* Sun Aug 24 2003 Rui Miguel Seabra <rms@1407.org>
- update spec to current stat of affairs
- building from source rpm is now aware of --with and --without flags:
- --without aspell --without ispell --without myspell --with uspell

* Wed Jul 16 2003 Rui Miguel Seabra <rms@1407.org>
- take advantage of environment rpm macros

* Sun Jul 13 2003 Dom Lachowicz <cinamod@hotmail.com>
- Initial version
