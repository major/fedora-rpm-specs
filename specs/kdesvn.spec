%undefine __cmake_in_source_build
Name:           kdesvn
Version:        2.1.0
Release:        13%{?dist}
Summary:        Subversion client for KDE

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/KDE/kdesvn
Source0:        http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}-1.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  subversion-devel
BuildRequires:  neon-devel
BuildRequires:  cmake3 >= 3.1.0
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  libappstream-glib


%description
KDESvn is a frontend to the subversion vcs. In difference to most other
tools it uses the subversion C-Api direct via a c++ wrapper made by Rapid
SVN and doesn't parse the output of the subversion client. So it is a real
client itself instead of a frontend to the command line tool.

It is designed for the K-Desktop environment and uses all of the goodies
it has. It is planned for future that based on the native client some plugins
for konqueror and/or kate will made.


%prep
%autosetup


%build
# erase invalid tag order (2.0 before 2.1)
sed -i -e '/release version="2.0" date="2016-12-10"/d' src/org.kde.kdesvn.appdata.xml

%cmake_kf5
%cmake_build


%install
%cmake_install


%find_lang %{name} --with-html

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING GPL.txt
%{_bindir}/%{name}
%{_bindir}/kdesvnaskpass
%{_qt5_plugindir}/kdesvnpart.so
%{_qt5_plugindir}/kio_ksvn.so
%{_kf5_plugindir}/kded/kdesvnd.so
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/*.protocol
%{_datadir}/kservices5/ServiceMenus/%{name}*.desktop
%{_datadir}/config.kcfg/kdesvn_part.kcfg
%{_datadir}/dbus-1/interfaces/kf5_org.kde.kdesvnd.xml
%{_datadir}/dbus-1/services/org.kde.kdesvnd.service
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svgz
%{_datadir}/kconf_update/kdesvn-use-external-update.sh
%{_datadir}/kconf_update/kdesvnpartrc-use-external.upd
%{_datadir}/%{name}
%{_datadir}/kxmlgui5/%{name}
%{_datadir}/metainfo/org.kde.kdesvn.appdata.xml
%{_mandir}/man1/kdesvn.1.gz
%{_mandir}/man1/kdesvnaskpass.1.gz
%{_mandir}/*/man1/*.gz


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Marie Loise Nolden <loise@kde.org> - 2.1.0-1
- Update to 2.1.0-1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.95-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Vasiliy N. Glazov <vascom2@gmail.com> 2.0.95-4
- Updated to latest version
- Added appdata

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Vasiliy N. Glazov <vascom2@gmail.com> 2.0.95-2
- Add translations

* Fri Apr 19 2019 Vasiliy N. Glazov <vascom2@gmail.com> 2.0.95-1
- Update to latest git

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 4 2016 Orion Poplawski <orion@cora.nwra.com> - 1.7.0-1
- Update to 1.7.0
- Drop devel sub-package - libsvnqt is now a private API

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6.0-7
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.6.0-3
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 6 2012 Orion Poplawski <orion@cora.nwra.com> - 1.6.0-1
- Update to 1.6.0
- Drop kdex, virtual, and gcc47 patches applied upstream

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Orion Poplawski <orion@cora.nwra.com> - 1.5.5-5
- Add patch to fix offending virtual inheritance
- Add patch to compile with gcc 4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 1.5.5-2
- Rebuilt for gcc bug 634757

* Wed Sep 15 2010 Orion Poplawski <orion@cora.nwra.com> - 1.5.5-1
- Update to 1.5.5

* Tue Aug 24 2010 Jaroslav Reznik <jreznik@redhat.com> - 1.5.4-1
- Update to 1.5.4

* Thu Jul 8 2010 Orion Poplawski <orion@cora.nwra.com> - 1.5.3-2
- Add patch to update kdex.dtd title, fixes FTBS bug 599983

* Fri Apr 09 2010 Jaroslav Reznik <jreznik@redhat.com> - 1.5.3-1
- Update to 1.5.3

* Mon Feb 22 2010 Orion Poplawski <orion@cora.nwra.com> - 1.5.2-1
- Update to 1.5.2

* Mon Jan 18 2010 Jaroslav Reznik <jreznik@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Mon Jan 11 2010 Jaroslav Reznik <jreznik@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Thu Oct 01 2009 Jaroslav Reznik <jreznik@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Mon Aug 10 2009 Jaroslav Reznik <jreznik@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-1
- Update to 1.3.2

* Fri Apr 24 2009 Orion Poplawski <orion@cora.nwra.com> - 1.3.0-1
- Update to 1.3.0

* Wed Mar 4 2009 Orion Poplawski <orion@cora.nwra.com> - 1.2.4-1
- Update to 1.2.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-1
- Update to 1.2.3

* Mon Nov 24 2008 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-1
- Update to 1.2.2
- Drop upstreamed patches

* Fri Oct 3 2008 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-1
- Update to 1.2.1

* Mon Sep 29 2008 Orion Poplawski <orion@cora.nwra.com> - 1.2.0-0.20080926.1
- Update to 1.2.0.20080926, KDE4 version

* Mon Sep 29 2008 Orion Poplawski <orion@cora.nwra.com> - 1.0.2-1
- Update to 1.0.2
- Add BR sqlite-devel needed for Qt3 build

* Thu Aug 7 2008 Orion Poplawski <orion@cora.nwra.com> - 1.0.0-1
- Update to 1.0.0
- Drop png patch applied upstream
- Update asneeded patch
- Handle multiple languages

* Tue Jul 15 2008 Orion Poplawski <orion@cora.nwra.com> - 0.14.6-1
- Update to 0.14.6

* Mon May 19 2008 Orion Poplawski <orion@cora.nwra.com> - 0.14.4-1
- Update to 0.14.4

* Tue May 6 2008 Orion Poplawski <orion@cora.nwra.com> - 0.14.3-1
- Update to 0.14.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.14.1-4
- Autorebuild for GCC 4.3

* Tue Dec 11 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> - 0.14.1-3
- BuildRequires: kdelibs-devel -> kdelibs3-devel

* Tue Dec 11 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> - 0.14.1-2
- Rebuild for new openssl/openldap

* Mon Nov 19 2007 Orion Poplawski <orion@cora.nwra.com> - 0.14.1-1
- Update to 0.14.1
- Link libsvnqt.so with --as-needed
- Add patch to fix bug #388821 (dangling symlinks)

* Mon Sep  3 2007 Joe Orton <jorton@redhat.com> 0.13.0-4
- rebuild for fixed 32-bit APR (#254241)

* Tue Aug 28 2007 Orion Poplawski <orion@cora.nwra.com> - 0.13.0-3
- Rebuild for new expat

* Tue Aug 21 2007 Orion Poplawski <orion@cora.nwra.com> - 0.13.0-2
- Rebuild for BuildID

* Wed Aug  8 2007 Orion Poplawski <orion@cora.nwra.com> - 0.13.0-1
- Update to 0.13.0
- Update License tag to GPLv2+

* Wed Jun 13 2007 Orion Poplawski <orion@cora.nwra.com> - 0.12.1-1
- Update to 0.12.1
- Remove index.cache hacks fixed upstream

* Mon Apr 16 2007 Orion Poplawski <orion@cora.nwra.com> - 0.11.2-3
- Remove no longer needed .so permission fix

* Fri Apr 06 2007 Orion Poplawski <orion@cora.nwra.com> - 0.11.2-2
- Use %%cmake macro
- Fix shared library permissions

* Mon Mar 26 2007 Orion Poplawski <orion@cora.nwra.com> - 0.11.2-1
- Update to 0.11.2
- Install a prebuilt en_index.cache.bz2 to fix multilib (bug #228370)

* Wed Nov  1 2006 Orion Poplawski <orion@cora.nwra.com> - 0.11.0-1
- Update to 0.11.0

* Wed Oct  4 2006 Orion Poplawski <orion@cora.nwra.com> - 0.10.0-1
- Update to 0.10.0

* Tue Oct  3 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-1
- Update to 0.9.3
- Remove patch applied upstream

* Fri Sep  1 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-1
- Update to 0.9.2, uses cmake
- Add patch from Rajko Albrecht to fix lib64 installs

* Thu Jul 27 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-1
- Update to 0.9.1, should fix bug #185165

* Mon Jun  5 2006 Orion Poplawski <orion@cora.nwra.com> - 0.8.4-1
- Update to 0.8.4

* Wed Mar  8 2006 Orion Poplawski <orion@cora.nwra.com> - 0.7.4-1
- Update to 0.7.4

* Mon Feb 13 2006 Orion Poplawski <orion@cora.nwra.com> - 0.7.3-2
- Rebuild for gcc/glibc changes

* Wed Feb  1 2006 Orion Poplawski <orion@cora.nwra.com> - 0.7.3-1
- Update to 0.7.3

* Fri Jan 20 2006 Orion Poplawski <orion@cora.nwra.com> - 0.7.2-1
- Update to 0.7.2
- Remove gcc41 patch fixed upstream
- Remove apr-1-config and apu-1-config args - fixed upstream
- Drop srcver - bad idea

* Fri Dec 16 2005 Orion Poplawski <orion@cora.nwra.com> - 0.7.1-3
- Add missing files not detected by mock
- Add patch to fix gcc41 compile error

* Tue Dec 13 2005 Orion Poplawski <orion@cora.nwra.com> - 0.7.1-2
- Specify apr-1-config and apu-1-config to configure

* Fri Dec  9 2005 Orion Poplawski <orion@cora.nwra.com> - 0.7.1-1
- New upstream version 0.7.1

* Sun Nov 20 2005 Orion Poplawski <orion@cora.nwra.com> - 0.7.0-0.rc1
- New upstream version 0.7.0rc1
- Remove desktop patch fixed upstream
- Add patch to remove X11 checks from configure

* Fri Nov  4 2005 Orion Poplawski <orion@cora.nwra.com> - 0.6.3-2
- Make use of buildroot consistant
- Just BuildRequires the "desktop-file-utils" package
- Add post/postun update-desktop-database and gtk-update-icon-cache
- Add Application Category tag to desktop file

* Thu Nov  3 2005 Orion Poplawski <orion@cora.nwra.com> - 0.6.3-1
- Initial Fedora Extras release
