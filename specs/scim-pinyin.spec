Name:       scim-pinyin
Version:    0.5.92
Release:    29%{?dist}
Summary:    Smart Pinyin IMEngine for Smart Common Input Method platform

License:    GPL-2.0-only
URL:        https://github.com/scim-im/scim-pinyin
Source0:    http://dl.sourceforge.net/scim/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  scim-devel, gtk2-devel, gettext, gettext-devel, autoconf, automake,libtool
Requires:   scim
Obsoletes:  iiimf-le-chinput <= 0.3, miniChinput <= 0.0.3
Patch2:         scim-pinyin-showallkeys.patch
# Patch3:         scim-pinyin-helper.patch
# Patch4:         scim-pinyin-0.5.91-13.bz200702.patch
# Patch5:         scim-pinyin-help-translate.patch
Patch6:         scim-pinyin-0.5.91-save-in-temp.patch
# Patch7:         scim-pinyin-0.5.91-fix-load.patch
Patch8:         scim-pinyin-0.5.91-fix-ms-shuangpin.patch
# Patch9:         scim-pinyin-0.5.91-gcc43.patch

%description
Simplified Chinese Smart Pinyin IMEngine for SCIM.


%prep
%setup -q
%patch -P2 -p1 -b .2-showallkeys
# %patch3 -p1 -b .3-helperi
# %patch4 -p1 -b .4-bz200702
# %patch5 -p1 -b .5-translate
%patch -P6 -p1 -b .6-savetmp
# %patch7 -p1 -b .6-fix-load
%patch -P8 -p1 -b .8-fix-ms-shuangpin
# %patch9 -p1 -b .9-gcc43

%build
./bootstrap
%configure --disable-static
make -C po update-gmo
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install

