
# enable qt5 support (will probbably make this non-optional soon)
%global qt5 1

%undefine __cmake_in_source_build

Name:		qtcurve
Summary:        A set of widget styles for GTK+ and Qt widget toolkits
Version:	1.9.1
Release:	32%{?dist}

# KDE e.V. may determine that future LGPL versions are accepted
# Automatically converted from old format: LGPLv2 or LGPLv3 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
#URL:		http://www.kde-look.org/content/show.php?content=40492
URL:            https://cgit.kde.org/?p=%{name}
Source0:        https://github.com/KDE/qtcurve/archive/%{version}.tar.gz#/qtcurve-%{version}.tar.gz

## upstream patches (master branch)
Patch37: 0037-utils-gtkprops-Remove-unnecessary-constexpr-this-is-.patch
Patch66: 0066-Fix-build-with-Qt-5.15-missing-QPainterPath-include.patch

## downstream patches
Patch101:  qtcurve-1.8.18-no_env.patch

# for autosetup -Sgit
BuildRequires:  git-core
BuildRequires:  cmake
BuildRequires:	gettext
BuildRequires:  gtk2-devel
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(QtGui)
%if 0%{?qt5}
BuildRequires:  pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets) pkgconfig(Qt5Svg) pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-frameworkintegration-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kxmlgui-devel
%endif

# main metapackage
Requires: %{name}-gtk2%{?_isa} = %{version}-%{release}
Requires: %{name}-qt4%{?_isa} = %{version}-%{release}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: %{name}-kf5%{?_isa} = %{version}-%{release}

%description
QtCurve is a desktop theme for the GTK+ and Qt widget toolkits,
allowing users to achieve a uniform look between these widget toolkits.

%package libs
Summary: Runtime libraries for QtCurve
%description libs
%{summary}.

%package gtk2
Summary: QtCurve gtk2 style support
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description gtk2
%{summary}.

%package qt4
Summary: QtCurve Qt4 style support
Obsoletes: qtcurve-kde4 < 1.8.18
Provides:  qtcurve-kde4 = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description qt4
%{summary}.

%package qt5
Summary: QtCurve Qt5 style support
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description qt5
%{summary}.

%package kf5
Summary: QtCurve KF5/Plasma support
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
## not sure yet -- rex
#Requires: plasma-workspace
%description kf5
%{summary}.


%prep
%autosetup -Sgit


%build
%cmake \
  -DQTC_QT4_ENABLE_KDE:BOOL=OFF \
  -DDENABLE_QT5:BOOL=%{?qt5:ON}%{!?qt5:OFF}

%cmake_build


%install
%cmake_install

# unpackaged files
rm -fv %{buildroot}%{_libdir}/libqtcurve-{cairo,utils}.so


%files -n qtcurve
# empty metapackage

%ldconfig_scriptlets libs

%files libs
%doc AUTHORS Bugs.md README.md TODO.md ChangeLog.md
%license COPYING
%{_libdir}/libqtcurve-utils.so.2*

%ldconfig_scriptlets gtk2

%files gtk2
%{_libdir}/gtk-2.0/*/engines/libqtcurve.so
%{_libdir}/libqtcurve-cairo.so.1*
%{_datadir}/themes/QtCurve/

%files qt4
%{_qt4_plugindir}/styles/qtcurve.so

%files qt5
%{_qt5_plugindir}/styles/qtcurve.so

%files kf5
%{_kf5_qtplugindir}/kstyle_qtcurve5_config.so
%{_kf5_datadir}/kstyle/themes/qtcurve.themerc
%{_kf5_datadir}/kxmlgui5/QtCurve/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.1-31
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 1.9.1-24
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 1.9.1-23
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 1.9.1-22
- Rebuild (qt5)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1.9.1-19
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 07:55:12 CET 2020 Jan Grulich <jgrulich@redhat.com> - 1.9.1-17
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 1.9.1-16
- rebuild (qt5)

* Mon Aug 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.9.1-15
- FTBFS, use new %%cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.9.1-12
- pull in upstream Qt 5.15 fix

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.9.1-11
- rebuild (qt5)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 1.9.1-9
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 1.9.1-8
- rebuild (qt5)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 1.9.1-6
- rebuild (qt5)

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.9.1-5
- rebuild (qt5)

* Mon Feb 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.9.1-4
- rebuild (qt5)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.9.1-2
- rebuild (qt5)

* Wed Sep 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.9.1-1
- 1.9.1
- URL: use kde.org
- .spec cleanup, use %%make_build %%ldconfig_scriptlets

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.18-12.g330bfa5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.8.18-11.g330bfa5
- rebuild (qt5)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.18-10.g330bfa5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.8.18-9.g330bfa5
- BR: qt5-qtbase-private-devel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.18-8.g330bfa5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.18-7.g330bfa5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.18-6.g330bfa5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 01 2016 Rex Dieter <rdieter@fedoraproject.org> 1.8.18-5.g330bfa5
- update URL (#1325314)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.18-4.g330bfa5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Rex Dieter <rdieter@fedoraproject.org> 1.8.18-3.g330bfa5
- -gtk2: lose dependency on /usr/bin/env

* Mon Oct 26 2015 Rex Dieter <rdieter@fedoraproject.org> 1.8.18-2.g330bfa5
- -qt5/-kf5 subpkgs

* Wed Oct 21 2015 Rex Dieter <rdieter@fedoraproject.org> 1.8.18-1
- qtcurve-1.8.18, qtcurve-qt4 qtcurve-gtk2 build from one place
