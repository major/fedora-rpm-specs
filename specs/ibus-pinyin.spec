# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3

Name:       ibus-pinyin
Version:    1.5.1
Release:    3%{?dist}
Summary:    The Chinese Pinyin and Bopomofo engines for IBus input platform
License:    GPL-2.0-or-later
URL:        https://github.com/ibus/ibus-pinyin
Source0:    https://github.com/ibus/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  gnome-common
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  libuuid-devel
BuildRequires:  ibus-devel >= 1.5.4
BuildRequires:  lua-devel >= 5.1
BuildRequires:  opencc-devel
BuildRequires:  pyzy-devel
BuildRequires:  python3-devel
BuildRequires: make

# Requires(post): sqlite

Requires:   ibus >= 1.5.4


%description
The Chinese Pinyin and Bopomofo input methods for IBus platform.

%prep
%autosetup -p1

%build
./autogen.sh
%configure --disable-static --enable-db-open-phrase \
           --enable-opencc \
           --disable-boost

# make -C po update-gmo
make %{?_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install

%py_byte_compile %{python3} $RPM_BUILD_ROOT%{_datadir}/ibus-pinyin/setup

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-pinyin
%{_libexecdir}/ibus-setup-pinyin
%{_datadir}/ibus-pinyin/phrases.txt
%{_datadir}/ibus-pinyin/icons
%{_datadir}/ibus-pinyin/setup
%{_datadir}/applications/ibus-setup-bopomofo.desktop
%{_datadir}/applications/ibus-setup-pinyin.desktop
%dir %{_datadir}/ibus-pinyin
%dir %{_datadir}/ibus-pinyin/db
%{_datadir}/ibus/component/*
%{_datadir}/ibus-pinyin/base.lua
%{_datadir}/ibus-pinyin/db/english.db


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr  9 2024 Peng Wu <pwu@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 16 2023 Peng Wu <pwu@redhat.com> - 1.5.0-30
- Add ibus-pinyin-fixes-preference-dialog.patch

* Tue May  9 2023 Peng Wu <pwu@redhat.com> - 1.5.0-29
- Update ibus-pinyin-fixes-english-db-build.patch

* Mon May  8 2023 Peng Wu <pwu@redhat.com> - 1.5.0-28
- Migrate to SPDX license
- Fix compile

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug  5 2020 Peng Wu <pwu@redhat.com> - 1.5.0-22
- Rebuilt with python3

* Tue Aug  4 2020 Peng Wu <pwu@redhat.com> - 1.5.0-21
- Fixes FTBFS bug

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Peng Wu <pwu@redhat.com> - 1.5.0-9
- Rebuilt for pyzy

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov  8 2013 Peng Wu <pwu@redhat.com> - 1.5.0-5
- Fixes ibus: visible password entry flaw. (rhbz#1027029) (CVE-2013-4509)

* Tue Aug  6 2013 Peng Wu <pwu@redhat.com> - 1.5.0-4
- Fixes lua 5.2 compile

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Peng Wu <pwu@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Mon Dec 17 2012 Peng Wu <pwu@redhat.com> - 1.4.99.20120808-3
- Fixes requires

* Fri Dec 14 2012 Peng Wu <pwu@redhat.com> - 1.4.99.20120808-2
- Rebuilt for pyzy

* Tue Dec 11 2012 Peng Wu <pwu@redhat.com> - 1.4.99.20120808-1
- Update to 1.4.99.20120808

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.99.20120620-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012  Peng Wu <pwu@redhat.com> - 1.4.99.20120620-2
- Fixes spec

* Mon Jun 25 2012  Peng Wu <pwu@redhat.com> - 1.4.99.20120620-1
- Update to 1.4.99.20120620

* Tue Jun 12 2012  Peng Wu <pwu@redhat.com> - 1.4.0-17
- Remove the libpinyin integration patch

* Thu Apr 12 2012  Peng Wu <pwu@redhat.com> - 1.4.0-16
- Fixes commit method in libpinyin bopomofo editor

* Tue Mar 27 2012  Peng Wu <pwu@redhat.com> - 1.4.0-15
- Rebuilt for libpinyin-0.5.92

* Tue Mar 06 2012  Peng Wu <pwu@redhat.com> - 1.4.0-14
- Rebuilt for ibus-1.4.99

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-13
- Rebuilt for c++ ABI breakage

* Thu Feb 16 2012  Peng Wu <pwu@redhat.com> - 1.4.0-12
- Auto detect the ibus-pinyin data files

* Mon Feb 13 2012  Peng Wu <pwu@redhat.com> - 1.4.0-11
- Fixes use enter key to input English

* Fri Feb 03 2012  Peng Wu <pwu@redhat.com> - 1.4.0-10
- Rebuilt for opencc 0.3.0

* Tue Jan 31 2012  Peng Wu <pwu@redhat.com> - 1.4.0-9
- Bring back ibus-pinyin-db-open-phrase

* Mon Jan 30 2012  Peng Wu <pwu@redhat.com> - 1.4.0-8
- Removes and obsoletes ibus-pinyin-db-open-phrase

* Mon Jan 30 2012  Peng Wu <pwu@redhat.com> - 1.4.0-7
- Fixes Bopomofo Engine

* Sun Jan 29 2012  Peng Wu <pwu@redhat.com> - 1.4.0-6
- Enable Intelligent Bopomofo

* Wed Jan 18 2012  Peng Wu <pwu@redhat.com> - 1.4.0-5
- Re-build for libpinyin 0.5.0

* Mon Jan 16 2012  Peng Wu <pwu@redhat.com> - 1.4.0-4
- Fixes ibus-pinyin-libpinyin-integration.patch

* Fri Jan 13 2012  Peng Wu <pwu@redhat.com> - 1.4.0-3
- Update ibus-pinyin-libpinyin-integration.patch

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 27 2011  Peng Wu <pwu@redhat.com> - 1.4.0-1
- Update to 1.4.0, and refresh ibus-pinyin-libpinyin-integration.patch

* Wed Nov 30 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110706-13
- Change i386 to i686

* Wed Nov 30 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110706-12
- Only enable opencc on i386 and x86_64

* Fri Nov 25 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110706-11
- Fixes process space in libpinyin phonetic editor

* Tue Nov 22 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110706-10
- Fixes 'nv' handle in full pinyin editor

* Fri Nov 18 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110706-9
- Re-build for libpinyin 0.3.0

* Mon Nov 14 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110706-8
- Fixes 'dia', (rhbz#753687)

* Tue Nov 08 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110706-7
- Updates ibus-pinyin-libpinyin-integration.patch

* Tue Nov 08 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110706-6
- Improves pinyin default input style. (rhbz#751923)

* Thu Nov 03 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110706-5
- Fixes crashes, update ibus-pinyin-libpinyin-integration.patch

* Mon Oct 31 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110706-4
- Fixes pinyin.xml.in.in

* Thu Oct 27 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110706-3
- Add ibus-pinyin-libpinyin-integration.patch

* Mon Aug 01 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110706-2
- Add ibus-pinyin-xx-icon-symbol.patch

* Mon Aug 01 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110706-1
- Update to 1.3.99.20110706

* Mon May 23 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110520-1
- Update to 1.3.99.20110520

* Wed Mar 02 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110217-2
- Disable boost when configure to fix compiling

* Wed Mar 02 2011  Peng Wu <pwu@redhat.com> - 1.3.99.20110217-1
- Update version to 1.3.99.20110217

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.99.20101029-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 08 2010  Peng Wu <pwu@redhat.com> - 1.3.99.20101029-1
- Update to 1.3.99.20101029.

* Fri Nov 05 2010  Peng Wu <pwu@redhat.com> - 1.3.11-2
- Re-built for f15.

* Tue Sep 28 2010  Peng Wu <pwu@redhat.com> - 1.3.11-1
- Update to 1.3.11

* Fri Aug 27 2010  Peng Wu <pwu@redhat.com> - 1.3.10-1
- Update to 1.3.10, and enable opencc support.

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 1.3.9-2
- recompiling .py files against Python 2.7 (rhbz#623319)

* Fri Jul 16 2010  Peng Wu <pwu@redhat.com> - 1.3.9-1
- Update to 1.3.9

* Sat May 29 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.8-1
- Update to 1.3.8

* Fri May 28 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.7-1
- Update to 1.3.7

* Mon May 03 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.5-1
- Update to 1.3.5
- Add MS double pinyin back.
- Fix a problem in double pinyin parser.

* Sun May 02 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.4-1
- Update to 1.3.4

* Thu Apr 15 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.3-1
- Update to 1.3.3

* Sun Apr 11 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.2-1
- Update to 1.3.2

* Mon Apr 05 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Fri Mar 26 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.0-1
- Update to 1.3.0
- Fix some double pinyin problems.

* Thu Mar 18 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20100318-1
- Update to 1.2.99.20100318
- Fix some double pinyin problems.

* Mon Mar 15 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20100315-1
- Update to 1.2.99.20100315

* Mon Mar 08 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20100308-1
- Update to 1.2.99.20100308

* Fri Feb 19 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20100212-1
- Update to 1.2.99.20100212

* Thu Feb 11 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20100211-1
- Update to 1.2.99.20100211
- Add BuildRequires libsigc++20-devel

* Tue Feb 02 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20100202-1
- Update to 1.2.99.20100202

* Fri Dec 11 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.99.20091211-1
- Update to 1.2.99.20091211

* Thu Dec 10 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090915-2
- Correct pinyin database download location.

* Tue Sep 15 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090915-1
- Update to 1.2.0.20090915.
- Fix bug 508006 - The color of English Candidates doesn't work

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090617-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20090617-1
- Update to 1.2.0.20090617.

* Fri Jun 12 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090612-1
- Update to 1.1.0.20090612.

* Mon May 25 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090303-2
- Update to HEAD version in upstream git repository
- Fix bug 500762 - The iBus input speed becomes much slower after "Fuzzy PinYin" enabled
- Fix bug 501218 - make the pinyin setup window come to the front
- Fix bug 500763 - User DB is unavailable in ibus for liveCD

* Tue Mar 3 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090303-1
- Update to 1.1.0.20090303.

* Wed Feb 25 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090225-1
- Update to 1.1.0.20090225.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0.20090211-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090211-1
- Update version to 1.1.0.20090211.

* Thu Feb 05 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090205-1
- Update version to 1.1.0.20090205.

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.1.20081004-2
- Rebuild for Python 2.6

* Sat Oct 04 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20081004-1
- Update version to 0.1.1.20081004.

* Thu Sep 18 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080918-1
- Update version to 0.1.1.20080918.

* Mon Sep 01 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080901-1
- Update version to 0.1.1.20080901.

* Sat Aug 23 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080823-1
- The first version.
