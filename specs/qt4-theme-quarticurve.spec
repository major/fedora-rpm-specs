Name: qt4-theme-quarticurve
Version: 0.0
Release: 0.46.beta8%{?dist}
URL: http://www.kde-look.org/content/show.php/Quarticurve?content=59884
# downloadable from URL above
Source: quarticurve-beta8.tar.bz2
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
BuildRequires: make
BuildRequires: kdelibs4-devel
Requires: kde-filesystem >= 4-7

Summary: Unofficial port of the Bluecurve widget theme to Qt 4
%description
Quarticurve is an unofficial port of Red Hat's Bluecurve Qt 3 widget theme to
Qt 4.

%prep
%setup -q -n quarticurve-beta8

%build
%{qmake_qt4}
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT

%files
%{_qt4_plugindir}/styles/libquarticurve.so
%{_kde4_appsdir}/color-schemes/Quarticurve.colors
%doc COPYING ChangeLog readme.txt

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.46.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0-0.45.beta8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.44.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.43.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.42.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.41.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.40.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.39.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.38.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.37.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.36.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.35.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.34.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.33.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.32.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.31.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.30.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.29.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.28.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.27.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.26.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 0.0-0.25.beta8
- use %%qmake_qt4/%%_qt4_plugindir macros

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.24.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0-0.23.beta8
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.22.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.21.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.20.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.19.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.18.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.17.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.16.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.15.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-0.14.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 16 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.0-0.13.beta8
- Update to beta 8:
  - The size of icons in menus is now fixed to 16x16 (matches Qt/KDE 3 and GTK+)
  - Fixed crashes with QtWebKit (#466421) (ported to QStyleOption)
  - Fixed blurriness when painting widgets on a painter which has anti-aliasing
    of graphics enabled (as in QtWebKit)
  - Fixed _kde4_appsdir detection (no longer need manual override)

* Mon Jul 7 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.0-0.12.beta7
- Explicitly set KDE4_APPSDIR to work around broken autodetection for now
  (fixes FTBFS).

* Sat Feb 9 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.0-0.11.beta7
- Rebuild for GCC 4.3.

* Fri Jan 25 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.0-0.10.beta7
- Update to beta 7:
  - Added a color scheme for the KDE 4 color scheme selector
  - Updated the color section in readme.txt
- BR kdelibs4-devel for kde4-config.
- Require kde-filesystem >= 4-7 for directory ownership.
- Update file list (add Quarticurve.colors).
- Cleanup description.

* Mon Dec 3 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.0-0.9.beta6
- Update to beta 6:
  - Use system (rather than builtin Qt) icons in Qt 4 dialogs also in KDE 4 apps

* Fri Oct 26 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.0-0.8.beta5
- Fix setup command (forgot to update directory name).

* Fri Oct 26 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.0-0.7.beta5
- Don't own %%{qtplugindir}/styles, now owned by qt4.

* Fri Oct 26 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.0-0.6.beta5
- Update to beta 5:
  - Force selection color to always active (as in Qt/KDE 3)
  - Dock widgets now look much closer to the Qt 3 theme
  - Draw frames around status bar sections (as in Qt 3)

* Mon Oct 15 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.0-0.5.beta4
- Update to beta 4 (updated readme, fixed QPushButton::iconSize being ignored).

* Wed Aug 22 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 0.0-0.4.beta3
- respin (BuildID)

* Fri Aug 3 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.0-0.3.beta3
- Specify GPL version in License tag.

* Fri Jul 20 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.0-0.2.beta3
- Update readme.txt.

* Sat Jun 16 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.0-0.1.beta3
- First Fedora RPM.
