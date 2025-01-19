%undefine __cmake_in_source_build

Name:       kbibtex
Version:    0.10.0
Release:    9%{?dist}
Summary:    A BibTeX editor for KDE

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        https://userbase.kde.org/KBibTeX
Source0:    http://download.kde.org/stable/KBibTeX/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake qt5-qtbase-devel desktop-file-utils gettext-devel
%ifarch %qt5_qtwebengine_arches
BuildRequires:  qt5-qtwebengine-devel
%else
BuildRequires:  qt5-qtwebkit-devel
%endif
BuildRequires:  cmake(Qt5NetworkAuth)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  extra-cmake-modules
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  qca-qt5-devel
BuildRequires:  libicu-devel
BuildRequires:  qoauth-qt5-devel
BuildRequires:  shared-mime-info
Requires:       bibutils

%description
The program KBibTeX is a bibliography editor for KDE. Its main purpose is to
provide a user-friendly interface to BibTeX files.

%package  libs
Summary:  Runtime files for %{name}
%description libs
The program KBibTeX is a bibliography editor for KDE. Its main purpose is to
provide a user-friendly interface to BibTeX files.

This package provides the runtime libraries for %{name}

%package  devel
Summary:  Development files for KBibTeX
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: libxslt-devel%{?_isa}
Requires: poppler-qt5-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files necessary for
developing programs using KBibTeX libraries.

%prep
%setup -q


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name

