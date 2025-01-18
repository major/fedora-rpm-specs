
# koffice version to Obsolete
%global koffice_ver 3:2.3.70

Name:    calligraplan
Version: 3.3.0
Release: 11%{?dist}
Summary: A Project Planner 

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:     http://www.calligra-suite.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/calligra/%{version}/calligraplan-%{version}.tar.xz

## upstream patches

# %%check validation
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

# kf5
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Init)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)

#BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KChart) >= 2.8
BuildRequires: cmake(KGantt) >= 2.8

#BuildRequires: cmake(KF5CalendarCore)
#BuildRequires: cmake(KF5Contacts)
%ifarch %{qt5_qtwebengine_arches}
#BuildRequires: cmake(KF5AkonadiContact)
%endif

# optional
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Holidays)
BuildRequires: cmake(KReport)
BuildRequires: cmake(KPropertyWidgets)
BuildRequires: cmake(Qca-qt5)

# qt5
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5OpenGL)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5X11Extras)

BuildRequires: perl-interpreter
BuildRequires: zlib-devel

Obsoletes: koffice-kplato < %{koffice_ver}
Obsoletes: koffice-kplato-libs < %{koffice_ver}

Obsoletes: calligra-plan < 3.0.90
Provides:  calligra-plan = %{version}-%{release}

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%if 0%{?mpxj}
BuildRequires: java-devel
Requires: apache-poi
#Requires: apache-mpxj
%endif

%{?kf5_kinit_requires}

%description
Plan is a project management application. It is intended for managing
moderately large projects with multiple resources.

%package  libs
Summary:  Runtime libraries for %{name}
Obsoletes: calligra-plan-libs < 3.0.90
Provides:  calligra-plan-libs = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%autosetup -p1 -n calligraplan-%{version}


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

## unpackaged files
# bogus locale
rm -frv %{buildroot}%{_kf5_datadir}/locale/x-test/
# no need to package lib*.so symlinks
find  %{buildroot}%{_kf5_libdir}/  -maxdepth 1 -name lib*.so -type l -delete 

%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.calligraplan.appdata.xml 
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.calligraplan.desktop
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.calligraplanwork.desktop


%files -f %{name}.lang
%license COPYING*
%{_kf5_sysconfdir}/xdg/calligraplanrc
%{_kf5_sysconfdir}/xdg/calligraplanworkrc
%{_kf5_bindir}/calligraplan
%{_kf5_bindir}/calligraplanwork
%{_kf5_libdir}/libkdeinit5_calligraplan.so
%{_kf5_libdir}/libkdeinit5_calligraplanwork.so
%{_kf5_datadir}/kxmlgui5/calligraplan/
%{_kf5_datadir}/kxmlgui5/calligraplanwork/
%{_kf5_metainfodir}/org.kde.calligraplan.appdata.xml
%{_kf5_datadir}/applications/org.kde.calligraplan.desktop
%{_kf5_datadir}/applications/org.kde.calligraplanwork.desktop
%{_kf5_datadir}/calligraplan/
%{_kf5_datadir}/calligraplanwork/
%{_kf5_datadir}/config.kcfg/calligraplansettings.kcfg
%{_kf5_datadir}/config.kcfg/calligraplanworksettings.kcfg
%{_kf5_datadir}/icons/hicolor/*/*/*

%ldconfig_scriptlets libs

%files libs
%{_kf5_libdir}/libplanprivate.so.*
%{_kf5_libdir}/libplanworkfactory.so.*
%{_kf5_qtplugindir}/calligraplan/
%{_kf5_qtplugindir}/calligraplanworkpart.so
%{_kf5_libdir}/libplankernel.so.*
%{_kf5_libdir}/libplanmodels.so.*
%{_kf5_libdir}/libplanui.so.*
%{_kf5_libdir}/libplankundo2.so.*
%{_kf5_libdir}/libplanmain.so.*
%{_kf5_libdir}/libplanodf.so.*
%{_kf5_libdir}/libplanplugin.so.*
%{_kf5_libdir}/libplanstore.so.*
%{_kf5_libdir}/libplanwidgets.so.*
%{_kf5_libdir}/libplanwidgetutils.so.*


%changelog
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

