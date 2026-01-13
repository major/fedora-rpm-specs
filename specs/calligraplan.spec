%bcond mpxj 0

%global app_id org.kde.calligraplan

Name:    calligraplan
Version: 4.0.1
Release: 1%{?dist}
Summary: A Project Planner 

License: GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://www.calligra-suite.org/
Source:  https://download.kde.org/%{stable_kf6}/%{name}/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches

## downstream patches


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   %{ix86}

BuildRequires: gcc-c++
BuildRequires: perl-interpreter
# kf6
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6ThreadWeaver)
BuildRequires: cmake(PlasmaActivities)
# qt6
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6DBus)
# optional
BuildRequires: cmake(KChart6)
BuildRequires: cmake(KGantt6)
BuildRequires: cmake(Qca-qt6)
BuildRequires: pkgconfig(cups)
# %%check validation
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%if %{with mpxj}
BuildRequires: java-devel
Requires: apache-poi
#Requires: apache-mpxj
%endif

%description
Plan is a project management application. It is intended for managing
moderately large projects with multiple resources.

%package  libs
Summary:  Runtime libraries for %{name}
Requires: %{name}-data = %{version}-%{release}
%description libs
%{summary}.

%package data
Summary:   Runtime support files for %{name}
BuildArch: noarch
Requires:  hicolor-icon-theme
%description data
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

## unpackaged files
# no need to package lib*.so symlinks
find  %{buildroot}%{_kf6_libdir}/  -maxdepth 1 -name lib*.so -type l -delete

%if %{without mpxj}
rm -f %{buildroot}%{_kf6_datadir}/mime/packages/plan_mpxj_mimetype.xml
%endif

%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{app_id}*.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/%{app_id}*.desktop


%files
%{_kf6_bindir}/calligraplan
%{_kf6_bindir}/calligraplanportfolio
%{_kf6_bindir}/calligraplanwork
%{_kf6_datadir}/applications/%{app_id}.desktop
%{_kf6_datadir}/applications/%{app_id}portfolio.desktop
%{_kf6_datadir}/applications/%{app_id}work.desktop
%{_kf6_metainfodir}/%{app_id}.appdata.xml
%{_kf6_metainfodir}/%{app_id}portfolio.appdata.xml
%{_kf6_metainfodir}/%{app_id}work.appdata.xml

%files libs
%{_kf6_libdir}/lib%{name}*.so.4{,.*}
%{_kf6_qtplugindir}/%{name}/

%files data -f %{name}.lang
%license LICENSES/*
%{_kf6_sysconfdir}/xdg/calligraplanrc
%{_kf6_sysconfdir}/xdg/calligraplanworkrc
%{_kf6_datadir}/calligraplan/
%{_kf6_datadir}/calligraplanwork/
%{_kf6_datadir}/config.kcfg/calligraplansettings.kcfg
%{_kf6_datadir}/config.kcfg/calligraplanworksettings.kcfg
%{_kf6_datadir}/kxmlgui5/calligraplan/
%{_kf6_datadir}/kxmlgui5/calligraplanportfolio/
%{_kf6_datadir}/kxmlgui5/calligraplanwork/
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}portfolio.*
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}work.*
%{_kf6_datadir}/icons/hicolor/*/mimetypes/application-x-vnd.kde.{kplato,plan}.*
%{_kf6_datadir}/mime/packages/calligraplanportfolio_mimetype.xml
%if %{with mpxj}
%{_kf6_datadir}/mime/packages/plan_mpxj_mimetype.xml
%endif


%changelog
* Sun Jan 11 2026 Yaakov Selkowitz <yselkowi@redhat.com> - 4.0.1-1
- 4.0.1

* Tue Jan 06 2026 Yaakov Selkowitz <yselkowi@redhat.com> - 4.0.0-1
- 4.0.0

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3.0-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 3.3.0-1
- calligraplan-3.3.0
- use new cmake macros
- revert BR: make (not needed)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.2.2-3
- pull in Qt5.15 upstream patch
- use %%make_install

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.2.2-1
- 3.2.2

* Sat Nov 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.2.1-1
- 3.2.1

* Thu Nov 14 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-3
- use %%make_build %%ldconfig_scriptlets
- upstream Qt-5.11 fixes

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Wed Jan 03 2018 Rex Dieter <rdieter@fedoraproject.org> 3.0.91-3
- -libs: really add ldconfig scriptlet
- fix icon dir ownership

* Tue Jan 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.0.91-2
- drop x-test locale
- -libs: +ldconfig scriptlet, delete lib.so symlinks, Provides: calligra-plan-libs

* Mon Jan 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.0.91-1
- calligraplan-3.0.91 