%check
desktop-file-validate  $RPM_BUILD_ROOT%{_kf5_datadir}/applications/*.desktop


%files -f %{name}.lang
%doc README.md ChangeLog
%{_kf5_bindir}/%{name}
%{_qt5_plugindir}/%{name}part.so*
%{_kf5_datadir}/applications/*%{name}.desktop
%{_kf5_datadir}/kservices5/%{name}part.desktop
%{_kf5_datadir}/kxmlgui5/*
%{_kf5_datadir}/%{name}/
%{_datadir}/metainfo/*
%{_datadir}/mime/packages/bibliography.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/qlogging-categories5/kbibtex.categories
%{_kf5_docdir}/HTML/*/%{name}
%{_mandir}/*

%files libs
%license LICENSE
%{_libdir}/lib%{name}*.so.*

%files devel
%{_includedir}/KBibTeX/
%{_libdir}/cmake/KBibTeX/
%{_libdir}/lib%{name}*.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.10.0-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 0.10.0-6
- Rebuild for ICU 74

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 0.10.0-2
- Rebuilt for ICU 73.2

* Sat Mar 18 2023 Orion Poplawski <orion@nwra.com> - 0.10.0-1
- Update to 0.10.0

* Sun Mar 05 2023 Orion Poplawski <orion@nwra.com> - 0.9.3.2-1
- Update to 0.9.3.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 0.9.2-10
- Rebuild for ICU 72

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.2-9
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 0.9.2-5
- Rebuild for ICU 69

* Tue Feb  2 2021 Robin Lee <cheeselee@fedoraproject.org> - 0.9.2-4
- Fix requirement of devel subpackage (RHBZ#1919474)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Marie Loise Nolden <loise@kde.org> - 0.9.2-1
- Update to 0.9.2

* Mon May 18 2020 Pete Walter <pwalter@fedoraproject.org> - 0.9-6
- Rebuild for ICU 67

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 0.9-4
- Rebuild for poppler-0.84.0

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 0.9-3
- Rebuild for ICU 65

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.9-1
- Update to 0.9

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 0.8.1-2
- Rebuild for ICU 63

* Sun Jul 15 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1
- Requires bibutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0.7-3
- Rebuild for ICU 62

* Tue May  1 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.7-2
- Fix build with ICU 61

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 0.7-2
- Rebuild for ICU 61.1

* Fri Feb  9 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.7-1
- Update to 0.7 (BZ#1543148)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr  9 2017 Robin Lee <cheeselee@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 31 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.6-3
- devel subpackage requires poppler-qt-devel%%{?_isa}

* Fri Oct 30 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.6-2
- Use a new patch from upstream to fix ARM build
- devel subpackage requres libs instead of the base package

* Tue Oct 13 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.6-1
- Update to 0.6
- Fix ARM build with 0001-Use-qreal-instead-of-double.patch
- Use upstream appdata
- Move the shared libraries to %%{_libdir} and to a libs subpackage

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.1-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.5.1-6
- Add an AppData file for the software center

* Sun Aug 17 2014 Rex Dieter <rdieter@fedoraproject.org> 0.5.1-5
- BR: pkgconfig(QtWebKit), it's no longer pulled in implicitly by kdelibs-devel

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 16 2014 Rex Dieter <rdieter@fedoraproject.org> 0.5.1-3
- update scriptlets, BR: kdelibs4-devel, tighten subpkg dep

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Mon Dec 30 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.5-1
- Update to 0.5
- Split out a devel subpackage

* Wed Nov 20 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.4.1-5
- Fix URL

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 14 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.4.1-3
- Requires okular-part (BZ#984142)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 0.4-3
- Rebuild (poppler-0.20.0)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.4-1
- Update to 0.4
- Move the unversioned shared object files to a program-private directory

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 0.3-4
- Rebuild (poppler-0.17.3)

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 0.3-3
- Rebuild (poppler-0.17.0)

* Sat Jun 25 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.3-2
- Scriptlets revised
- Use description from upstream REAMDE

* Sat Jun 25 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.3-1
- Update to 0.3
- BR: cmake kdelibs-devel poppler-qt4-devel added, kdelibs3-devel removed
- Cmake-based build
- Scriptlets revised
- Specfile Untabified
- URL and Source0 updated
- kbibtex-0.2-desktop-file-type.patch removed
- Other cleanup

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 23 2009 Christian Nolte <ch.nolte at noltec.org> - 0.2.2-19
- Updated to latest upstream version 0.2.2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.2-14
- BR kdelibs3-devel instead of kdebase-devel (should not need kdebase) (#434344)

* Tue Jan 01 2008 Christian Nolte <ch.nolte at noltec.org> - 0.2-13
- Updated to latest upstream version 0.2
- Desktop-File kbibtex_part.desktop patched: Type is Application now

* Mon Jul 09 2007 Christian Nolte <ch.nolte at noltec.org> - 0.1.5.52-11
- Updated to latest upstream version

* Wed Mar 21 2007 Christian Nolte <ch.nolte at noltec.org> - 0.1.5-8
- latest patches (storesearchurls, webquerypubmedmultiplequeries,
  xslhtmlexport)

* Tue Dec 05 2006 Christian Nolte <ch.nolte at fh-wolfenbuettel.de> - 0.1.5-4
- Bumped release ver. to solve the violated upgrade path (BUG #216007)

* Sun Oct 29 2006 Christian Nolte <ch.nolte at fh-wolfenbuettel.de> - 0.1.5-2
- latest released patches (filteredselection,gcc4.2,viewdocument)

* Wed Oct 18 2006 Christian Nolte <ch.nolte at fh-wolfenbuettel.de> - 0.1.5-1
- Update to 0.1.5

* Fri Sep 15 2006 Christian Nolte <ch.nolte at fh-wolfenbuettel.de> - 0.1.4-2
- Rebuild for FC6

* Thu Apr 27 2006 Christian Nolte <ch.nolte at fh-wolfenbuettel.de> - 0.1.4-1
- Update to the version 0.1.4

* Fri Dec 23 2005 Christian Nolte <ch.nolte at fh-wolfenbuettel.de> - 0.1.3-3
- Patch to resolve an error when this package is compiled with gcc 4.1.0

* Tue Dec 13 2005 Christian Nolte <ch.nolte at fh-wolfenbuettel.de> - 0.1.3-2
- BUG 17556 - package review: fixed all problems

* Mon Dec 12 2005 Christian Nolte <ch.nolte at fh-wolfenbuettel.de> - 0.1.3-1
- Version 0.1.3
