Name:          arianna
Version:       1.1.0
Release:       1%{?dist}
Summary:       EPub Reader for mobile devices
# Complete license breakdown can be found in the "LICENSE-BREAKDOWN" file.
License:       GPLv3
URL:           https://invent.kde.org/graphics/%{name}

Source:        https://invent.kde.org/graphics/arianna/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: kf5-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: qt5-qtbase-devel
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5WebSockets)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5FileMetaData)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5KirigamiAddons)
BuildRequires: cmake(KF5QQC2DesktopStyle)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(KF5Baloo)
BuildRequires: cmake(KF5QuickCharts)
BuildRequires: reuse
BuildRequires: fdupes
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

# QML module dependencies
Requires: kf5-kirigami2%{?_isa}
Requires: kf5-kirigami2-addons%{?_isa}
Requires: kf5-kquickcharts%{?_isa}
Requires: qt5-qtgraphicaleffects%{?_isa}
Requires: qt5-qtquickcontrols2%{?_isa}
Requires: qt5-qtwebchannel%{?_isa}
Requires: qt5-qtwebengine%{?_isa}

%if 0%{?fedora} || 0%{?epel} > 7
# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
# Package doesn't build on arches that qtwebengine is not built on.
ExclusiveArch: %{qt5_qtwebengine_arches}
%endif

%description
An ebook reader and library management app


%prep
%autosetup -n %{name}-v%{version} -p1

%build
%cmake_kf5
%cmake_build
%fdupes

%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.arianna.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.arianna.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/arianna
%{_datadir}/applications/org.kde.arianna.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.arianna.svg
%{_datadir}/metainfo/org.kde.arianna.appdata.xml
%{_datadir}/qlogging-categories5/arianna.categories

%changelog
* Sun Jun 11 2023 Steve Cossette <farchord@gmail.com> - 1.1.0-1
- This release adds a table of content overview as well as a book detail dialog.

* Mon May 29 2023 Steve Cossette <farchord@gmail.com> - 1.0.1-2
- Added more install dependancies
- Cleaned up the licensing text by moving the license breakdown to a separate file

* Sun May 21 2023 Steve Cossette <farchord@gmail.com> - 1.0.1-1
- Initial release