rm $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/{IMEngine,SetupUI}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/Helper/*.la

%find_lang %{name}



%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libdir}/scim-1.0/*/IMEngine/pinyin.so
%{_libdir}/scim-1.0/*/SetupUI/pinyin-imengine-setup.so
%{_datadir}/scim/pinyin
%{_datadir}/scim/icons/smart-pinyin.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 28 2023 Peng Wu <pwu@redhat.com> - 0.5.92-25
- Migrate to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb  3 2017 Peng Wu <pwu@redhat.com> - 0.5.92-9
- Disable scim-pinyin-0.5.91-fix-load.patch for RHBZ#1415391

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.92-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.92-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.92-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.92-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012  Peng Wu <pwu@redhat.com> - 0.5.92-1
- Update to 0.5.92

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.91-31
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.91-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.91-29
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.91-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.91-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.91-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 25 2008 Huang Peng <phuang@redhat.com> - 0.5.91-25
- Fix build error with GCC 4.3.
- Drop the scim-pinyin-helper because upstream does not accept it and we will stop maintaining it.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5.91-24
- Autorebuild for GCC 4.3

* Thu Dec 12 2007 Huang Peng <phuang@redhat.com> - 0.5.91-23
- Fix wrong key bind in ms shuangpin scheme, the patch from yufanyufan@gmail.com.

* Thu Nov 15 2007 Huang Peng <phuang@redhat.com> - 0.5.91-22
- Catch exception when load data from file to fix bug 237439.

* Mon Nov 9 2007 Huang Peng <phuang@redhat.com> - 0.5.91-21
- Save user data in temp files, and then overwrite old files to fix bug 237439.

* Mon Aug 27 2007 Huang Peng <phuang@redhat.com> - 0.5.91-20
- Change rpm license field to GPLv2

* Wed Jun 27 2007 Huang Peng <phuang@redhat.com> - 0.5.91-19
- Drop line `Patch1: scim-pinyin-shuangpin.patch' in spec file.
- Remove ChangeLog from rpm package.

* Wed Jun 27 2007 Jens Petersen <petersen@redhat.com>
- remove with_libstdc_preview macro

* Mon Jun 26 2007 Huang Peng <phuang@redhat.com> - 0.5.91-18
- Refine rpm package to resolve some warning in build.log.

* Mon Jun 18 2007 Huang Peng <phuang@redhat.com> - 0.5.91-17
- Drop patch scim-pinyin-shuangpin.patch to enable shuangpin and to fix bug (#233054)

* Thu Nov 23 2006 Shawn Huang <phuang@redhat.com> - 0.5.91-16
- add Obsoletes: miniChinput <= 0.3 to remove miniChinput when upgrading 
  from RHEL4 (#211878).

* Thu Nov 23 2006 Shawn Huang <phuang@redhat.com> - 0.5.91-15
- update all .po files for all languages.

* Wed Nov 22 2006 Shawn Huang <phuang@redhat.com> - 0.5.91-14
- Translate refined online help to Chinese (#200702).
- Update some msgids in po/zh_CN.po to fix Some tooltips were not 
  translated (#216831).

* Wed Oct 11 2006 Caius Chance <cchance@redhat.com> - 0.5.91-13.fc6
- bz#200702 - refine online help of pinyin helper.

* Thu Sep 14 2006 Qian Shen <qshen@redhat.com> - 0.5.91-12
- fix a pinyin helper bug

* Fri Aug 25 2006 Qian Shen <qshen@redhat.com> - 0.5.91-11.4
- update pinyin helper

* Mon Jul 24 2006 Qian Shen <qshen@redhat.com> - 0.5.91-11.3
- remove all ShuangPin plans

* Thu Jul 20 2006 Qian Shen <qshen@redhat.com> - 0.5.91-11.2
- remove " g_object_set ( renderer_num, "alignment", 0.5, NULL) " in add_column() to fit gtk2.10 in fc6

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Thu Jun 29 2006 Qian Shen <qshen@redhat.com> - 0.5.91-11
- rebuilt

* Thu Jun 29 2006 Qian Shen <qshen@redhat.com> - 0.5.91-10
- add gettext-devel, automake, autoconf,libtool to buildreq 
- use ./bootstrap

* Thu Jun 29 2006 Qian Shen <qshen@redhat.com> - 0.5.91-9
- run aclocal/autoconf/automake before configure
- to create new confiugre/Makefiles based on the 
- modified configure.ac 

* Thu Jun 29 2006 Qian Shen <qshen@redhat.com> - 0.5.91-8
- use rm -f ../Helper/*.la

* Thu Jun 29 2006 Qian Shen <qshen@redhat.com> - 0.5.91-7.1
- rebuilt 

* Wed Jun 28 2006 Qian Shen <qshen@redhat.com> - 0.5.91-7
- add pinyin-imengine-helper.so to the files section. rebuilt 

* Tue Jun 27 2006 Qian Shen <qshen@redhat.com> - 0.5.91-6
- add scim-pinyin-helper.patch

* Fri Mar 31 2006 Jens Petersen <petersen@redhat.com> - 0.5.91-5
- rebuild without libstdc++so7

* Mon Feb 13 2006 Qian Shen <qshen@redhat.com> - 0.5.91-4.3
- add scim-pinyin-showallkeys.patch

* Mon Feb 13 2006 Jens Petersen <petersen@redhat.com>
- remove superfluous post and postun scripts

* Mon Feb 13 2006 Qian Shen <qshen@redhat.com> - 0.5.91-4.2
- add scim-pinyin-shuangpin.patch

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.5.91-4.1
- bump again for double-long bug on ppc(64)

* Thu Feb  9 2006 Jens Petersen <petersen@redhat.com> - 0.5.91-4
- build conditionally with libstdc++so7 preview library (#166041)
  - add with_libstdc_preview switch and tweak libtool to link against it
- update filelist since moduledir is now api-versioned

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 14 2005 Jens Petersen <petersen@redhat.com> - 0.5.91-3
- add obsoletes iiimf-le-chinput for upgrades (#173071)

* Thu Oct  6 2005 Jens Petersen <petersen@redhat.com> - 0.5.91-2
- require scim

* Tue Aug 16 2005 Jens Petersen <petersen@redhat.com> - 0.5.91-1
- update to 0.5.91 test release
  - scim-pinyin-0.5.0-setup-ambiguity-cast.patch no longer needed

* Mon Aug  8 2005 Jens Petersen <petersen@redhat.com> - 0.5.0-5
- initial build for Fedora Core

* Wed Jul 27 2005 Ryo Dairiki <ryo-dairiki@mbm.nifty.com> - 0.5.0-4
- Rebuild for scim-1.4.0

* Tue Jun 21 2005 Ryo Dairiki <ryo-dairiki@mbm.nifty.com> - 0.5.0-3
- minor change on the files section

* Mon Jun 20 2005 Jens Petersen <petersen@redhat.com> - 0.5.0-2
- add source url
- add scim-pinyin-0.5.0-setup-ambiguity-cast.patch from cvs to fixing build
  on 64bit archs (Ryo Dairiki)
- configure with --disable-static so only .la files need to be removed

* Sat Jun 18 2005 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 0.5.0-1
- Initial packaging for Fedora Extras.

* Thu Jan 06 2005 James Su <suzhe@tsinghua.org.cn>
- Change package name to scim-pinyin.

* Mon Apr 26 2004 James Su <suzhe@tsinghua.org.cn>
- change the license to GPL.

* Thu Jun 19 2003 James Su <suzhe@tsinghua.org.cn>
- updated to include setup module.

* Thu May 22 2003 James Su <suzhe@tsinghua.org.cn>
- upto v0.2.1

* Mon Mar 31 2003 James Su <suzhe@tsinghua.org.cn>
- upto v0.2.0

* Sun Jul 7 2002 James Su <suzhe@tsinghua.org.cn>
- first public release of SCIM-chinese.


