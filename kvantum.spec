%global _vpath_srcdir Kvantum
%bcond_without  qt6

Name:           kvantum
Version:        1.0.10
Release:        %autorelease
Summary:        SVG-based theme engine for Qt, KDE and LXQt

License:        GPL-3.0-only
URL:            https://github.com/tsujan/Kvantum
Source0:        %url/archive/V%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  cmake(KF5WindowSystem)
%if %{with qt6}
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  kde-filesystem
Requires:       %{name}-data
Requires:       hicolor-icon-theme

%if %{with qt6}
Recommends:     (%{name}-qt6 if qt6-qtbase-gui)
%endif

%description
Kvantum is an SVG-based theme engine for Qt, tuned to KDE and LXQt, with an
emphasis on elegance, usability and practicality.

Kvantum has a default dark theme, which is inspired by the default theme of
Enlightenment. Creation of realistic themes like that for KDE was the first
reason to make Kvantum but it goes far beyond its default theme: you could
make themes with very different looks and feels for it, whether they be
photorealistic or cartoonish, 3D or flat, embellished or minimalistic, or
something in between, and Kvantum will let you control almost every aspect of
Qt widgets.

Kvantum also comes with many other themes that are installed as root and can
be selected and activated by using Kvantum Manager.

%if %{with qt6}
%package qt6
Summary:   SVG-based theme engine for Qt6
Requires:  %{name}-data

%description qt6
Kvantum is an SVG-based theme engine for Qt, tuned to KDE and LXQt, with an
emphasis on elegance, usability and practicality.

This package contains the Qt6 integration plugin.
%endif

%package data
Summary:    SVG-based theme engine for Qt5, KDE and LXQt
BuildArch:  noarch
Requires:   kvantum

%description data
Kvantum is an SVG-based theme engine for Qt, tuned to KDE and LXQt, with an
emphasis on elegance, usability and practicality.

This package contains the data needed Kvantum.

%prep
%autosetup -n Kvantum-%{version}

%build
%if %{with qt6}
%global _vpath_builddir %{_target_platform}-qt6
%cmake -DENABLE_QT5:BOOL=OFF
%cmake_build
%endif
%global _vpath_builddir %{_target_platform}-qt5
%cmake -DENABLE_QT5:BOOL=ON
%cmake_build

%install
%if %{with qt6}
%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
%endif
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install

# desktop-file-validate doesn't recognize LXQt
sed -i "s|LXQt|X-LXQt|" %{buildroot}%{_datadir}/applications/kvantummanager.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/kvantummanager.desktop

%find_lang %{name} --all-name --with-qt

%files -f %{name}.lang
%license Kvantum/COPYING
%doc Kvantum/ChangeLog Kvantum/NEWS Kvantum/README.md
%{_bindir}/kvantummanager
%{_bindir}/kvantumpreview
%{_qt5_plugindir}/styles/libkvantum.so

%if %{with qt6}
%files qt6
%license Kvantum/COPYING
%{_qt6_plugindir}/styles/libkvantum.so
%endif

%files data
%{_datadir}/Kvantum/
%{_datadir}/applications/kvantummanager.desktop
%{_datadir}/color-schemes/Kv*.colors
%{_datadir}/icons/hicolor/scalable/apps/kvantum.svg
%dir %{_datadir}/kvantumpreview
%dir %{_datadir}/kvantumpreview/translations
%dir %{_datadir}/kvantummanager
%dir %{_datadir}/kvantummanager/translations

%changelog
%autochangelog
