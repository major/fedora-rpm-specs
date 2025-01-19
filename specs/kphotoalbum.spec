%undefine __cmake_in_source_build

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Summary: KDE Photo Album 
Name:	 kphotoalbum
Version: 6.0.1
Release: 2%{?dist}

# KDE e.V. may determine that future GPL versions are accepted
# Automatically converted from old format: (GPLv2 or GPLv3) and GFDL - review is highly recommended.
License: (GPL-2.0-only OR GPL-3.0-only) AND LicenseRef-Callaway-GFDL

URL:	 http://kphotoalbum.org/
Source0: https://download.kde.org/stable/kphotoalbum/%{version}/kphotoalbum-%{version}.tar.xz

## upstream patches (lookaside cache)

## upstreamable patches

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: libjpeg-devel
BuildRequires: pkgconfig(exiv2)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Test)

BuildRequires: cmake(Phonon4Qt6)

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6WidgetsAddons)

BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KDcrawQt6)
BuildRequires: cmake(Marble) >= 24.11.70

%description
A photo album tool. Focuses on three key points:
  * It must be easy to describe a number of images at a time. 
  * It must be easy to search for images. 
  * It must be easy to browse and View the images.


%prep
%autosetup -p1


%build
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang %{name} --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kphotoalbum.*.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kphotoalbum.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kphotoalbum-import.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kphotoalbum.open-raw.desktop


%files -f %{name}.lang
%license LICENSES/*
%config(noreplace) %{_kf6_sysconfdir}/xdg/kphotoalbumrc
%{_kf6_bindir}/kpa-backup.sh
%{_kf6_bindir}/kphotoalbum
%{_kf6_bindir}/open-raw.pl
%{_kf6_bindir}/kpa-thumbnailtool
%{_kf6_libdir}/libkpabase.so
%{_kf6_libdir}/libkpathumbnails.so
%{_kf6_libdir}/libkpaexif.so
%{_kf6_datadir}/kphotoalbum/
%{_kf6_metainfodir}/org.kde.kphotoalbum.*.xml
%{_kf6_datadir}/applications/org.kde.kphotoalbum.desktop
%{_kf6_datadir}/applications/org.kde.kphotoalbum-import.desktop
%{_kf6_datadir}/applications/org.kde.kphotoalbum.open-raw.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 6.0.1-1
- 6.0.1 hotfix

* Tue Dec 17 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 6.0.0-1
- 6.0.0

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 5.12.0-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 30 2024 Robert-André Mauchin <zebob.m@gmail.com> - 5.12.0-4
- Rebuilt for exiv2 0.28.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 27 2023 Marie Loise Nolden <loise@kde.org> - 5.12.0-1
- Update to 5.12.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 04 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 5.9.1-1
- Hotfix: KPhotoAlbum 5.9.1 (https://www.kphotoalbum.org//2022/09/06/hotfix-kphotoalbum-5.9.1/

* Sun Sep 04 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 5.9.0-1
- 5.9.0

* Tue Aug 09 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 5.8.1-1
- 5.8.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 09 2020 Marie Loise Nolden <loise@kde.org> - 5.7.0-1
- 5.7.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020 Marie Loise Nolden <loise@kde.org> - 5.6.1-1
- 5.6.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.4-1
- 5.4, pull in exiv2 fixes from master branch

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.3-2
- rebuild (exiv2)

* Wed Jul 25 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.3-1
- kphotoalbum-5.3
- use %%make_build

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.2-6
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.2-3
- trim changelog

* Fri May 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.2-2
- libkface support unconditionally off (upstream doesn't enable by default)

* Fri May 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.2-1
- kphotoalbum-5.2, disable libkface support on f26+

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.1-2
- rebuild (exiv2)

* Mon Feb 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.1-1
- 5.1 (kf5-based)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.7.2-1
- 4.7.2

* Fri Apr 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.7.1-2
- disable libkface f25+ (#1246056)

* Sat Mar 05 2016 Rex Dieter <rdieter@fedoraproject.org> 4.7.1-1
- 4.7.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 Rex Dieter <rdieter@fedoraproject.org> 4.6.2-1
- 4.6.2

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.6.1-4
- rebuild (exiv2)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-2
- drop (unused) marble dep (using libkgeomap now instead), use kde_runtime_requires macro

* Wed Apr 15 2015 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-1
- 4.6.1

* Wed Dec 10 2014 Rex Dieter <rdieter@fedoraproject.org> 4.5-4
- rebuild (marble)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 06 2014 Rex Dieter <rdieter@fedoraproject.org> 4.5-2
- rebuild (kde-4.14)

* Wed Jul 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.5-1
- kphotoalbum-4.5
- trim changelog
- update License
- improve scriptlets
